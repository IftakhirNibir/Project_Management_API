from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Project,ProjectMember,Task,Comment])