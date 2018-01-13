from django.apps import AppConfig

class OrdersAppConfig(AppConfig):
    name = "orders" # Здесь указываем исходное имя приложения
    verbose_name = "заказы" # А здесь, имя которое необходимо отобразить в админке