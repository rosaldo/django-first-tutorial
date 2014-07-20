from django.contrib import admin
from polls.models import Poll


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

admin.site.register(Poll, PollAdmin)
