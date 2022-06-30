from django.contrib import admin
from api.models import Stdnt# Register your models here.
@admin.register(Stdnt)
class StdnAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']