from django.urls import path, re_path
from . import views

app_name = 'mango_app'  # Added app_name for URL namespacing

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('pests/', views.PestsView.as_view(), name='pests'),
    path('diseases/', views.DiseasesView.as_view(), name='diseases'),
    path('surveillance/', views.SurveillanceView.as_view(), name='surveillance'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    # URL pattern with regex for project detail pages
    re_path(r'^projects/(?P<item_id>\d+)/$', views.MangoItemDetailView.as_view(), name='project_detail'),
]