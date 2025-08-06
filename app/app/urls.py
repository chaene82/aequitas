"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from settlement import views
from frontend_views import home_view, login_view, create_legal_guardian_view, create_patient_view

# Frontend URLs
frontend_urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('create-legal-guardian/', create_legal_guardian_view, name='create_legal_guardian'),
    path('create-patient/', create_patient_view, name='create_patient'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
] + frontend_urlpatterns

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
settlement_router = routers.DefaultRouter()
settlement_router.register(r'users', UserViewSet)
settlement_router.register(r'patient', views.PatientViewSet)
settlement_router.register(r'cost_approval', views.CostApprovalViewSet)
settlement_router.register(r'address', views.AddressViewSet)
settlement_router.register(r'legal_gardiant', views.LegalGuardiantViewSet)
settlement_router.register(r'insurance', views.InsuranceViewSet)
settlement_router.register(r'payment_methode', views.PaymentMethodeViewSet)
settlement_router.register(r'cost_approval_tpye', views.CostApprovalTypeViewSet)
settlement_router.register(r'settlement', views.SettelmentViewSet)
