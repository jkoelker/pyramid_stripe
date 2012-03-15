import logging

from pyramid import view
from pyramid import httpexceptions

from pyramid_stripe import events


log = logging.getLogger(__name__)


@view.view_config(route_name="stripe",
                  request_method="POST",
                  renderer="string")
def stripe_webhook(request):
    event = request.stripe_raw
    _events = [events.Stripe(request)]

    # TODO(jkoelker) DRY this up
    # NOTE(jkoelker) This ordering is important
    if event["type"].startswith("charge."):
        _events.append(events.Charge(request))

        if "succeeded" in event["type"]:
            _events.append(events.ChargeSucceeded(request))

        elif "failed" in event["type"]:
            _events.append(events.ChargeFailed(request))

        elif "refunded" in event["type"]:
            _events.append(events.ChargeRefunded(request))

        elif "disputed" in event["type"]:
            _events.append(events.ChargeDisputed(request))

    elif event["type"].startswith("customer."):
        _events.append(events.Customer(request))

        if "subscription" in event["type"]:
            _events.append(events.CustomerSubscription(request))

            if "created" in event["type"]:
                _events.append(events.CustomerSubscriptionCreated(request))

            elif "updated" in event["type"]:
                _events.append(events.CustomerSubscriptionUpdated(request))

            elif "deleted" in event["type"]:
                _events.append(events.CustomerSubscriptionDeleted(request))

            elif "trial_will_end" in event["type"]:
                e = events.CustomerSubscriptionTrialWillEnd(request)
                _events.append(e)

        elif "discount" in event["type"]:
            _events.append(events.CustomerDiscount(request))

            if "created" in event["type"]:
                _events.append(events.CustomerDiscountCreated(request))

            elif "updated" in event["type"]:
                _events.append(events.CustomerDiscountUpdated(request))

            elif "deleted" in event["type"]:
                _events.append(events.CustomerDiscountDeleted(request))

        else:
            if "created" in event["type"]:
                _events.append(events.CustomerCreated(request))

            elif "updated" in event["type"]:
                _events.append(events.CustomerUpdated(request))

            elif "deleted" in event["type"]:
                _events.append(events.CustomerDeleted(request))

    elif event["type"].startswith("invoice."):
        _events.append(events.Invoice(request))

        if "created" in event["type"]:
            _events.append(events.InvoiceCreated(request))

        elif "updated" in event["type"]:
            _events.append(events.InvoiceUpdated(request))

        elif "payment_succeeded" in event["type"]:
            _events.append(events.InvoicePaymentSucceeded(request))

        elif "payment_failed" in event["type"]:
            _events.append(events.InvoicePaymentFailed(request))

    elif event["type"].startswith("invoiceitem."):
        _events.append(events.InvoiceItem(request))

        if "created" in event["type"]:
            _events.append(events.InvoiceItemCreated(request))

        elif "updated" in event["type"]:
            _events.append(events.InvoiceItemUpdated(request))

        elif "deleted" in event["type"]:
            _events.append(events.InvoiceItemDeleted(request))

    elif event["type"].startswith("plan."):
        _events.append(events.Plan(request))

        if "created" in event["type"]:
            _events.append(events.PlanCreated(request))

        elif "updated" in event["type"]:
            _events.append(events.PlanUpdated(request))

        elif "deleted" in event["type"]:
            _events.append(events.PlanDeleted(request))

    elif event["type"].startswith("coupon."):
        _events.append(events.Coupon(request))

        if "created" in event["type"]:
            _events.append(events.CouponCreated(request))

        elif "updated" in event["type"]:
            _events.append(events.CouponUpdated(request))

        elif "deleted" in event["type"]:
            _events.append(events.CouponDeleted(request))

    elif event["type"].startswith("transfer."):
        _events.append(events.Transfer(request))

        if "created" in event["type"]:
            _events.append(events.TransferCreated(request))

        elif "failed" in event["type"]:
            _events.append(events.TransferFailed(request))

    elif event["type"] == "ping":
        _events.append(events.Ping(request))

    else:
        # NOTE(jkoelker) If this is reached, we don't know about this event
        #                raise a 500 so stripe knows we did not get this
        #                webhook
        raise httpexceptions.HTTPInternalServerError("Unknown event type")

    request.registry.notify(*_events)

    return ''
