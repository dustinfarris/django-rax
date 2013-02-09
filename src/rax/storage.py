from django.core.files.storage import FileSystemStorage
import pyrax

from mixin import RaxMixin


class FileSystemStorageMixin(FileSystemStorage):

    def __init__(self, *args, **kwargs):
        super(FileSystemStorageMixin, self).__init__(*args, **kwargs)


class RaxStorage(RaxMixin, FileSystemStorageMixin):

    def __init__(self, *args, **kwargs):
        super(RaxStorage, self).__init__(*args, **kwargs)

    def _save(self, name, content, checksum=None):
        if self.verify_checksum:
            checksum = pyrax.utils.get_checksum(content)
        self.container.upload_file(content, obj_name=name, etag=checksum)
        return super(RaxStorage, self)._save(name, content)

    def exists(self, name):
        return (super(RaxStorage, self).exists(name) and
                name in self.remote_object_names)
