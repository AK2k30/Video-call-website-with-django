from django.conf import Settings, settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('i/',views.i,name="i"),
    path('dash/',views.dash,name="i"),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join_room'),
    path('',views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)