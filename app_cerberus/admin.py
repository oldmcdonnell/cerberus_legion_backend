from django.contrib import admin
from app_cerberus.models import Profile

class ProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)