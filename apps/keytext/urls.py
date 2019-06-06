from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.keytext.views import TextFilterKey

router = DefaultRouter()
# router.register(r'', TextkeyViewSet, base_name='all_tasks')
urlpatterns = router.urls

urlpatterns += [
    # path('', TextkeyViewSet.as_view({'get': 'list'}), name='text_list'),
    path('list_text/', TextFilterKey.as_view(), name='text_list'),
]