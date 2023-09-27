from django.contrib import admin
from contactForm.models import contactFields

class contactDataAdmin(admin.ModelAdmin):
    form_list=('Name', "Email", "Phone", "Website_Link", "Country", "Message")
admin.site.register(contactFields,contactDataAdmin)
# Register your models here.
