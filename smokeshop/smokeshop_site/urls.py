from django.urls import path
from . import views

# Path Converters
# int: Integers
# str: Strings
# path: whole urls /
# slug: hyphen-and_underscores_stuff
# UUID: universally unique identifier


urlpatterns = [
    
    # Path for the home page
    path('', views.home, name='home'),
    
    # Path for the test page
    path('test/', views.test, name='test'),
    
    # Path for the update time 
    path('get_remaining_time/', views.get_remaining_time, name='get_remaining_time'),

]
