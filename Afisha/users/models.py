from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class CustomUser(AbstractUser):
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=False)