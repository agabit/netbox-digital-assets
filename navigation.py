from netbox.plugins.navigation import PluginMenu, PluginMenuButton, PluginMenuItem

menu = PluginMenu(
    label='Digital Assets',
    groups=(
        ('Procurement', (
            PluginMenuItem(
                link='plugins:netbox_digital_assets:supplier_list',
                link_text='Suppliers',
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_digital_assets:supplier_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_digital_assets:contract_list',
                link_text='Contracts',
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_digital_assets:contract_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                ),
            ),
        )),
        ('Assets', (
            PluginMenuItem(
                link='plugins:netbox_digital_assets:certificate_list',
                link_text='Certificates',
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_digital_assets:certificate_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_digital_assets:license_list',
                link_text='Licenses',
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_digital_assets:license_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_digital_assets:subscription_list',
                link_text='Subscriptions',
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_digital_assets:subscription_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                ),
            ),
        )),
    ),
    icon_class='mdi mdi-briefcase-outline',
)
