# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.error_404),
# ]

# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.error_404),  # Example path for the error_404 view
    path('hit_mhs/', views.hit_mhs_404),
    path('hit_mhs/<str:hit_mhs>/', views.hit_mhs),  # Add a path with a dynamic parameter
]