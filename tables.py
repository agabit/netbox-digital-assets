import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Supplier, Contract, Certificate, License, Subscription


class SupplierTable(NetBoxTable):
    name = tables.LinkColumn(attrs={"a": {"target": "_blank"}})
    contact_name = tables.Column()
    contact_email = tables.Column()
    website = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Supplier
        fields = (
            'pk', 'id', 'name', 'slug', 'contact_name',
            'contact_email', 'contact_phone', 'website', 'description',
        )
        default_columns = ('name', 'contact_name', 'contact_email', 'website')


class ContractTable(NetBoxTable):
    name = tables.LinkColumn(attrs={"a": {"target": "_blank"}})
    supplier = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Contract
        fields = (
            'pk', 'id', 'name', 'number', 'supplier',
            'start_date', 'end_date', 'description',
        )
        default_columns = ('name', 'number', 'supplier', 'start_date', 'end_date')


class CertificateTable(NetBoxTable):
    name = tables.LinkColumn(attrs={"a": {"target": "_blank"}})
    contract = tables.Column(linkify=True)
    wildcard = tables.BooleanColumn()

    class Meta(NetBoxTable.Meta):
        model = Certificate
        fields = (
            'pk', 'id', 'name', 'domain', 'wildcard',
            'start_date', 'expiry_date', 'contract', 'description',
        )
        default_columns = ('name', 'domain', 'wildcard', 'expiry_date', 'contract')


class LicenseTable(NetBoxTable):
    name = tables.LinkColumn(attrs={"a": {"target": "_blank"}})
    contract = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = License
        fields = (
            'pk', 'id', 'name', 'license_key', 'quantity',
            'start_date', 'expiry_date', 'contract', 'description',
        )
        default_columns = ('name', 'quantity', 'expiry_date', 'contract')


class SubscriptionTable(NetBoxTable):
    name = tables.LinkColumn(attrs={"a": {"target": "_blank"}})
    contract = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Subscription
        fields = (
            'pk', 'id', 'name', 'service_name',
            'start_date', 'expiry_date', 'contract', 'description',
        )
        default_columns = ('name', 'service_name', 'expiry_date', 'contract')
