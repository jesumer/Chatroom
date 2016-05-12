from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "soa"

    def ready(self):
        import_module("soa.receivers")
