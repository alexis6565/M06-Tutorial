#importing django path function and all views from the blog application 
from django.urls import path 
from . import views 

# view is a place where we put "logic"of our application 
# views are placed in the views.py file in the blog folder 
#assigning a view called post list to the root URL
#URL pattern will match an empty string and the Django URL resolver will ignore the domain name that prefixes the full URL path 
#name post_list is url name that will ID the view and can be the same or different name from the view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
]

#post/<int:pk>/ specifies a URL pattern – we will explain it for you:
#post/ means that the URL should begin with the word post followed by a /. So far so good.
#<int:pk> – this part is trickier. It means that Django expects an integer value and will transfer it to a view as a variable called pk.
#/ – then we need a / again before finishing the URL.