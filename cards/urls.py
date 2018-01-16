from rest_framework import routers

from cards.views import CardViewSet


router = routers.SimpleRouter()
router.register(r'cards', CardViewSet)

urlpatterns = router.urls
