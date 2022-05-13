from enum import Enum


class VisitorRequestStatus(Enum):
    SUCCESS = 1
    NEED_PREPARE = 2
    PRODUCT_MISSING = 3
