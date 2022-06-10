from .X17 import BMMinerX17
from miners._types import S17  # noqa - Ignore access to _module


class BMMinerS17(BMMinerX17, S17):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip
