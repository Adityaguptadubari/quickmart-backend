from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import supabase
from typing import List

router = APIRouter()

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: int

class OrderData(BaseModel):
    user_id: str
    address: str
    total_price: int
    items: List[OrderItem]

# --- Place a new order ---
@router.post("/orders")
def place_order(data: OrderData):
    # Save the order
    order = supabase.table("orders").insert({
        "user_id": data.user_id,
        "total_price": data.total_price,
        "address": data.address,
        "status": "pending"
    }).execute()

    order_id = order.data[0]["id"]

    # Save each item in the order
    items = [
        {
            "order_id": order_id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": item.price
        }
        for item in data.items
    ]
    supabase.table("order_items").insert(items).execute()

    return {"message": "Order placed!", "order_id": order_id}

# --- Get all orders for a user ---
@router.get("/orders/{user_id}")
def get_orders(user_id: str):
    result = supabase.table("orders").select("*").eq("user_id", user_id).execute()
    return result.data