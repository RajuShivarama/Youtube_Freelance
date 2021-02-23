from django.contrib import admin
from .models import Hiretuber

# Register your models here.
class HrAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'email', 'tuber_name')
    search_fields = ('first_name', )

admin.site.register(Hiretuber, HrAdmin)