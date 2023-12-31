from businessmen.apps import BusinessmenConfig
from rest_framework.routers import DefaultRouter
from businessmen.views import BusinessmanViewSets, ProductViewSets

app_name = BusinessmenConfig.name
router = DefaultRouter()
router.register(r'businessman', BusinessmanViewSets, basename='factory')
router.register(r'product_businessman', ProductViewSets, basename='product')
urlpatterns = [

] + router.urls
