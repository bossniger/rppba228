from django.urls import include
from django.urls import path
from .docs import urlpatterns as docs_urlpatterns
from .users import urlpatterns as user_url

app_name = 'api'
urlpatterns = [
    path('docs/', include(docs_urlpatterns)),
    path('users/', include(user_url)),
]
