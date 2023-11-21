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
    #path('<str:path>/', views.error_404),
    path('hit_mhs/', views.error_404),
    path('hit_mhs/<str:hit_mhs>/', views.hit_mhs),  # Add a path with a dynamic parameter
    path('detail_mhs/', views.error_404),
    path('detail_mhs/<str:detail_mhs>/', views.detail_mhs),
    path('hit/', views.error_404),
    path('hit/<str:hit>/', views.hit),
    path('detail_dosen/', views.error_404),
    path('detail_dosen/<str:detail_dosen>/', views.detail_dosen),
    path('detail_prodi/', views.error_404),
    path('detail_prodi/<str:detail_prodi>/', views.detail_prodi),
    path('detail_prodi_undifined/', views.error_404),
    path('detail_prodi_undifined/<str:detail_prodi_undifined>/', views.detail_prodi_undifined),
    path('detail_pt/', views.error_404),
    path('detail_pt/<str:detail_pt>/', views.detail_pt),
    path('stat_pt/', views.error_404),
    path('stat_pt/<str:stat_pt>/', views.stat_pt),

    # v2
    path('v2/detail_pt/', views.error_404),
    path('v2/detail_pt/<str:detail_pt_v2>/', views.detail_pt_v2),
    path('v2/detail_pt_prodi/', views.error_404),
    path('v2/detail_pt_prodi/<str:detail_pt_prodi_v2>/', views.detail_pt_prodi_v2),
    path('v2/detail_pt_jumlah/', views.error_404),
    path('v2/detail_pt_jumlah/<str:detail_pt_jumlah_v2>/', views.detail_pt_jumlah_v2),
    path('v2/detail_pt_dosen/', views.error_404),
    path('v2/detail_pt_dosen/<str:detail_pt_dosen_v2>/', views.detail_pt_dosen_v2),
]