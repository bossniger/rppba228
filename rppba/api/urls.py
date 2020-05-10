from django.urls import include
from django.urls import path
from apps.elements.views import ElementListCreateAPIView, ElementUpdateAPIView
from apps.materials_order.views import MaterialOrderCreateAPIView
from apps.orders.views import OrdersRetrieveAPIView, OrdersListAPIView
from apps.warehouse_materials.views import WarehouseMaterialsListAPIView, WarehouseMaterialsRetrieveAPIView
from apps.operations.views import (
    OperationListCreateListApiView,
    OperationListUpdateApiView,
    ProductOperationListCreateListApiView,
    ProductOperationUpdateApiView,
)
from apps.production_order.views import (
    ProductionOrderListCreateAPIView,
    ProductionOrderUpdateAPIView
)
from apps.products.views import (
    ProductListCreateAPIView,
    ProductUpdateAPIView
)
from .docs import urlpatterns as docs_urlpatterns
from apps.views import api_root

app_name = 'api'
urlpatterns = [
    path('docs/', include(docs_urlpatterns)),
    path('', api_root),
    path('elements/', ElementListCreateAPIView.as_view()),
    path('elements/<int:id>', ElementUpdateAPIView.as_view()),
    path('orders/', OrdersListAPIView.as_view()),
    path('orders/<id>/', OrdersRetrieveAPIView.as_view()),
    path('materials_order/', MaterialOrderCreateAPIView.as_view() ),
    path('warehouse_materials/', WarehouseMaterialsListAPIView.as_view()),
    path('warehouse_materials/<id>/', WarehouseMaterialsRetrieveAPIView.as_view()),
    path('operation_list/', OperationListCreateListApiView.as_view()),
    path('operation_list/<id>', OperationListUpdateApiView.as_view()),
    path('product_operation/', ProductOperationListCreateListApiView.as_view()),
    path('product_operation/<id>', ProductOperationUpdateApiView.as_view()),
    path('product', ProductListCreateAPIView.as_view()),
    path('product/<int:id>', ProductUpdateAPIView.as_view()),
    path('production_order', ProductionOrderListCreateAPIView.as_view()),
    path('production_order/<id>', ProductionOrderUpdateAPIView.as_view()),

]
