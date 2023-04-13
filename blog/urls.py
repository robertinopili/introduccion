from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetaiView, BlogUpdateView, BlogDeleteView

app_name='blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetaiView.as_view(), name='detail' ), #intpk hace referencia al id
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")
]