""" Signals generated by staff app. """
import logging

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from shared.utils import visitor_ip_address
from two_factor.signals import user_verified


logger = logging.getLogger(__name__)


@receiver(user_verified)
def staff_2fa_login(request, user, device, **kwargs):
    # TODO(mhogains): Use device.name="backup" to email or text users phone when used
    log_msg = '{} logged in using device: {}'.format(user, device)
    if device.name == 'backup':
        msg = '#User2FALoginBackup: {}'.format(log_msg)
    else:
        msg = '#User2FALogin: {}'.format(log_msg)
    logger.debug(msg)


@receiver(user_login_failed)
def staff_login_failed(credentials, request, **kwargs):
    logger.debug('#UserLoginFailed: {} did not authenticate password for ip: {}.'.format(credentials, request))

