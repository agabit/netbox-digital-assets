from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Supplier, Contract, Certificate, License, Subscription
from .serializers import (
    SupplierSerializer, ContractSerializer, CertificateSerializer,
    LicenseSerializer, SubscriptionSerializer
)


class SupplierViewSet(NetBoxModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ContractViewSet(NetBoxModelViewSet):
    queryset = Contract.objects.prefetch_related('supplier')
    serializer_class = ContractSerializer


class CertificateViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.prefetch_related('contract', 'devices', 'virtual_machines')
    serializer_class = CertificateSerializer


class LicenseViewSet(NetBoxModelViewSet):
    queryset = License.objects.prefetch_related('contract', 'devices', 'virtual_machines')
    serializer_class = LicenseSerializer


class SubscriptionViewSet(NetBoxModelViewSet):
    queryset = Subscription.objects.prefetch_related('contract')
    serializer_class = SubscriptionSerializer
