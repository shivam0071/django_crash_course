from django.shortcuts import render
from django.http import HttpResponse # use this to test the connections
# Create your views here.
def homepage(request):
    return render(request, 'le_static_app/index.html', context = {'demo':'Malboro: A great Day'})
