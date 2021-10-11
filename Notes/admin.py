from Notes.models import createnotes
from django.contrib import admin

# Register your models here.
admin.site.register(createnotes)

admin.site.site_header="Admin Panel"
admin.site.site_title="Notes"
admin.site.index_title="Create notes"
