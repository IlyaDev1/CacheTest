from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.CharField(max_length=100, blank=False, null=False, unique=True, db_index=True)


class Passport(models.Model):
    series = models.CharField(max_length=4, blank=False, null=False)
    number = models.CharField(max_length=6, blank=False, null=False)
    slug = models.CharField(max_length=11, unique=True, null=True)
    person = models.OneToOneField(Person, on_delete=models.PROTECT, null=True, blank=False, related_name='passport')

