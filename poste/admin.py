from django.contrib import admin

from poste.models import Poste

# Register your models here.

admin.site.site_header = "Recrutement Mhd Abdellahi Tech"
admin.site.site_title = "Recrutement Mhd Abdellahi Tech"


class  PosteAdmin(admin.ModelAdmin):
    fields = ['title','recruteur','objectif_a_recruter','departement','lieu_travail','type_emploi','email']
    # fields = '__all__'
    # exclude=['recruteur']
    list_display = ['title','recruteur','objectif_a_recruter','departement','lieu_travail','type_emploi','email']
    list_display_links = ['title']
    # list_editable = ['title','recruteur','objectif_a_recruter','departement','lieu_travail','type_emploi','lieuResidance','email']
    list_filter = ['title','recruteur','objectif_a_recruter','departement','lieu_travail','type_emploi']
    search_fields = ['title','recruteur','objectif_a_recruter','departement','lieu_travail','type_emploi']


admin.site.register(Poste,PosteAdmin)
