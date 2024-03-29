from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path('', views.post_list, name='post'),
    path('', views.header_list, name='header'),
    path('', views.slider_list, name='slider'),
    path('', views.thebigthree_list, name='thebigthree'),
    path('', views.leaders_list, name='leaders'),
    path('', views.leadersstaff_list, name='leadersstaff'),
    path('', views.secondslider_list, name='secondslider'),
    path('', views.hire_list, name='hire'),
    path('', views.hirestaff_list, name='hirestaff'),
    path('', views.thelastthree_list, name='thelastthree'),
    path('', views.footer_list, name='footer'),
    path('', views.rent_list, name='rent'),
    path('', views.contacts_list, name='contacts'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)