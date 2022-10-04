from os import link
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Url
# Create your views here.
def home(request):
    if request.method == "POST" :
        fullurl = request.POST.get('fullurl')
        obj=Url.create(fullurl)
        return render(request , "index.html" ,
                      {'fullurl' : obj.fullurl ,
                      'shorturl': request.get_host() + '/' + obj.shorturl }
                      )
    
    
    
    return render(request , "index.html")




def route_to_url (request , key):
    try:
        obj = Url.objects.get(shorturl=key)
        return redirect(obj.fullurl)
    
    except:
        obj = None
        return redirect(home)
    return redirect(request , "index.html" )