import logging

import stripe


log = logging.getLogger(__name__)


def _get_event(request):
    # TODO(jkoelker) Contact the stripe peeps to see about getting a header
    #                in the webhook request so we could do like
    #                if not request.header.get("x-stripe-webhook"):
    content_type = request.headers.get("content-type", '')
    if ("application/json" not in content_type or
        request.method != "POST"):
        return

    try:
        return request.json_body
    except Exception:
        log.exception("Error loading json data")


def add_stripe_event_raw(request):
    event_data = _get_event(request)
    log.debug("Raw Stripe event: %s" % event_data)
    return event_data


def add_stripe_event(request):
    event_data = _get_event(request)
    if not event_data:
        return

    # NOTE(jkoelker) Events coming from webhooks are not convertable
    #                by default
    event_data[u"object"] = u"event"

    log.debug("Stripe event: %s" % event_data)

    return stripe.convert_to_stripe_object(event_data, stripe.api_key)
