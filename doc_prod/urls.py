from django.contrib import admin
from django.urls import path, include
import registry.urls as doc_prod_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(doc_prod_urls)),
]
