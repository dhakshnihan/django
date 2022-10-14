from django.contrib import admin
from apple.models import Tiru
class tiruadmin(admin.ModelAdmin):
    list_display=['id','name','adress','age']
# Register your models here.
admin.site.register(Tiru)
