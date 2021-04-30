from django.contrib import admin

# Register your models here.
from data.models import *

admin.site.register(Blog)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(QA)
admin.site.register(Domain)
admin.site.register(Developer)


