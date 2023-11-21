# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# # @api_view(['GET'])
# # def test_data(request):
# #     person = {'name':'Ridwan Halim', 'age':20}
# #     return Response(person)
# # https://api-frontend.kemdikbud.go.id/hit_mhs/ridwan%20halim%20uty

# @api_view(['GET'])
# def error_404(request):
#     msg = {'message': '404 Not Found'}
#     return Response(msg,status=status.HTTP_404_NOT_FOUND)

# api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests  # Import the requests module

@api_view(['GET'])
def error_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

# ============= mahasiswa ==================

@api_view(['GET'])
def hit_mhs_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def hit_mhs(request, hit_mhs):  # Added the hit_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/hit_mhs/{hit_mhs}'

    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

@api_view(['GET'])
def detail_mhs_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def detail_mhs(request, detail_mhs):  # Added the detail_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/detail_mhs/{detail_mhs}'

    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# ============== dosen, prodi, pt ==============

@api_view(['GET'])
def hit_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def hit(request, hit):  # Added the hit_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/hit/{hit}'

    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail dosen
@api_view(['GET'])
def detail_dosen_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def detail_dosen(request, detail_dosen):  # Added the detail_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/detail_dosen/{detail_dosen}'
    # Make a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)


# detail prodi
@api_view(['GET'])
def detail_prodi_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def detail_prodi(request, detail_prodi):  # Added the detail_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/detail_prodi/{detail_prodi}'
    # Make a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)

# detail prodi (undifined)
@api_view(['GET'])
def detail_prodi_undifined_404(request):
    msg = {'message': '404 Not Found'}
    return Response(msg, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def detail_prodi_undifined(request, detail_prodi_undifined):  # Added the detail_mhs parameter
    # Construct the URL with the dynamic parameter
    url = f'https://api-frontend.kemdikbud.go.id/detail_prodi/{detail_prodi_undifined}/undifined'
    # Make a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        # If the request was not successful, return an message response
        msg = {'message': 'Failed to fetch data'}
        return Response(msg, status=response.status_code)