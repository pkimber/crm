from datetime import datetime

from django.core.management.base import BaseCommand

from crm.tests.model_maker import (
    make_contact,
    make_industry,
    make_priority,
    make_ticket,
    make_user_contact,
)
from login.tests.model_maker import make_user


class Command(BaseCommand):

    help = "Create demo data for 'crm'"

    def handle(self, *args, **options):
        fred = make_user('fred')
        make_user('matt')
        contact = make_contact(
            'pkimber',
            'Patrick Kimber',
            address='High Street\nExeter\nDevon',
            mail='mail@pkimber.net',
            url='https://pkimber.net',
            phone='01837 123 456',
            industry=make_industry('Farming'),
        )
        make_user_contact(fred, contact)
        description = """Hey diddle diddle rhyme
Hey diddle diddle, the cat and the fiddle,
The cow jumped over the moon.
The little dog laughed to see such fun
And the dish ran away with the spoon!
        """
        make_ticket(
            contact,
            "Milk the cows",
            description,
            make_priority('High', 1),
            due=datetime.today(),
        )
        make_contact(
            'ssmith',
            'Sam Smith',
            industry=make_industry('Leisure'),
        )
        print("Created 'crm' demo data...")
