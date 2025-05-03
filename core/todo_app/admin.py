from django.contrib import admin
from .models import AddTodo
# Register your models here.
class AddtodoAdmin(admin.ModelAdmin):
    list_display = ["task"]


admin.site.register(AddTodo, AddtodoAdmin)