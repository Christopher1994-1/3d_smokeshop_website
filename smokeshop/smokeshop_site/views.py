from django.shortcuts import render

# Create your views here.




# Homepage for the website
def home(request):
    return render(request, 'home.html', {})
    