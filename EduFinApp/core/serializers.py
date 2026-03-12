from rest_framework import serializers
from core.models import Testing, Transaction, Budget, Category




class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'


class TestingNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = ['id', 'name']       



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'title', 'amount', 'transaction_type', 'category', 'date', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_amount(self, value):
        """Ensure the amount is a positive number."""
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate_title(self, value):
        """Ensure the title is not empty or just whitespace."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value        
    def validate(self, data):
        """
        Cross-field validation: if transaction_type is 'income', category must not be empty.
        """
        transaction_type = data.get('transaction_type')
        category = data.get('category')
        
        if transaction_type == 'income' and not category:
            raise serializers.ValidationError({
                'category': 'Category is required for income transactions.'
            })
        
        return data

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'limit_amount', 'month', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']    





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        existing = Category.objects.filter(name__iexact=value)
        if existing.exists():
            if self.instance and self.instance.id == existing.first().id:
                return value
            raise serializers.ValidationError("A category with this name already exists.")
        return value        