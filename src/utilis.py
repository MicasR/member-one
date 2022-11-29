def is_positive_int(number: int) -> bool:
    """returns true if number is a positive int."""
    if not type(number) == int: return False
    if number < 0: return False
    return True


def paginateable(items_per_page: int, page: int) -> bool:
    """If object instance can paginate return true."""
    if not is_positive_int(items_per_page): return False
    if not is_positive_int(page): return False
    if page == 0: return False
    return True
