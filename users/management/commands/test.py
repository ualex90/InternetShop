from django.core.management import BaseCommand

from users import utils


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        utils.get_user_key()