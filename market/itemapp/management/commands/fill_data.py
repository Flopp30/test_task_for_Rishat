import json

from django.core.management import BaseCommand
from itemapp.models import Item
from django.contrib.auth.models import User
from django.conf import settings


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Item.objects.all().delete()

        items = load_from_json('items')

        for item in items:
            Item.objects.create(**item)

        User.objects.all().delete()
        User.objects.create_superuser(username='admin', email='django@django.local', password='admin')
