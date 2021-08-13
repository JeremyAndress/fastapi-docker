import math
from core.config import settings


class Page(object):

    def __init__(self, items, page, page_size, total):
        self.data = items
        self.previous_page = None
        self.next_page = None
        self.previous_page = page - 1 if page > 1 else None
        previous_items = (page - 1) * page_size
        has_next = previous_items + len(items) < total
        self.next_page = page + 1 if has_next else None
        self.total = total
        self.pages = int(math.ceil(total / float(page_size)))


def paginate(query, page, page_size=settings.PAGE_SIZE):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    total = query.order_by(None).count()
    return Page(items, page, page_size, total)
