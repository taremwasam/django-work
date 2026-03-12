from django.contrib import admin
from core.models import Testing, Transaction, Budget, Category  

admin.site.register(Testing)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Category)