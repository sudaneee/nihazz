from django.contrib import admin
from website.models import (
    Slider,
    GeneralSettings,
    Program,
    Update,
    Event,
)

admin.site.register(Slider)
admin.site.register(GeneralSettings)
admin.site.register(Program)
admin.site.register(Update)
admin.site.register(Event)

