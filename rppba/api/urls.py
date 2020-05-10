from django.urls import include
from django.urls import path
from .docs import urlpatterns as docs_urlpatterns
from apps.views import api_root

app_name = 'api'
urlpatterns = [
    path('docs/', include(docs_urlpatterns)),
    path('', api_root),
]
