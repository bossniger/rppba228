from django.urls import include
from django.urls import path
from .views import ProductView, SingleProductView
from .docs import urlpatterns as docs_urlpatterns
from .users import urlpatterns as user_url

app_name = 'api'
urlpatterns = [
    path('docs/', include(docs_urlpatterns)),
    path('users/', include(user_url)),
    path('', ProductView.as_view()),
    path('<int:pk>', SingleProductView.as_view()),
]
