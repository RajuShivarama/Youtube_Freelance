from django.contrib import admin

from .models import Contacttuber

class CtAdmin(admin.ModelAdmin):

    list_display = ('id', 'full_name', 'email', 'phone')
    search_fields = ('full_name', )


# Register your models here.
admin.site.register(Contacttuber,CtAdmin)
