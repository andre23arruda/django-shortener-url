from django.contrib import admin
from django.conf.locale.pt_BR import formats
from .models import Url

formats.DATE_FORMAT = 'd/m/Y'

@admin.register(Url)
class UrlRegister(admin.ModelAdmin):
    list_display = ('id', 'long_url', 'short_url', 'registered_at', 'is_valid',)
    list_display_links = ('id', 'long_url', 'short_url')

    @admin.display(boolean=True, description='Is valid')
    def is_valid(self, obj):
        return obj.is_valid()
