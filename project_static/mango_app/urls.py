from django.urls import path
from . import views

app_name = 'mango_app'  # Added app_name for URL namespacing

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('pests/', views.PestsView.as_view(), name='pests'),
    path('diseases/', views.DiseasesView.as_view(), name='diseases'),
    path('surveillance/', views.SurveillanceView.as_view(), name='surveillance'),
    path('about/', views.AboutView.as_view(), name='about'),
]