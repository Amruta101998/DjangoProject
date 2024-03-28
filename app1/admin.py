#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import YourModel  # Import your model(s) here

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Add fields you want to display in the admin list view
    search_fields = ('field1', 'field2')  # Add fields you want to search in the admin

# If you have more models, you can register them in a similar fashion
# Example:
# from .models import AnotherModel
# 
# @admin.register(AnotherModel)
# class AnotherModelAdmin(admin.ModelAdmin):
#     list_display = ('fieldA', 'fieldB')
#     search_fields = ('fieldA', 'fieldB')
