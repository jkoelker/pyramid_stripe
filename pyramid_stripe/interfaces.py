from zope import interface


class IStripe(interface.Interface):
    request = interface.Attribute('The request object')


class ICharge(IStripe):
    pass


class IChargeSucceeded(ICharge):
    pass


class IChargeFailed(ICharge):
    pass


class IChargeRefunded(ICharge):
    pass


class IChargeDisputed(ICharge):
    pass


class IChargeFailed(ICharge):
    pass


class ICustomer(IStripe):
    pass


class ICustomerCreated(ICustomer):
    pass


class ICustomerUpdated(ICustomer):
    pass


class ICustomerDeleted(ICustomer):
    pass


class ICustomerSubscription(ICustomer):
    pass


class ICustomerSubscriptionCreated(ICustomerSubscription):
    pass


class ICustomerSubscriptionUpdated(ICustomerSubscription):
    pass


class ICustomerSubscriptionDeleted(ICustomerSubscription):
    pass


class ICustomerSubscriptionTrialWillEnd(ICustomerSubscription):
    pass


class ICustomerDiscount(ICustomer):
    pass


class ICustomerDiscountCreated(ICustomerDiscount):
    pass


class ICustomerDiscountUpdated(ICustomerDiscount):
    pass


class ICustomerDiscountDeleted(ICustomerDiscount):
    pass


class IInvoice(IStripe):
    pass


class IInvoiceCreated(IInvoice):
    pass


class IInvoiceUpdated(IInvoice):
    pass


class IInvoicePayment(IInvoice):
    pass


class IInvoicePaymentSucceeded(IInvoicePayment):
    pass


class IInvoicePaymentFailed(IInvoicePayment):
    pass


# TODO(jkoelker) Figure out if this should really be a subclass of IInvoice
class IInvoiceItem(IStripe):
    pass


class IInvoiceItemCreated(IInvoiceItem):
    pass


class IInvoiceItemUpdated(IInvoiceItem):
    pass


class IInvoiceItemDeleted(IInvoiceItem):
    pass


class IPlan(IStripe):
    pass


class IPlanCreated(IPlan):
    pass


class IPlanUpdated(IPlan):
    pass


class IPlanDeleted(IPlan):
    pass


class ICoupon(IStripe):
    pass


class ICouponCreated(ICoupon):
    pass


class ICouponUpdated(ICoupon):
    pass


class ICouponDeleted(ICoupon):
    pass


class ITransfer(IStripe):
    pass


class ITransferCreated(ITransfer):
    pass


class ITransferFailed(ITransfer):
    pass


class IPing(IStripe):
    pass
