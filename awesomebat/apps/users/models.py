from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)

    def __str__(self):
        return self.email