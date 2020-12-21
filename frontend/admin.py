from django.contrib import admin

# Register your models here.
from .models import Metadatas, ContactDetails, ContactMessage, Footer, Work, Whoweare, Blog


admin.site.register(Metadatas)

admin.site.register(ContactDetails)

admin.site.register(ContactMessage)

admin.site.register(Footer)

admin.site.register(Work)

admin.site.register(Whoweare)

admin.site.register(Blog)

