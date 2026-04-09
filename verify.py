import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from apps.training.models import TrainingSession
from django.utils import timezone
from datetime import timedelta

client = Client(SERVER_NAME='localhost')

TrainingSession.objects.all().delete()

session = TrainingSession.objects.create(
    title="Test Session",
    start_time=timezone.now(),
    end_time=timezone.now() + timedelta(hours=1),
    description="A session for testing"
)
print("Created session:", session.title)

response = client.post(
    '/graphql/',
    data=json.dumps({'query': '{ trainings { id title } }'}),
    content_type='application/json'
)
print("Without token:", response.json())

response = client.post(
    '/api/token/',
    data={'username': 'admin', 'password': 'admin'},
)
token = response.json().get('access')
print("Got token:", "YES" if token else "NO")

response = client.post(
    '/graphql/',
    data=json.dumps({'query': '{ trainings { id title } }'}),
    content_type='application/json',
    HTTP_AUTHORIZATION=f'Bearer {token}'
)
print("With token:", response.json())
