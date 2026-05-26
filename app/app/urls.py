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
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import routers, serializers, viewsets
from settlement import views


@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'healthy', 'service': 'aequitas'})


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# API Router configuration
settlement_router = routers.DefaultRouter()
settlement_router.register(r'users', UserViewSet)
settlement_router.register(r'patient', views.PatientViewSet)
settlement_router.register(r'cost_approval', views.CostApprovalViewSet)
settlement_router.register(r'address', views.AddressViewSet)
settlement_router.register(r'legal_guardian', views.LegalGuardianViewSet)
settlement_router.register(r'insurance', views.InsuranceViewSet)
settlement_router.register(r'payment_method', views.PaymentMethodViewSet)
settlement_router.register(r'cost_approval_type', views.CostApprovalTypeViewSet)
settlement_router.register(r'settlement', views.SettlementViewSet)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('api/', include(settlement_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
