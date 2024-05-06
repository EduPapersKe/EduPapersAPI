# from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import UserViewset, LoginView, LogoutView

# router = SimpleRouter()
# router.register(r'users', UserViewset)


urlpatterns = [
    path('users/register/', UserViewset.as_view({'post': 'register'}), name='create-user'),
    path('users/<uuid:pk>/', UserViewset.as_view({'get': 'retrieve'}), name='get-user'),
    path('users/<uuid:pk>/update/', UserViewset.as_view({'put': 'update'}), name='update-user'),
    path('users/<uuid:pk>/patch/', UserViewset.as_view({'patch': 'partial_update'}), name='update-user-partially'),
    path('users/<uuid:pk>/delete/', UserViewset.as_view({'delete': 'destroy'}), name='delete-user'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='log-out'),
]

# urlpatterns += router.urls