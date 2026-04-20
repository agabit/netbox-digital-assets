from netbox.api.serializers import NetBoxModelSerializer
from ..models import Supplier, Contract, Certificate, License, Subscription


class SupplierSerializer(NetBoxModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id', 'url', 'display', 'name', 'slug', 'contact_name',
            'contact_email', 'contact_phone', 'website', 'description',
        ]


class ContractSerializer(NetBoxModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id', 'url', 'display', 'name', 'number', 'supplier',
            'start_date', 'end_date', 'description',
        ]


class CertificateSerializer(NetBoxModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'id', 'url', 'display', 'name', 'domain', 'wildcard',
            'start_date', 'expiry_date', 'contract', 'devices',
            'virtual_machines', 'description',
        ]


class LicenseSerializer(NetBoxModelSerializer):
    class Meta:
        model = License
        fields = [
            'id', 'url', 'display', 'name', 'license_key', 'quantity',
            'start_date', 'expiry_date', 'contract', 'devices',
            'virtual_machines', 'description',
        ]


class SubscriptionSerializer(NetBoxModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id', 'url', 'display', 'name', 'service_name',
            'start_date', 'expiry_date', 'contract', 'description',
        ]
