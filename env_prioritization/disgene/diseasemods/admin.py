# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  .models import DiseaseModule

# Register your models here.

class DiseaseModuleAdmin(admin.ModelAdmin):
	pass

admin.site.register(DiseaseModule, DiseaseModuleAdmin)