# NetBox Digital Assets Plugin

A NetBox plugin for managing digital assets including suppliers, contracts, certificates, licenses, and subscriptions.

## Features

- **Suppliers** — vendor/provider catalog with contact information
- **Contracts** — linked to suppliers, with contract numbers and dates
- **Certificates** — SSL/wildcard certificates, linked to contracts, devices and VMs
- **Licenses** — software licenses with quantity tracking, linked to contracts, devices and VMs
- **Subscriptions** — service subscriptions linked to contracts
- **Global search** — all objects searchable via NetBox global search
- **REST API** — full API support for all models
- **Changelog** — change history for every object
- **Device integration** — licenses and certificates visible on Device/VM detail pages
- **Tender integration** — direct links to procurement tenders (requires netbox_budget plugin)

## Compatibility

| Plugin Version | NetBox Version |
|---------------|----------------|
| 0.1           | 4.5.x          |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/agabit/netbox-digital-assets.git
cd netbox-digital-assets
pip install -e .
```

### 2. Add to NetBox configuration

In `netbox/netbox/configuration.py`:

```python
PLUGINS = [
    'netbox_digital_assets',
]

PLUGINS_CONFIG = {
    'netbox_digital_assets': {},
}
```

### 3. Run migrations

```bash
python manage.py migrate netbox_digital_assets
```

### 4. Restart NetBox

```bash
sudo systemctl restart netbox
```

## Models

### Supplier
- Name, slug, contact name, email, phone, website, description

### Contract
- Name, number, supplier (FK), start/end dates, description

### Certificate
- Name, domain, wildcard flag, start/expiry dates, contract (FK), tender (FK), devices (M2M), VMs (M2M)

### License
- Name, license key, quantity, start/expiry dates, contract (FK), tender (FK), devices (M2M), VMs (M2M)

### Subscription
- Name, service name, start/expiry dates, contract (FK)

## Related Plugins

- [netbox-budget](https://github.com/agabit/netbox-budget) — Budget planning and tender tracking

## Author

Aidarbek Gabit ([@agabit](https://github.com/agabit))

## Credits

This plugin was developed with the assistance of [Claude AI](https://claude.ai) by Anthropic.
The plugin architecture, models, views, forms, templates and all code were generated through
an interactive conversation with Claude AI, following the official NetBox plugin development
documentation and tutorial.

## License

Apache 2.0
