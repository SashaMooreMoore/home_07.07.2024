from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PageStatic.as_view(), name="urlPageStatic"),
    re_path(r'help/?$', views.PageHelp.as_view(), name="urlPageHelp"),
    re_path(r'contacts/?$', views.PageContacts.as_view(), name="urlPageContacts"),
    re_path(r'cats/?$', views.PageCat.as_view(), name="urlPageCat"),
]
