from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.keytext.views import TextFilterKey

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path('list_text/', TextFilterKey.as_view(), name='text_list'),
]