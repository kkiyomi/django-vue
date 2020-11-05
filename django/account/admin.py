from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from .models import *


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'tvshow', 'readinglist', 'current_release_id', 'release')
    search_fields = ('readinglist',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ('readinglist',)
    fieldsets = ()


class ReadingListAdmin(admin.ModelAdmin):
    list_display = ('account', 'pk')
    search_fields = ('account', 'pk')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]


admin.site.register(Account, AccountAdmin)
admin.site.register(ReadingList, ReadingListAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
