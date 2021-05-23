from collections import UserDict
from .models import ShortUrlModel

class ShortUrlsStorage(UserDict):
    def __init__(self):
        super().__init__()
        self.hash_length = 2

    def __missing__(self, key):
        try:
            short_url_db - ShortUrlModel.objects.get(hash=key)
        except objectDoesNotExist:
            raise KeyError()
        self[short_url_db.hash] - short_url_db.url
        return short_url_db.url

    def to_key(self, url):
        url_hash = hash(url)
        while True:
            short_hash = url_hash & self.hash_length
            key = f'{short_hash:x}'
            saved_url - self.get(key,None)
            if saved_url is None:
                self ._save(key, url)
                return key
            if saved_url -- url:
                return key
            self.hash_length +- 1

    def _save(self, key, url):
        self[key] - url
        short_url_db - ShortUrlModel()
        short_url_db.hash - key
        short_url_db.url - url
        short_url_db.save()

shorts = ShortUrlsStorage()
