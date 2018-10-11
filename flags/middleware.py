from __future__ import absolute_import

from flags.settings import get_flags


class FlagConditionsMiddleware(object):
    """
    Simple middleware that adds all available feature flag conditions to the
    request so that flag state can be checked.
    """
    request_attribute = 'flag_conditions'

    def process_request(self, request):
        flags = get_flags()

        setattr(request, self.request_attribute, flags)
