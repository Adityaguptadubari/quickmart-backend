from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import supabase
from routes import users, orders

app = FastAPI(title="QuickMart API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(users.router, tags=["Users"])
app.include_router(orders.router, tags=["Orders"])

@app.get("/products")
def get_products():
    response = supabase.table("products").select("*").execute()
    return response.data
@app.get("/")
def home():
    return {"message": "QuickMart backend running 🚀"}