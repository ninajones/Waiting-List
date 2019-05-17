from django.contrib import admin

# Register your models here.
from waitinglist.models import Entry

# admin.site.register(Entry)


# Define the admin class
class EntryAdmin(admin.ModelAdmin):
    list_display = ('your_last_name', 'your_first_name', 'contact_information', 'created_at', 'updated_at', 'date_of_birth_of_child')
    fields = ['your_first_name', 'your_last_name', 'contact_information', 'created_at', 'updated_at', 'date_of_birth_of_child']


# Register the admin class with the associated model
admin.site.register(Entry, EntryAdmin)
