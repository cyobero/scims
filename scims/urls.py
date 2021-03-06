"""scims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from scims.views import home
from user_auth.views import user_login, user_logout, user_signup
from products.views import inventory_view,  add_product_view, product_view, ProductConfigDataTableView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/', user_signup, name='user_signup'),
    path('inventory/', ProductConfigDataTableView.as_view(), name='inventory'),
    path('inventory/add_product', add_product_view, name='add_product'),
    path('product/<slug:slug>', product_view, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
