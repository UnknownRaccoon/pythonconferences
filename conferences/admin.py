from django.contrib import admin
from . import models


class ParticipationInline(admin.TabularInline):
    model = models.Participation
    extra = 1


class ConferenceAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)


admin.site.register(models.Conference, ConferenceAdmin)
