from django.dispatch import receiver
from store.signals import order_created


@receiver(order_created)
def on_order_created(sender, **kwargs):
    """Signal handler that performs actions when an order is created."""
    order = kwargs.get('order')
    # Implement any logic needed when an order is created
    print(f"Order created with ID: {order.id}")
