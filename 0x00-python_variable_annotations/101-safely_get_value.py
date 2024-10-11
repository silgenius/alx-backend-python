#!/usr/bin/env python3

"""
Annotated a function parameter and return values
with the appropriate types
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T', covariant=False)


def safely_get_value(
        dct: Mapping,
        key: Any, default:
        Union[T, None] = None
        ) -> Union[Any, T]:
    """
    func to annotate
    """
    if key in dct:
        return dct[key]
    else:
        return default
