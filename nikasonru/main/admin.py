from django.contrib import admin
from .models import Message, Portfolio, BeforeAfter, SmiAboutUs, ClientsAboutUs
# Register your models here.
admin.site.register(Message)
admin.site.register(Portfolio)
admin.site.register(BeforeAfter)
admin.site.register(SmiAboutUs)
admin.site.register(ClientsAboutUs)