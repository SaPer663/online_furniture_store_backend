from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """Приложение заказы."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
    verbose_name = 'Заказы'
