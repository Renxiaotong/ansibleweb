from django.contrib import admin
from apis.models import Hosts,Groups,Argument,Module


for item in [Hosts,Groups,Argument,Module]:
    admin.site.register(item);
