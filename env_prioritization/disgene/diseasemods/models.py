# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DiseaseModule(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default="Module description")
	def __unicode__(self):
		return  self.name
		