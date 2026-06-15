from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from database import supabase
import datetime

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"])
SECRET = "your-secret-key-change-this"  # change this to any random string

# --- Models (what data we expect from frontend) ---
class SignupData(BaseModel):
    name: str
    email: str
    password: str
    phone: str = None

class LoginData(BaseModel):
    email: str
    password: str

# --- Signup ---
@router.post("/signup")
def signup(data: SignupData):
    # Check if email already exists
    existing = supabase.table("users").select("id").eq("email", data.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Save user with hashed password (never store plain passwords!)
    hashed = pwd.hash(data.password)
    supabase.table("users").insert({
        "name": data.name,
        "email": data.email,
        "password_hash": hashed,
        "phone": data.phone
    }).execute()

    return {"message": "Account created successfully!"}
        
# --- Login ---
@router.post("/login")
def login(data: LoginData):
    # Find user by email
    result = supabase.table("users").select("*").eq("email", data.email).execute()
    if not result.data:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    user = result.data[0]

    # Check password
    if not pwd.verify(data.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Create a token (like a key the user carries for future requests)
    token = jwt.encode({
        "user_id": str(user["id"]),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, SECRET, algorithm="HS256")

    return {
        "token": token,
        "name": user["name"],
        "email": user["email"]
    }