from django.db import models
from base.models.base import BaseEntity


class Office(BaseEntity):
    name = models.CharField(max_length=120)
    address = models.TextField()
    employee = models.IntegerField(help_text='How many employees there?')
    code = models.IntegerField(default=123)
    logo = models.ImageField(upload_to='office', blank=True, null=True)

    def __str__(self):
        return self.name
