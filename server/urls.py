"""
server URL Configuration
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
# from rest_auth import urls as auth_views
from rest_auth.views import PasswordResetConfirmView



from funder.views import FunderSignup, FunderList, FunderProfile, FunderProfileUpdate
from sme.views import SMESignup, SMEList, SMEProfile, SMEProfileUpdate

router = DefaultRouter()
router.register('smes', SMEList)
router.register('funders', FunderList)

#url patterns with media configurations


urlpatterns = [
    path(r'', include_docs_urls(title='SME_Funders API', public=False)),
    # path('smes_login/', SMELogin.as_view(), name="smes_login"),
    # path('funders_login/', FunderLogin.as_view(), name="funders_login"),
    path('admin/', admin.site.urls),
    path('smes/', SMEList.as_view(), name="sme_list"),
    path('sme_signup/', SMESignup.as_view(), name="sme_signup"),
    path('smes/<str:pk>/', SMEProfile.as_view(), name="sme_profile"),
    path('smes/<str:pk>/update/',SMEProfileUpdate.as_view(), name="sme_profile_update"),
    path('funders/', FunderList.as_view(), name="funders_list"),
    path('funder_signup/', FunderSignup.as_view(), name="funder_signup"),
    path('funders/<int:pk>/', FunderProfile.as_view(), name="funders_profile"),
    path('funders/<int:pk>/update/', FunderProfileUpdate.as_view(), name="funders_profile_update"),
    url(r'^account/', include('rest_auth.urls')),
    re_path(r'^account/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    # url(r'^account/registration/', include('rest_auth.registration.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
