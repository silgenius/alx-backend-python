#!/usr/bin/env python3

"""
Annotated a function parameter and return values
with the appropriate types
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    func to annotate
    """
    if lst:
        return lst[0]
    else:
        return None
