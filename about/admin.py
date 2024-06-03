from django.contrib import admin
from .models import About, Contact, TeamMember, Services


# Organizaation admin
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(TeamMember)
admin.site.register(Services)

