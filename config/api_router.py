from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.orders.views import DeliveryTypeViewSet, DeliveryViewSet, OrderViewSet
from apps.product.cart_views import add_item, cart_items, del_item
from apps.product.views import (
    CategoryViewSet,
    CollectionViewSet,
    ColorViewSet,
    DiscountViewSet,
    MaterialViewSet,
    ProductViewSet,
)
from apps.reviews.views import ReviewViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('colors', ColorViewSet, basename='colors')
router.register('categories', CategoryViewSet, basename='categories')
router.register('materials', MaterialViewSet, basename='materials')
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('discounts', DiscountViewSet, basename='discounts')
# router.register('carts', CartViewSet, basename='carts')

router.register('delivery_types', DeliveryTypeViewSet, basename='delivery_types')
router.register('delivery', DeliveryViewSet, basename='delivery')
router.register('orders', OrderViewSet, basename='orders')

app_name = 'api'
urlpatterns = [
    path('carts/items/', cart_items, name='items'),
    path('carts/add_item/', add_item, name='add_item'),
    path('carts/del_item/<int:id>/', del_item, name='del_item'),
    path('', include(router.urls)),
]
