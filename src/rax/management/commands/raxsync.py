from optparse import make_option
from os import rmdir, symlink, unlink
from os.path import basename, join
from tempfile import mkdtemp

from django.conf import settings
from django.core.management.base import BaseCommand

from rax.mixin import RaxMixin


class Command(RaxMixin, BaseCommand):

    help = "Synchronize your static files with Rackspace Cloud Files."
    option_list = BaseCommand.option_list + (
        make_option(
            '--media',
            action='store_true',
            dest='media',
            default=False,
            help="Synchronize media files instead."),
        make_option(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help="Synchronize media AND static files."))

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        if not options['media']:
            tmp_dir = mkdtemp()
            symlink(
                self.static_root, join(tmp_dir, basename(self.static_root)))
            self.connection.sync_folder_to_container(tmp_dir, self.container)
            unlink(join(tmp_dir, basename(self.static_root)))
            rmdir(tmp_dir)
        if options['media'] or options['all']:
            media_dir = getattr(settings, 'MEDIA_ROOT')
            self.connection.sync_folder_to_container(
                media_dir, self.container)
