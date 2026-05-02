# 🛒 PyShop – Django E-commerce Website

A full-stack eCommerce web application built using Django.  
Users can browse products, add items to cart, place orders, and manage accounts.

---

## 🚀 Live Demo
🔗 https://pyshop-ecommerce.onrender.com  

---

## ✨ Features

- 🔐 User Authentication (Login / Register / Logout)
- 🔑 Forgot Password (Email-based reset)
- 🛍️ Product Listing & Categories
- 🛒 Add to Cart / Remove from Cart
- 📦 Order Management
- 👤 User Profile Management
- 🧾 Admin Dashboard (Django Admin)
- ☁️ Cloudinary Integration for Image Storage
- 🌐 Deployed on Render

---

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Database:** PostgreSQL (Production), SQLite (Development)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render  
- **Media Storage:** Cloudinary  
- **Other Tools:** Gunicorn, WhiteNoise  

---

## ⚙️ Installation (Local Setup)

> ⚠️ Note: This project is configured primarily for production deployment (Render + PostgreSQL + Cloudinary).  
> Some adjustments may be required to run it locally.

```bash
git clone https://github.com/RajatKumarBal779/pyshop-ecommerce.git
cd ecom

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🔑 Environment Variables

- SECRET_KEY=your_secret_key
- DEBUG=True

### Use SQLite locally or provide PostgreSQL URL
- DATABASE_URL=sqlite:///db.sqlite3

- EMAIL_HOST_USER=your_email
- EMAIL_HOST_PASSWORD=your_app_password

### Cloudinary (required for image handling)
- CLOUDINARY_CLOUD_NAME=your_cloud_name
- CLOUDINARY_API_KEY=your_api_key
- CLOUDINARY_API_SECRET=your_api_secret

> ⚠️ Notes Media files (uploaded images) may not persist on free hosting (Render free tier).
> Recommended to use cloud storage for production.

--- 

## 📌 Future Improvements
- 💳 Razorpay Payment Integration
- ☁️ Cloud Storage for Media (AWS S3 / Cloudinary)
- 📱 Improved UI/UX
- 📊 Order Tracking System

--- 

## Author & Contact
<strong>Rajat Kumar Bal</strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a>
<div align = 'center'>
   Made With 💖  by <strong>Rajat</strong>
</div>
