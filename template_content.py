from netbox.plugins.templates import PluginTemplateExtension


class DeviceBudgetPanel(PluginTemplateExtension):
    models = ['dcim.device']

    def right_page(self):
        device = self.context['object']
        budget_plans = device.budget_plans.prefetch_related('tenders').all()
        return self.render(
            'netbox_digital_assets/inc/device_budget.html',
            extra_context={
                'budget_plans': budget_plans,
            }
        )


class VirtualMachinePanel(PluginTemplateExtension):
    models = ['virtualization.virtualmachine']

    def right_page(self):
        vm = self.context['object']
        licenses = vm.licenses.prefetch_related('contract', 'tender').all()
        certificates = vm.certificates.prefetch_related('contract', 'tender').all()
        return self.render(
            'netbox_digital_assets/inc/vm_assets.html',
            extra_context={
                'licenses': licenses,
                'certificates': certificates,
            }
        )


template_extensions = [DeviceBudgetPanel, VirtualMachinePanel]
