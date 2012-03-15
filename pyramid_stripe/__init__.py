from pyramid import config

from pyramid_stripe import request


def add_routes(config):
    config.add_route('stripe', '/stripe')


def includeme(config):
    """Set up standard configurator registrations.  Use via:

    .. code-block:: python

       config = Configurator()
       config.include('pyramid_stripe')

    """
    config.set_request_property(request.add_stripe_event, "stripe",
                                reify=True)
    config.set_request_property(request.add_stripe_event_raw, "stripe_raw",
                                reify=True)
    config.include(add_routes)
    config.scan("pyramid_stripe.views")


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    c = config.Configurator(settings=settings)
    includeme(c)
    return c.make_wsgi_app()
