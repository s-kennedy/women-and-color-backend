# Django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.middleware.csrf import get_token
from allauth.account.views import PasswordResetView
from mailchimp3 import MailChimp

# App
from wac.apps.accounts.models import Profile

import hashlib

class Command(BaseCommand):
    help = "Add all users who are not already subscribed to a mailing list. Takes two arguments: 'target_list_id' is the id of the list to subscribe the email to and 'check_list_id' is the id of the list to check if the email is already subscribed."

    def check_if_subscribed(self, profile, list_id, client):
        email_hash = hashlib.md5(profile.user.email.encode('utf-8')).hexdigest()

        subscriber = client.lists.members.get(
            list_id=list_id,
            subscriber_hash=email_hash
        )

        print("subscriber")
        print(subscriber)

        return subscriber.status == 'subscribed'


    def subscribe_to_list(self, profile, list_id, client):
        email_hash = hashlib.md5(profile.user.email.encode('utf-8')).hexdigest()

        client.lists.members.create_or_update(
            list_id=list_id,
            subscriber_hash=email_hash,
            data={
                'email_address': profile.user.email,
                'status': 'subscribed',
                'status_if_new': 'subscribed',
                'merge_fields': {
                  'FNAME': profile.first_name,
                  'LNAME': profile.last_name,
                  'ICITY': profile.location.city if profile.location else "undisclosed location",
            },
          }
        )

    def add_arguments(self, parser):
        parser.add_argument('target_list_id')
        parser.add_argument('check_list_id')

    def handle(self, *args, **options):
        profiles = Profile.objects.all()
        target_list_id = options['target_list_id']
        check_list_id = options['check_list_id']
        client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, timeout=10.0)

        for profile in profiles:
            already_subscribed = self.check_if_subscribed(profile, check_list_id, client)
            if already_subscribed:
                self.stdout.write(self.style.SUCCESS('Email already subscribed to {}: {}'.format(check_list_id, profile.user.email)))
            else:
                self.subscribe_to_list(profile, target_list_id, client)
                self.stdout.write(self.style.SUCCESS('New email subscribed to {}: {}'.format(target_list_id, profile.user.email)))



