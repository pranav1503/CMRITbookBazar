from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$',views.Register,name='signup'),
    url(r'^login/$', views.Login,name='login'),
    url(r'^logout/$', views.Logout,name='logout'),
]
