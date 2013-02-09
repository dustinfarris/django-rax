from os.path import abspath

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import pyrax


class RaxMixin(object):

    def __init__(self, *args, **kwargs):
        rax_settings = getattr(settings, 'RAX')
        if rax_settings is None:
            raise ImproperlyConfigured("You have not defined RAX settings.")

        self.static_root = abspath(getattr(settings, 'STATIC_ROOT'))
        self.username = rax_settings.get('USERNAME')
        self.api_key = rax_settings.get('API_KEY')
        self.cloudfiles_container = rax_settings.get('CONTAINER')
        self.region = rax_settings.get('REGION', 'ORD')
        self.verify_checksum = rax_settings.get('VERIFY_CHECKSUM', True)
        super(RaxMixin, self).__init__(*args, **kwargs)

    @property
    def connection(self):
        if not hasattr(self, '_connection'):
            pyrax.set_credentials(self.username, self.api_key)
            # For some reason pyrax.encoding doesn't get set by default.
            pyrax.encoding = "utf-8"
            self._connection = pyrax.connect_to_cloudfiles(
                region=self.region)
        return self._connection

    @property
    def container(self):
        if not hasattr(self, '_container'):
            self._container = self.connection.get_container(
                self.cloudfiles_container)
        return self._container

    @property
    def remote_object_names(self):
        if not hasattr(self, '_remote_object_names'):
            self._remote_object_names = self.container.get_object_names()
        return self._remote_object_names
