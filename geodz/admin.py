from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static

from models import Municipality, Province


class GeodzModelAdmin(admin.ModelAdmin):

    def google_maps(self, obj):

        html = u'<a target="_blank" href="{0}"><img src="{1}" width="16" height="16" alt="" /></a>'

        return format_html(html,
            obj.get_gmaps_query_url(),
            static('img/gmaps.png')
        )

    google_maps.allow_tags = True


class MunicipalityAdmin(GeodzModelAdmin):
    list_display = ('name', 'province', 'google_maps')
    list_filter = ('province',)
    search_fields = ('name',)

class ProvinceAdmin(GeodzModelAdmin):
    list_display = ('code', 'name', 'municipality_count', 'google_maps')
    list_display_links = ('name',)
    search_fields = ('name', 'code',)

    def municipality_count(self, obj):
        return obj.municipalities.count()

admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Province, ProvinceAdmin)