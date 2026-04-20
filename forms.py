from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField, SlugField
from .models import Supplier, Contract, Certificate, License, Subscription
from netbox_budget.models import Tender
from dcim.models import Device
from virtualization.models import VirtualMachine


class SupplierForm(NetBoxModelForm):
    slug = SlugField()
    comments = CommentField()

    class Meta:
        model = Supplier
        fields = [
            'name', 'slug', 'contact_name', 'contact_email',
            'contact_phone', 'website', 'description', 'tags',
        ]


class SupplierFilterForm(NetBoxModelFilterSetForm):
    model = Supplier
    tag = DynamicModelMultipleChoiceField(
        queryset=Supplier.objects.none(),
        required=False
    )


class ContractForm(NetBoxModelForm):
    supplier = DynamicModelChoiceField(queryset=Supplier.objects.all())
    comments = CommentField()

    class Meta:
        model = Contract
        fields = [
            'name', 'number', 'supplier', 'start_date',
            'end_date', 'description', 'tags',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ContractFilterForm(NetBoxModelFilterSetForm):
    model = Contract
    supplier = DynamicModelChoiceField(
        queryset=Supplier.objects.all(),
        required=False
    )


class CertificateForm(NetBoxModelForm):
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )
    tender = DynamicModelChoiceField(
        queryset=Tender.objects.all(),
        required=False
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = Certificate
        fields = [
            'name', 'domain', 'wildcard', 'start_date', 'expiry_date',
            'contract', 'tender', 'devices', 'virtual_machines', 'description', 'tags',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CertificateFilterForm(NetBoxModelFilterSetForm):
    model = Certificate
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )
    wildcard = forms.NullBooleanSelect()


class LicenseForm(NetBoxModelForm):
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )
    tender = DynamicModelChoiceField(
        queryset=Tender.objects.all(),
        required=False
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = License
        fields = [
            'name', 'license_key', 'quantity', 'start_date', 'expiry_date',
            'contract', 'tender', 'devices', 'virtual_machines', 'description', 'tags',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }


class LicenseFilterForm(NetBoxModelFilterSetForm):
    model = License
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )


class SubscriptionForm(NetBoxModelForm):
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = Subscription
        fields = [
            'name', 'service_name', 'start_date', 'expiry_date',
            'contract', 'description', 'tags',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SubscriptionFilterForm(NetBoxModelFilterSetForm):
    model = Subscription
    contract = DynamicModelChoiceField(
        queryset=Contract.objects.all(),
        required=False
    )
