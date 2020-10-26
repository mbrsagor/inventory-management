from django.urls import path
from base.views.dashboard_view import Dashboard
from base.views.auth_view import UserLoginView, LogoutView
from base.views.category_view import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView
from base.views.inventory_view import CreateInventoryView, InventoryListView, InventoryDetailView, \
    InventoryUpdateView, InventoryDeleteView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('create-inventory/', CreateInventoryView.as_view(), name='inventory_create'),
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory-update/<pk>/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory-delete/<pk>/', InventoryDeleteView.as_view(), name='inventory_delete'),
]
