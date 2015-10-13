import logging

import stripe


log = logging.getLogger(__name__)


def _get_event(request):
    content_type = request.headers.get("content-type", '')
    is_json = "application/json" in content_type
    is_post = request.method == "POST"

    if not is_json and not is_post:
        return

    try:
        return request.json_body
    except AttributeError:
        log.exception("Error loading json data")


def add_stripe_event_raw(request):
    event_data = _get_event(request)
    log.debug("Raw Stripe event: %s" % event_data)
    return event_data


def add_stripe_event(request):
    event_data = _get_event(request)

    if not event_data:
        return

    log.debug("Stripe event: %s" % event_data)

    return stripe.convert_to_stripe_object(event_data, stripe.api_key, None)
