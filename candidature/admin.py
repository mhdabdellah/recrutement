from django.contrib import admin
from .models import Candidature

# Register your models here.

class  CandidatureAdmin(admin.ModelAdmin):
    fields = ['poste','nom','prenom','email','telephone','cv']
    list_display = ['poste','nom','prenom','email','telephone','cv']
    list_display_links = ['poste']
    # list_filter = ['poste','nom','prenom','email','telephone']
    search_fields = ['poste','nom','prenom','email','telephone']



admin.site.register(Candidature,CandidatureAdmin)
