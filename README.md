# QuickMart Backend 🛒⚡

A Python FastAPI backend for QuickMart — a Blinkit-style quick commerce app.

## 🚀 Live API
https://quickmart-backend-production-c5d1.up.railway.app

## 🛠️ Tech Stack
- **Python** — core language
- **FastAPI** — web framework
- **Supabase** — PostgreSQL database
- **Railway** — cloud deployment

## 📦 Features
- Get all products
- Filter products by category
- User signup & login (JWT auth)
- Place orders
- View order history

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | Get all products |
| GET | /products/{category} | Filter by category |
| POST | /signup | Create account |
| POST | /login | Login & get token |
| POST | /orders | Place an order |
| GET | /orders/{user_id} | Get user orders |

## 🏃 Run Locally
```bash
# Clone the repo
git clone https://github.com/Adityaguptadubari/quickmart-backend.git
cd quickmart-backend

# Install dependencies
pip install -r requirements.txt

# Add your .env file
SUPABASE_URL=your-url
SUPABASE_KEY=your-key

# Start server
python -m uvicorn main:app --reload
```

## 👨‍💻 Author
Aditya Gupta — [GitHub](https://github.com/Adityaguptadubari)
