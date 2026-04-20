from netbox.views import generic
from . import models, tables, forms


# Supplier views
class SupplierListView(generic.ObjectListView):
    queryset = models.Supplier.objects.all()
    table = tables.SupplierTable
    filterset_form = forms.SupplierFilterForm


class SupplierView(generic.ObjectView):
    queryset = models.Supplier.objects.all()


class SupplierEditView(generic.ObjectEditView):
    queryset = models.Supplier.objects.all()
    form = forms.SupplierForm


class SupplierDeleteView(generic.ObjectDeleteView):
    queryset = models.Supplier.objects.all()


# Contract views
class ContractListView(generic.ObjectListView):
    queryset = models.Contract.objects.prefetch_related('supplier')
    table = tables.ContractTable
    filterset_form = forms.ContractFilterForm


class ContractView(generic.ObjectView):
    queryset = models.Contract.objects.prefetch_related('supplier')


class ContractEditView(generic.ObjectEditView):
    queryset = models.Contract.objects.all()
    form = forms.ContractForm


class ContractDeleteView(generic.ObjectDeleteView):
    queryset = models.Contract.objects.all()


# Certificate views
class CertificateListView(generic.ObjectListView):
    queryset = models.Certificate.objects.prefetch_related('contract')
    table = tables.CertificateTable
    filterset_form = forms.CertificateFilterForm


class CertificateView(generic.ObjectView):
    queryset = models.Certificate.objects.prefetch_related('contract', 'devices', 'virtual_machines')


class CertificateEditView(generic.ObjectEditView):
    queryset = models.Certificate.objects.all()
    form = forms.CertificateForm


class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = models.Certificate.objects.all()


# License views
class LicenseListView(generic.ObjectListView):
    queryset = models.License.objects.prefetch_related('contract')
    table = tables.LicenseTable
    filterset_form = forms.LicenseFilterForm


class LicenseView(generic.ObjectView):
    queryset = models.License.objects.prefetch_related('contract', 'devices', 'virtual_machines')


class LicenseEditView(generic.ObjectEditView):
    queryset = models.License.objects.all()
    form = forms.LicenseForm


class LicenseDeleteView(generic.ObjectDeleteView):
    queryset = models.License.objects.all()


# Subscription views
class SubscriptionListView(generic.ObjectListView):
    queryset = models.Subscription.objects.prefetch_related('contract')
    table = tables.SubscriptionTable
    filterset_form = forms.SubscriptionFilterForm


class SubscriptionView(generic.ObjectView):
    queryset = models.Subscription.objects.prefetch_related('contract')


class SubscriptionEditView(generic.ObjectEditView):
    queryset = models.Subscription.objects.all()
    form = forms.SubscriptionForm


class SubscriptionDeleteView(generic.ObjectDeleteView):
    queryset = models.Subscription.objects.all()
