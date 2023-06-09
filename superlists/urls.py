"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lists import views

"""
    Map: url-->function
    eg. Visiting "http://...lists/the_only-list-in-the-world/" will call views.view_list(request),
        which fetches list items from database and puts them into list.html and displays it
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    #   path: '/'

    path(r'', views.home_page, name='home'),
    path('lists/the_only-list-in-the-world/', views.view_list, name='view_list'),
    path('lists/new', views.new_list, name='new_list'),
]
