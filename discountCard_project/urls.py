from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('discountCard/', include('discountCard.urls')),
    path('admin/', admin.site.urls),
]