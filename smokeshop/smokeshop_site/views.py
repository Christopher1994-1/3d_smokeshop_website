from django.shortcuts import render
from .forms import SubListForm
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    