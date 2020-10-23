from django.urls import path
from product.views.category_view import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView
from product.views.inventory_view import CreateInventoryView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('create-inventory/', CreateInventoryView.as_view(), name='inventory_create'),
]
