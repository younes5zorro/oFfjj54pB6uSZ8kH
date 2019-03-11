from django.conf.urls import url

from api.views import ConnectionCreateView, ConnectionDetailView

urlpatterns = [
    url(r'^connections/$', ConnectionCreateView.as_view(), name='connections'),
    url(r'^connections/(?P<pk>[0-9]+)$', ConnectionDetailView.as_view(), name='detail'),
]