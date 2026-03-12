from django.urls import path
from core.views import testing_view, testing_detail_view, health_check, TransactionListView, TransactionDetailView, BudgetListView, BudgetDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    # Lab 1 endpoints
    path('testing/', testing_view, name='testing'),
    path('testing/<int:id>/', testing_detail_view, name='testing-detail'),
    path('health/', health_check, name='health'),
    
    # Lab 2 CRUD endpoints
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    
    # Budget endpoints
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/<int:id>/', BudgetDetailView.as_view(), name='budget-detail'),
    
    # Category endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
]