from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

import uuid

def short_uuid():
    return str(uuid.uuid4())[:8]


def next_7_days():
    '''Retorna data com mais sete dias de diferença'''
    return date.today() + timedelta(days=7)


class Url(models.Model):
    registered_at = models.DateField(auto_now_add=True)
    expired_at = models.DateField(default=next_7_days)
    long_url = models.URLField()
    short_url = models.CharField(max_length=8, default=short_uuid, unique=True)

    def __str__(self):
        return f'{ self.short_url }'

    def is_valid(self):
        '''Retorna se Url já está expirada'''
        return self.expired_at >= date.today()