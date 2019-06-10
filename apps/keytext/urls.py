from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.keytext.views import TextFilterKey, TextAll, AddNewText, DeleteText, UpdateText

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path('list_text/', TextFilterKey.as_view(), name='text_list'),
    path('list_text_all/', TextAll.as_view(), name='text_all_list'),
    path('add_new_text/', AddNewText.as_view(), name='text_add_new'),
    path('deleted_text/<int:pk>/', DeleteText.as_view(), name='text_deleted'),
    path('update_text/', UpdateText.as_view(), name='text_update'),

]