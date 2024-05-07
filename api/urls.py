from django.urls import path
# from rest_framework.routers import SimpleRouter

from .views import ResourceView

# router = SimpleRouter


urlpatterns = [
    path('resources/', ResourceView.as_view({'get': 'get'}), name='get all resources'),
    path('resources/<uuid:pk>/', ResourceView.as_view({'get': 'retrieve'}), name='get resource by id'),
    path('resources/create/', ResourceView.as_view({'post': 'post'}), name='create resource'),
    path('resources/<uuid:pk>/update/', ResourceView.as_view({'put': 'update'}), name='update resource'),
    path('resources/<uuid:pk>/delete/', ResourceView.as_view({'delete': 'destroy'}), name='delete resource'),
]

# urlpatterns += router.urls