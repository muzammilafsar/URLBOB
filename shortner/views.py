from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Urlform
from .models import *
import string,random
# Create your views here.
def home(request):
    if request.method=='POST':

        form=Urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            key=get_short_code()
        data=Urls()
        data.httpurl=url
        data.short_id=key
        data.save()
        key='http://localhost:8000/'+key
        return render(request, 'base.html', { 'url': url,'key':key})
    else:
        form=Urlform()
        return render(request,'base.html',{'form':form,})

def redirect_original(request, slug):
    url = get_object_or_404(Urls, pk=slug) # get object, if not        found return 404 error
    url.count += 1
    url.save()
    print(slug)
    return HttpResponseRedirect(url.httpurl)

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id