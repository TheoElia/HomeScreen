from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^ratings/(?P<name>[^/]+)/$",views.ratings, name="ratings"),
    ]