from django.urls import path
from apps.views import UserListView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list_page'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete_user_page'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update_user_page'),
]