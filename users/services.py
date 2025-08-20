import stripe
from dotenv import load_dotenv

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

load_dotenv()

def create_product(name, description):
    """Создание продукта"""
    product = stripe.Product.create(
        name=name,
        description=description
    )
    return product

def create_price(product, amount):
    """Создание цены"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product.id
    )
    return price

def create_session_to_url(price):
    """Создание сессии для получения ссылки на оплату"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{
            "price": price.id,
            "quantity": 1
        }],
        mode="payment",
    )
    return session.get("id"), session.get("url")
