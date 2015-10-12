from zope import interface


class IStripe(interface.Interface):
    request = interface.Attribute('The request object')


class IAccount(IStripe):
    pass


class IAccountUpdated(IAccount):
    pass


class IExternalAccount(IAccount):
    pass


class IExternalAccountCreated(IExternalAccount):
    pass


class IExternalAccountDeleted(IExternalAccount):
    pass


class IExternalAccountUpdated(IExternalAccount):
    pass


class IBalanceAvailable(IStripe):
    pass


class IBitcoin(IStripe):
    pass


class IBitcoinReceiverCreated(IBitcoin):
    pass


class IBitcoinReceiverFilled(IBitcoin):
    pass


class IBitcoinReceiverUpdated(IBitcoin):
    pass


class IBitcoinReceiverTransactionCreated(IBitcoin):
    pass


class ICharge(IStripe):
    pass


class IChargeCaptured(ICharge):
    pass


class IChargeFailed(ICharge):
    pass


class IChargeRefunded(ICharge):
    pass


class IChargeUpdated(ICharge):
    pass


class IChargeSucceeded(ICharge):
    pass


class IChargeDispute(ICharge):
    pass


class IChargeDisputeClosed(IChargeDispute):
    pass


class IChargeDisputeCreated(IChargeDispute):
    pass


class IChargeDisputeFundsReinstated(IChargeDispute):
    pass


class IChargeDisputeFundsWithdrawn(IChargeDispute):
    pass


class IChargeDisputeUpdated(IChargeDispute):
    pass


class ICoupon(IStripe):
    pass


class ICouponCreated(ICoupon):
    pass


class ICouponDeleted(ICoupon):
    pass


class ICouponUpdated(ICoupon):
    pass


class ICustomer(IStripe):
    pass


class ICustomerCreated(ICustomer):
    pass


class ICustomerDeleted(ICustomer):
    pass


class ICustomerUpdated(ICustomer):
    pass


class ICustomerBankAccountDeleted(ICustomer):
    pass


class ICustomerDiscount(ICustomer):
    pass


class ICustomerDiscountCreated(ICustomerDiscount):
    pass


class ICustomerDiscountDeleted(ICustomerDiscount):
    pass


class ICustomerDiscountUpdated(ICustomerDiscount):
    pass


class ICustomerSource(ICustomer):
    pass


class ICustomerSourceCreated(ICustomerSource):
    pass


class ICustomerSourceDeleted(ICustomerSource):
    pass


class ICustomerSourceUpdated(ICustomerSource):
    pass


class ICustomerSubscription(ICustomer):
    pass


class ICustomerSubscriptionCreated(ICustomerSubscription):
    pass


class ICustomerSubscriptionDeleted(ICustomerSubscription):
    pass


class ICustomerSubscriptionTrialWillEnd(ICustomerSubscription):
    pass


class ICustomerSubscriptionUpdated(ICustomerSubscription):
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


class IInvoicePaymentFailed(IInvoice):
    pass


class IInvoicePaymentSucceeded(IInvoice):
    pass


class IInvoiceUpdated(IInvoice):
    pass


class IInvoiceItem(IStripe):
    pass


class IInvoiceItemCreated(IInvoiceItem):
    pass


class IInvoiceItemDeleted(IInvoiceItem):
    pass


class IInvoiceItemUpdated(IInvoiceItem):
    pass


class IOrder(IStripe):
    pass


class IOrderCreated(IOrder):
    pass


class IOrderPaymentFailed(IOrder):
    pass


class IOrderPaymentSucceeded(IOrder):
    pass


class IOrderUpdated(IOrder):
    pass


class IPlan(IStripe):
    pass


class IPlanCreated(IPlan):
    pass


class IPlanDeleted(IPlan):
    pass


class IPlanUpdated(IPlan):
    pass


class IProduct(IStripe):
    pass


class IProductCreated(IProduct):
    pass


class IProductUpdated(IProduct):
    pass


class IRecipient(IStripe):
    pass


class IRecipientCreated(IRecipient):
    pass


class IRecipientDeleted(IRecipient):
    pass


class IRecipientUpdated(IRecipient):
    pass


class ISku(IStripe):
    pass


class ISkuCreated(ISku):
    pass


class ISkuUpdated(ISku):
    pass


class ITransfer(IStripe):
    pass


class ITransferCreated(ITransfer):
    pass


class ITransferFailed(ITransfer):
    pass


class ITransferPaid(ITransfer):
    pass


class ITransferReversed(ITransfer):
    pass


class ITransferUpdated(ITransfer):
    pass


class IPing(IStripe):
    pass
