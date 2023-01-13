from django.shortcuts import render
from .forms import SubListForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, timedelta
from django.http import JsonResponse


# Create all the functions

# Edit code below to change ad offer time. hour=(how many hours the offer is vaild for)
end_time = datetime.now() + timedelta(hours=24)

def get_remaining_time(request):
    time_left = end_time - datetime.now()
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_left_str = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    return JsonResponse({'time_left': time_left_str})








# Create your views here.

# Homepage for the website
def home(request):
    # Checking to see if user has entered their email
    submitted = False
    if request.method == "POST":
        form = SubListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your email was saved successully')
            return HttpResponseRedirect("/home?submitted=True")
    else:
        form = SubListForm()
        if 'submitted' in request.GET:
            submitted = True
    form = SubListForm  
    
    
    return render(request, 'home.html', {
        'form':form,
    })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Test page for the website
def test(request):
        # Checking to see if user has entered their email
    submitted = False
    if request.method == "POST":
        form = SubListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your email was saved successully')
            return HttpResponseRedirect("/home?submitted=True")
    else:
        form = SubListForm()
        if 'submitted' in request.GET:
            submitted = True
    form = SubListForm  
    
    
    return render(request, 'test.html', {
        "form":form,
    })
    