from chain.apps import ChainConfig
from rest_framework.routers import DefaultRouter
from chain.views import FactoryViewSets, ProductViewSets

app_name = ChainConfig.name
router = DefaultRouter()
router.register(r'factory', FactoryViewSets, basename='factory')
router.register(r'product_factory', ProductViewSets, basename='product')
urlpatterns = [

] + router.urls
