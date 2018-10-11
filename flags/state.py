from __future__ import absolute_import

from flags.middleware import FlagConditionsMiddleware
from flags.settings import get_flags


def flag_state(flag_name, **kwargs):
    """ Return the value for the flag by passing kwargs to its conditions """
    flags = None

    # If the request is given as a kwargs, and the FlagConditionsMiddleware is
    # enabled, use the flag conditions attached to the request.
    if 'request' in kwargs:
        flags = getattr(
            kwargs['request'],
            FlagConditionsMiddleware.request_attribute,
            None
        )

    if flags is None:
        flags = get_flags()

    # This logic should be separated out from check_state so that KeyErrors
    # raised when checking conditions aren't incorrectly caught.
    try:
        flag = flags[flag_name]
    except KeyError:
        return False

    return flag.check_state(**kwargs)


def flag_enabled(flag_name, **kwargs):
    """ Check if a flag is enabled by passing kwargs to its conditions. """
    return flag_state(flag_name, **kwargs)


def flag_disabled(flag_name, **kwargs):
    """ Check if a flag is disabled by passing kwargs to its conditions. """
    return not flag_state(flag_name, **kwargs)
