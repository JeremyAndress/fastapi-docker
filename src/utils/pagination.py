import math

class Page(object):

    def __init__(self, items, page, page_size, total):
        self.data = items
        self.previous_page = None
        self.next_page = None
        # self.has_previous = page > 1
        # if self.has_previous:
        #     self.previous_page = page - 1
        self.previous_page = page - 1 if page > 1 else None
        previous_items = (page - 1) * page_size
        # self.has_next = previous_items + len(items) < total
        # if self.has_next:
        #     self.next_page = page + 1
        has_next = previous_items + len(items) < total
        self.next_page = page + 1 if has_next else None
        self.total = total
        self.pages = int(math.ceil(total / float(page_size)))


def paginate(query, page, page_size):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    # We remove the ordering of the query since it doesn't matter for getting a count and
    # might have performance implications as discussed on this Flask-SqlAlchemy issue
    # https://github.com/mitsuhiko/flask-sqlalchemy/issues/100
    total = query.order_by(None).count()
    return Page(items, page, page_size, total)


# def paginate(query, page, per_page=20, error_out=True):
#     if error_out and page < 1:
#         abort(404)
#     items = query.limit(per_page).offset((page - 1) * per_page).all()
#     if not items and page != 1 and error_out:
#         abort(404)

#     # No need to count if we're on the first page and there are fewer
#     # items than we expected.
#     if page == 1 and len(items) < per_page:
#         total = len(items)
#     else:
#         total = query.order_by(None).count()

#     return Pagination(query, page, per_page, total, items)