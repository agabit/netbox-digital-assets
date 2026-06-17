from django.db import models
from netbox.models import NetBoxModel


class Supplier(NetBoxModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contact_name = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    comments = models.TextField(blank=True, verbose_name='Comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('plugins:netbox_digital_assets:supplier', args=[self.pk])


class Contract(NetBoxModel):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=100, unique=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='contracts'
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    comments = models.TextField(blank=True, verbose_name='Comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.number} - {self.name}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('plugins:netbox_digital_assets:contract', args=[self.pk])


class Certificate(NetBoxModel):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    wildcard = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certificates'
    )
    tender = models.ForeignKey(
        'netbox_budget.Tender',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certificates'
    )
    devices = models.ManyToManyField(
        'dcim.Device',
        blank=True,
        related_name='certificates'
    )
    virtual_machines = models.ManyToManyField(
        'virtualization.VirtualMachine',
        blank=True,
        related_name='certificates'
    )
    description = models.TextField(blank=True)
    comments = models.TextField(blank=True, verbose_name='Comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('plugins:netbox_digital_assets:certificate', args=[self.pk])


class License(NetBoxModel):
    name = models.CharField(max_length=200)
    license_key = models.CharField(max_length=500, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    start_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='licenses'
    )
    tender = models.ForeignKey(
        'netbox_budget.Tender',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='licenses'
    )
    devices = models.ManyToManyField(
        'dcim.Device',
        blank=True,
        related_name='licenses'
    )
    virtual_machines = models.ManyToManyField(
        'virtualization.VirtualMachine',
        blank=True,
        related_name='licenses'
    )
    description = models.TextField(blank=True)
    comments = models.TextField(blank=True, verbose_name='Comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('plugins:netbox_digital_assets:license', args=[self.pk])


class Subscription(NetBoxModel):
    name = models.CharField(max_length=200)
    service_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subscriptions'
    )
    description = models.TextField(blank=True)
    comments = models.TextField(blank=True, verbose_name='Comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('plugins:netbox_digital_assets:subscription', args=[self.pk])
