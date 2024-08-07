from typing import Any


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value
    
    def __getattr__(self, key: str):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)