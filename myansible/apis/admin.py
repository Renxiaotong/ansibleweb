from django.contrib import admin
from apis.models import Hosts,Groups,Argument,Module
# Register your models here.

for item in [Hosts,Groups,Argument,Module]:
    admin.site.register(item);