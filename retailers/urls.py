from retailers.apps import RetailersConfig
from rest_framework.routers import DefaultRouter
from retailers.views import RetailerViewSets, ProductViewSets

app_name = RetailersConfig.name
router = DefaultRouter()
router.register(r'product_retailer', ProductViewSets, basename='product')
router.register(r'retailer', RetailerViewSets, basename='retailer')
urlpatterns = [

] + router.urls
