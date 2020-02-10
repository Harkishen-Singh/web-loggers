# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

class GeneralLogger(models.Model):
    usr_filepath = models.CharField(max_length=50)
    sys_time = models.DateTimeField()
    message = models.CharField(max_length=225)

