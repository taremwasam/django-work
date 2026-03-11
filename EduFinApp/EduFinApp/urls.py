from django.contrib import admin
from django.urls import path, include
from core.views import testing_view, testing_detail_view  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('testing', testing_view, name='testing'),
    path('testing/<int:id>', testing_detail_view, name='testing-detail'),
]