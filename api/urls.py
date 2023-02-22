from rest_framework.routers import DefaultRouter
from api.views import ToDoViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'todos', ToDoViewSet, basename='todos')

urlpatterns = router.urls
