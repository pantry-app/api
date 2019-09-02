from django.core.management.base import BaseCommand

from account.models import User


class Command(BaseCommand):
    help = "Create records necessary for e2e testing"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        user = User.objects.create(email="tester@tmk.name")
        user.set_password("supersecretpassword123")
        user.save()

        self.stdout.write(f"Created user: {user}")
