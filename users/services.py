import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_product(name):
    return stripe.Product.create(name=name)


def create_price(product_id, amount):
    return stripe.Price.create(
        unit_amount=amount,
        currency="rub",
        product=product_id,
    )


def create_checkout_session(price_id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://127.0.0.1:8000/",
        cancel_url="http://127.0.0.1:8000/",
    )
    return session
