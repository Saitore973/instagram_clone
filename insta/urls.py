from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('photos/',views.photos,name = 'photos'),
    path('search/', views.search_profile, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)