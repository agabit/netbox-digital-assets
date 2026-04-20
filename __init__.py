from netbox.plugins import PluginConfig


class DigitalAssetsConfig(PluginConfig):
    name = 'netbox_digital_assets'
    verbose_name = 'Digital Assets'
    description = 'Manage suppliers, contracts, certificates, licenses and subscriptions'
    version = '0.1'
    author = 'Gabit Aidarbek'
    author_email = 'gabit.aidarbek@gmail.com'
    base_url = 'digital-assets'
    search_extensions = 'search'

config = DigitalAssetsConfig
