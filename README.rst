pyramid_stripe - Stripe helpers for pyramid
===========================================

pyramid_stipe provides tools to make integrating stripe payments into a
pyramid app easier.


Getting Started
---------------

In your application's configuration stanza (where you create a Pyramid
"Configurator"), use the ``config.include`` method::

   config.include("pyramid_stripe")

Configuration
-------------

The settings registry should have the key ``stripe.api_key`` set to your
stripe 'Secret Key'. You can add this to the Paste ``.ini`` file. For
exampe::

    [app:myproject]
    strip.api_key = 0000000000000000000000000000000

Current Features
----------------

Webhooks
~~~~~~~~

A webhook url will be created for converting webhooks to pyramid events. By
default this lives at ``/stripe``. If you wish to relocate this you can
specify a prefix to ``config.include``. For example, to place the webhook
url at ``/other/stripe`` do::

   config.include("pyramid_stripe", "/other")

Events will then be sent to subscribers.

Events
++++++

The following events are avialible in the ``pyramid_stripe.events`` module

- Stripe
- Charge
- ChargeSucceeded
- ChargeFailed
- ChargeRefunded
- ChargeDisputed
- ChargeFailed
- Customer
- CustomerCreated
- CustomerUpdated
- CustomerDeleted
- CustomerSubscription
- CustomerSubscriptionCreated
- CustomerSubscriptionUpdated
- CustomerSubscriptionDeleted
- CustomerSubscriptionTrialWillEnd
- CustomerDiscount
- CustomerDiscountCreated
- CustomerDiscountUpdated
- CustomerDiscountDeleted
- Invoice
- InvoiceCreated
- InvoiceUpdated
- InvoicePayment
- InvoicePaymentSucceeded
- InvoicePaymentFailed
- InvoiceItem
- InvoiceItemCreated
- InvoiceItemUpdated
- InvoiceItemDeleted
- Plan
- PlanCreated
- PlanUpdated
- PlanDeleted
- Coupon
- CouponCreated
- CouponUpdated
- CouponDeleted
- Transfer
- TransferCreated
- TransferFailed
- Ping

Events are considered heirarchial and all events below the event type are
notified. For example, when the webhook is called with a
``customer.subscription.created`` event. The ``Stripe``, ``Customer``,
``CustomerSubcription``, and ``CustomerSubcriptionCreated`` event
subscribers will all be notified. The exception is ``invoiceitem`` (``InvoiceItem``) which is *not* a child of ``invoice`` (``Invoice``).

To handle all events, it is only necessary to subscribe to the ``Stripe``
event. Likewise, to handle all ``Customer`` events, it is only necessary to
subscribe to the ``Customer`` event.  For example::

    from pyramid.events import subscriber
    from pyramid_stripe import events

    @subscriber(events.CustomerDiscount)
    def handle_discounts(event):
        stripe = event.request.stripe

        ... do stuff with the stripe event...


The stripe ``request`` property holds the ``stripe`` object. The
``stripe_raw`` property contains the unserialized json document from the
``POST``.
