from . import views
from django.urls import path

app_name='candidature'

urlpatterns = [
    path('', views.index, name ="postes"),
    path('<int:poste_id>/candidatureForm', views.candidatureForm, name ="candidatureform"),
]