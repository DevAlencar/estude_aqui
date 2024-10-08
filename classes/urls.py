from rest_framework import routers

from classes.models import Mentoring
from classes.views import CategoryViewSet, ReviewViewSet, MentoringViewSet

router = routers.SimpleRouter()
router.register(r'classes/category', CategoryViewSet)
router.register(r'classes/mentoring', MentoringViewSet)
router.register(r'classes/review', ReviewViewSet)
urlpatterns = router.urls
