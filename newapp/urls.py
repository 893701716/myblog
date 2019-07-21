from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'newapp'
urlpatterns=[
    path('', views.index, name='index'),
    path('blogPage/', views.blogPage, name='blogPage'),
    path('registered/', views.registered, name='registered'),
    path('login/', views.login, name='login'),
    path('registry/', views.registry, name='registry'),
    path('pannelpage/', views.pannelpage, name='pannelpage'),
    path('writepage/', views.writepage, name='writepage'),
    path('savemessage/', views.savemessage, name='savemessage'),
    path('personalpage/', views.personalpage, name='personalpage'),
    # path('purchasing/',views.purchasing,name='purchasing'),
    # path('purchased/',views.purchased,name='purchased'),
    # path('page_list/',views.page_split,name='page_list')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)