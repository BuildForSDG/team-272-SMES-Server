"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from funder.views import FunderList, FunderDetail, FunderUpdate
from sme.views import SMEList, SMEDetail, SMEUpdate

router = DefaultRouter()
router.register('smes', SMEList)
router.register('funders', FunderList)

#url patterns with media configurations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smes/', SMEList.as_view(), name="sme_list"),
    path('smes/<str:pk>/', SMEDetail.as_view(), name="sme_details"),
    path('smes/<str:pk>/update/',SMEUpdate.as_view(), name="sme_update"),
    path('funders/', FunderList.as_view(), name="funders_list"),
    path('funders/<str:pk>/', FunderDetail.as_view(), name="funders_details"),
    path('funders/<str:pk>/update/', FunderUpdate.as_view(), name="funders_update")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
