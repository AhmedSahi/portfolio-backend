# Portfolio Backend (Django REST Framework)

This is the backend for my personal portfolio, built with Django. It handles contact form submissions and sends emails using Gmail SMTP.

##  Features
- **Contact API:** Receives messages from the frontend.
- **Email Notifications:** Sends real-time emails via Gmail.
- **Secure:** Uses environment variables for sensitive data.

##  Tech Stack
- Python / Django
- Django REST Framework (DRF)
- Django-cors-headers (CORS)
- Python-decouple

##  Installation
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`.
3. Set up your `.env` file.
4. Run: `python manage.py runserver`.
