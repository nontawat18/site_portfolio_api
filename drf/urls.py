"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from api import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import StringArrayView

urlpatterns = [
    path('admin/', admin.site.urls),  
    # path('api/profiles/', views.profileListCreate.as_view()),
    # path('api/profiles/<int:pk>', views.profileDetailUpdateDelete.as_view()),   
    path('api/profile/', views.ProfileListCreate.as_view()),
    path('api/profile/<int:pk>', views.ProfileDetailUpdateDelete.as_view()),
    path('api/array/', views.StringArrayView.as_view(), name='string-array'), 
    path('profile-list/', views.profileList, name='todo-list'),
    path('profile-detail/<int:pk>', views.profileDetail, name='profile-detail'),
    path('profile-create/', views.profileCreate, name='profile-create'),
    path('profile-updates/<int:pk>', views.profileUpdate, name='profile-updates'),
    path('profile-delete/<int:pk>', views.profileDelete, name='profile-delete'),  
    path('skills/', views.skillList, name='skill-list'),
    path('skill/', views.skillCreate, name='skill-create'),
    path('skill<int:pk>', views.skillUpdate, name='skill-updates'),
    path('skill/<int:pk>', views.skillDelete, name='skill-delete'),   
    path('educations/', views.educationList, name='education-list'),
    path('education/', views.educationCreate, name='education-create'),
    path('education<int:pk>', views.educationUpdate, name='education-updates'),
    path('education/<int:pk>', views.educationDelete, name='education-delete'),  
    path('experiences/', views.experienceList, name='experience-list'),
    path('experience/', views.experienceCreate, name='experience-create'),
    path('experience<int:pk>', views.experienceUpdate, name='experience-updates'),
    path('experience/<int:pk>', views.experienceDelete, name='experience-delete'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
