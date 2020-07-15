from django.apps import AppConfig


class UserApiConfig(AppConfig):
    name = 'user_api'

    def ready(self):
        import user_api.signals
