from collections import UserDict

class ShortUrlsStorage(UserDict):
    def __init__(self):
        super().__init__()
        self.hash_length = 2

    def to_key(self, url):
        url_hash = hash(url)
        short_hash = url_hash & self.hash_length
        key = f'{short_hash:x}'
        self[key] = url
        return key

    def to_long(self, key):
        pass


shorts = ShortUrlsStorage()