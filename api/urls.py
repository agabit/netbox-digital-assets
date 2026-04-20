from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register('suppliers', views.SupplierViewSet)
router.register('contracts', views.ContractViewSet)
router.register('certificates', views.CertificateViewSet)
router.register('licenses', views.LicenseViewSet)
router.register('subscriptions', views.SubscriptionViewSet)

urlpatterns = router.urls
