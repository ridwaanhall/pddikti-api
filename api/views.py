# api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests

@api_view(['GET'])
def error_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

'''
notice: mhs_id not same as nim.
'''

# ============= mahasiswa ==================
# search hit mhs (using name/nim/college/combination of that)
@api_view(['GET'])
def hit_mhs(request, hit_mhs):
    url = f'https://api-frontend.kemdikbud.go.id/hit_mhs/{hit_mhs}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail mhs (using mhs id)
@api_view(['GET'])
def detail_mhs(request, detail_mhs):
    url = f'https://api-frontend.kemdikbud.go.id/detail_mhs/{detail_mhs}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# ============== dosen, prodi, pt ===============
# search hit (dosen, prodi, and pt)
@api_view(['GET'])
def hit(request, hit):
    url = f'https://api-frontend.kemdikbud.go.id/hit/{hit}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail dosen
@api_view(['GET'])
def detail_dosen(request, detail_dosen):
    url = f'https://api-frontend.kemdikbud.go.id/detail_dosen/{detail_dosen}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail prodi (detail of prodi using id of prodi)
@api_view(['GET'])
def detail_prodi(request, detail_prodi):
    url = f'https://api-frontend.kemdikbud.go.id/detail_prodi/{detail_prodi}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail prodi (undifined. detail of prodi using id of prodi)
@api_view(['GET'])
def detail_prodi_undifined(request, detail_prodi_undifined):
    url = f'https://api-frontend.kemdikbud.go.id/detail_prodi/{detail_prodi_undifined}/undifined'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail pt
@api_view(['GET'])
def detail_pt(request, detail_pt):
    url = f'https://api-frontend.kemdikbud.go.id/detail_pt/{detail_pt}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# stat pt
@api_view(['GET'])
def stat_pt(request, stat_pt):
    url = f'https://api-frontend.kemdikbud.go.id/stat_pt/{stat_pt}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# =============== v2 - more simple ==============
# v2/detail_pt
@api_view(['GET'])
def detail_pt_v2(request, detail_pt_v2):
    url = f'https://api-frontend.kemdikbud.go.id/v2/detail_pt/{detail_pt_v2}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# v2/detail_pt_prodi
@api_view(['GET'])
def detail_pt_prodi_v2(request, detail_pt_prodi_v2):
    url = f'https://api-frontend.kemdikbud.go.id/v2/detail_pt_prodi/{detail_pt_prodi_v2}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)