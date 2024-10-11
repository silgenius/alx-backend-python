#!/usr/bin/env python3

"""
Annotated a function parameter and return values
with the appropriate types
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    func to annotate
    """
    return [(i, len(i)) for i in lst]
