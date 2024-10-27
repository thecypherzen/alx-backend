#!/usr/bin/env python3
"""Contains definition of stellar function"""
from typing import Optional, Mapping, Tuple


def index_range(*args: Optional[Tuple[int]],
                **kwargs: Optional[Mapping[str, int]]) -> Tuple:
    """A function that takes two integer arguments

    Params:
    page():
    page_size()

    Returns:
        A tuple of size=2 containing a `start index` and an `end index`
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.

        Note:
           Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    if len(args) == 2:
        page, page_size = args
    elif len(kwargs) == 2:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')
    else:
        return ()
    end = page * page_size
    return (end - page_size, end)
