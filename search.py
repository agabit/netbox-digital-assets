from netbox.search import SearchIndex, register_search
from .models import Supplier, Contract, Certificate, License, Subscription


@register_search
class SupplierIndex(SearchIndex):
    model = Supplier
    fields = (
        ('name', 100),
        ('slug', 110),
        ('contact_name', 300),
        ('contact_email', 300),
        ('website', 300),
        ('description', 500),
    )


@register_search
class ContractIndex(SearchIndex):
    model = Contract
    fields = (
        ('name', 100),
        ('number', 100),
        ('description', 500),
    )


@register_search
class CertificateIndex(SearchIndex):
    model = Certificate
    fields = (
        ('name', 100),
        ('domain', 200),
        ('description', 500),
    )


@register_search
class LicenseIndex(SearchIndex):
    model = License
    fields = (
        ('name', 100),
        ('license_key', 200),
        ('description', 500),
    )


@register_search
class SubscriptionIndex(SearchIndex):
    model = Subscription
    fields = (
        ('name', 100),
        ('service_name', 200),
        ('description', 500),
    )
