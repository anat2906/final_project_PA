from django.contrib import admin
from .models import Message, InCompanies, Company, Membership

admin.site.register(Message)
admin.site.register(InCompanies)
admin.site.register(Company)
admin.site.register(Membership)