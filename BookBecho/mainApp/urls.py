from django.conf.urls import url
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainApp'

urlpatterns = [
    url(r'^$', views.Home.as_view(),name="home"),
    url(r'^sellBook/$', views.SellBook.as_view(),name="sellBook"),
    url(r'^sellBook/edit/(?P<pk>\d+)/$', views.EditSellBook.as_view(),name="sellBookEdit"),
    url(r'^sellBook/delete/(?P<pk>\d+)/$', views.DeleteSellBook.as_view(),name="sellBookDelete"),
    url(r'^cart/$', views.Cart.as_view(),name="cart"),
    url(r'^addToCart/(?P<pk>\d+)/$', views.AddToCart.as_view(),name="addToCart"),
    url(r'^removeFromCart/(?P<pk>\d+)/$', views.RemoveFromCart.as_view(),name="removeFromCart"),
    url(r'^search/results/$', views.Search.as_view(),name="search"),
    url(r'^emptyCart/$', views.emptyCart,name="emptyCart"),
    url(r'^checkout/$', views.checkOut,name="checkOut"),
    url(r'^orders/$', views.ConfirmOrders.as_view(),name="confirmCheckOut"),
    url(r'^orders/$',views.Orders.as_view(),name="orders"),
    url(r'^orders/finished_ordering/(?P<pk>\d+)/$',views.FinishedReceiving.as_view(),name="finishedOrders"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
