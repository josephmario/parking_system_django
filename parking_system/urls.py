"""
URL configuration for parking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from parking_app.views import parking_lot, enter_car, exit_car, verify_payment, insufficient, entry_vehicle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking_lot/', parking_lot, name='parking_lot'),
    path('enter/<int:spot_id>/', enter_car, name='enter_car'),
    path('exit/<int:spot_id>/', exit_car, name='exit_car'),
    path('verify_payment/<int:spot_id>/', verify_payment, name='verify_payment'),
    path('insufficient/', insufficient, name='insufficient'),
    path('entry_vehicle/<int:spot_id>/', entry_vehicle, name='entry_vehicle'),
]
