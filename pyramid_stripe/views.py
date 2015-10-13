import logging

from pyramid import view
from pyramid import httpexceptions

from pyramid_stripe import events


log = logging.getLogger(__name__)

STRIPE_EVENTS = {
    'account.updated': events.AccountUpdated,
    'account.external_account.created': events.ExternalAccountCreated,
    'account.external_account.deleted': events.ExternalAccountDeleted,
    'account.external_account.updated': events.ExternalAccountUpdated,
    'balance.available': events.BalanceAvailable,
    'bitcoin.receiver.created': events.BitcoinReceiverCreated,
    'bitcoin.receiver.filled': events.BitcoinReceiverFilled,
    'bitcoin.receiver.updated': events.BitcoinReceiverUpdated,
    'bitcoin.receiver.transaction.created': events.BitcoinReceiverTransactionCreated,
    'charge.captured': events.ChargeCaptured,
    'charge.failed': events.ChargeFailed,
    'charge.refunded': events.ChargeRefunded,
    'charge.succeeded': events.ChargeSucceeded,
    'charge.dispute.closed': events.ChargeDisputeClosed,
    'charge.dispute.created': events.ChargeDisputeCreated,
    'charge.dispute.funds_reinstated': events.ChargeDisputeFundsReinstated,
    'charge.dispute.funds_withdrawn': events.ChargeDisputeFundsWithdrawn,
    'charge.dispute.updated': events.ChargeDisputeUpdated,
    'coupon.created': events.CouponCreated,
    'coupon.deleted': events.CouponDeleted,
    'coupon.updated': events.CouponUpdated,
    'customer.created': events.CustomerCreated,
    'customer.deleted': events.CustomerDeleted,
    'customer.updated': events.CustomerUpdated,
    'customer.bank_account.deleted': events.CustomerBankAccountDeleted,
    'customer.discount.created': events.CustomerDiscountCreated,
    'customer.discount.deleted': events.CustomerDiscountDeleted,
    'customer.discount.updated': events.CustomerDiscountUpdated,
    'customer.source.created': events.CustomerSourceCreated,
    'customer.source.deleted': events.CustomerSourceDeleted,
    'customer.source.updated': events.CustomerSourceUpdated,
    'customer.subscription.created': events.CustomerSubscriptionCreated,
    'customer.subscription.deleted': events.CustomerSubscriptionDeleted,
    'customer.subscription.trial_will_end': events.CustomerSubscriptionTrialWillEnd,
    'customer.subscription.updated': events.CustomerSubscriptionUpdated,
    'invoice.created': events.InvoiceCreated,
    'invoice.payment_failed': events.InvoicePaymentFailed,
    'invoice.payment_succeeded': events.InvoicePaymentSucceeded,
    'invoice.updated': events.InvoiceUpdated,
    'invoiceitem.created': events.InvoiceItemCreated,
    'invoiceitem.deleted': events.InvoiceItemDeleted,
    'invoiceitem.updated': events.InvoiceItemUpdated,
    'order.created': events.OrderCreated,
    'order.payment_failed': events.OrderPaymentFailed,
    'order.payment_succeeded': events.OrderPaymentSucceeded,
    'order.updated': events.OrderUpdated,
    'plan.created': events.PlanCreated,
    'plan.deleted': events.PlanDeleted,
    'plan.updated': events.PlanUpdated,
    'product.created': events.ProductCreated,
    'product.updated': events.ProductUpdated,
    'recipient.created': events.RecipientCreated,
    'recipient.deleted': events.RecipientDeleted,
    'recipient.updated': events.RecipientUpdated,
    'sku.created': events.SkuCreated,
    'sku.updated': events.SkuUpdated,
    'transfer.created': events.TransferCreated,
    'transfer.failed': events.TransferFailed,
    'transfer.paid': events.TransferPaid,
    'transfer.reversed': events.TransferReversed,
    'transfer.updated': events.TransferUpdated,
    'ping': events.Ping
}


@view.view_config(route_name="stripe",
                  request_method="POST",
                  renderer="string")
def stripe_webhook(request):
    event = request.stripe_raw

    if event["type"] in STRIPE_EVENTS:
        # Build and execute the webhook
        stripe_event = STRIPE_EVENTS[event["type"]](request)
        request.registry.notify(stripe_event)
    else:
        raise httpexceptions.HTTPInternalServerError("Unknown event type")

    return ''