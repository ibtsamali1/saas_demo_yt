from django.http import HttpResponse
from django.shortcuts import render
from visits.models import *

def home_page_view(request ):
    return HttpResponse("<h1>hello nigga</h1>")

def base_page(request):
    return render(request, 'base.html')

# def home_page(request):
#     query_Set=page_visits.objects.all()
#     html_template='home.html'
#     path_total=page_visits.objects.filter(path=request.path)
#     my_context={
#         "quary_set":query_Set,
#         # "page_vists_count":query_Set.count(),
#         "path_counter": path_total.count(),   
#     }
    
    # # path= request.path
    # page_visits.objects.create(path=request.path)
    # return render(request, html_template,my_context)

