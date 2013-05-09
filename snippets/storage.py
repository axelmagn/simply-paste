from storages.backends.s3boto import S3BotoStorage
from require.storage import OptimizedFilesMixin
from django.contrib.staticfiles.storage import CachedFilesMixin

# S3 storage with r.js optimization.
class OptimizedS3BotoStorage(OptimizedFilesMixin, S3BotoStorage):
    pass

# S3 storage with r.js optimization and MD5 fingerprinting.
class OptimizedCachedS3BotoStorage(OptimizedFilesMixin, CachedFilesMixin,
                                   S3BotoStorage):
    pass
