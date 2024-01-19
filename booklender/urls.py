
from rest_framework.routers import DefaultRouter

from booklender.views import UserViewSet, BookViewSet, LenderRecordViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'books', BookViewSet, basename='book')
router.register(r'lender-records', LenderRecordViewSet,
                basename='lender-record')

urlpatterns = router.urls
