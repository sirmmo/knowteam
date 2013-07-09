from django.contrib import admin
from ktree.models import *


class TermAdmin(admin.ModelAdmin):
    pass
admin.site.register(Term, TermAdmin)
class LinkTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(LinkType, LinkTypeAdmin)
class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link, LinkAdmin)