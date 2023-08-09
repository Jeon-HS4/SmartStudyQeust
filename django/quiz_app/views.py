from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PageContentSerializer
import requests
from bs4 import BeautifulSoup

@api_view(['GET'])
def crawl_api(request):
    url = request.GET.get('url')

    if not url:
        return Response({'error': 'Please provide a valid URL parameter.'}, status=400)

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()

        serializer = PageContentSerializer(data={'url': url, 'content': content})
        serializer.is_valid()
        return Response(serializer.validated_data)

    except requests.exceptions.RequestException as e:
        return Response({'error': 'Error occurred: ' + str(e)}, status=500)
