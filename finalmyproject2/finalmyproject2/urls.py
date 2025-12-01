from django.contrib import admin
from django.urls import path
from myapp.views import home   # 🔹 bunu əlavə et

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),   # 🔹 əsas səhifə
]