from django.apps import AppConfig


class AppAdvsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advs'
    verbose_name = 'Объявления' # изменение названия приложения в админке, для домашки
