from django.contrib import admin
from enquire.models import Enquire
# Register your models here.
class EnquireAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'mobile', 'email')

admin.site.register(Enquire, EnquireAdmin)