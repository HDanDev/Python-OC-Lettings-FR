from whitenoise.storage import CompressedManifestStaticFilesStorage

class IgnoreMissingFilesStorage(CompressedManifestStaticFilesStorage):
    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            return name
