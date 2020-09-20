from django.urls import path
from .views import UrlView,WebsiteUrl

urlpatterns = [
    path('', UrlView.as_view(), name='url-shorner'),
    path('<slug:slug>', WebsiteUrl.as_view(), name='url-website'),
]