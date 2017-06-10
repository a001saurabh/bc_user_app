# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Users(models.Model):
    user_id = models.CharField(max_length = 10)
    joining_date = models.DateTimeField('date joined')
    name = models.CharField(max_length = 40)
    fathers_name = models.CharField(max_length = 40)
    classs = models.IntegerField()
    school = models.CharField(max_length = 40)

    def __str__(self):
        return self.name
