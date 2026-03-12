from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Testing, Transaction, Budget, Category
from core.serializers import TestingSerializer, TransactionSerializer, BudgetSerializer, CategorySerializer  



def testing_view(request):
    data = Testing.objects.all()
    serializer = TestingSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def health_check(request):
    return JsonResponse({'status': 'ok'})

def testing_detail_view(request, id):
    try:
        testing_record = Testing.objects.get(id=id)
        serializer = TestingSerializer(testing_record)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        return JsonResponse(
            {'error': 'Record not found'}, 
            status=404
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --- New CRUD views ---

class TransactionListView(APIView):
    """
    GET  /api/transactions/     -> List all transactions
    POST /api/transactions/     -> Create a new transaction
    """

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailView(APIView):
    """
    GET    /api/transactions/<id>/  -> Retrieve a single transaction
    PUT    /api/transactions/<id>/  -> Update a transaction
    DELETE /api/transactions/<id>/  -> Delete a transaction
    """

    def get_object(self, id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BudgetListView(APIView):
    """
    GET  /api/budgets/     -> List all budgets
    POST /api/budgets/     -> Create a new budget
    """

    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(user=request.user)
            else:
                from django.contrib.auth import get_user_model
                User = get_user_model()
                default_user = User.objects.first()
                serializer.save(user=default_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetailView(APIView):
    """
    GET    /api/budgets/<id>/  -> Retrieve a single budget
    PUT    /api/budgets/<id>/  -> Update a budget
    DELETE /api/budgets/<id>/  -> Delete a budget
    """

    def get_object(self, id):
        try:
            return Budget.objects.get(id=id)
        except Budget.DoesNotExist:
            return None

    def get(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response(
                {"error": "Budget not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response(
                {"error": "Budget not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response(
                {"error": "Budget not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    