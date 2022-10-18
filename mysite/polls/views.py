from django.http import HttpResponse


def index(request):
    """Initial basic view test"""
    return HttpResponse("Hello, world. You're at the polls index.")
