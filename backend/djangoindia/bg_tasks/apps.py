from django.apps import AppConfig


class BgTasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangoindia.bg_tasks"

    def ready(self):
        import djangoindia.bg_tasks.dbbackup
