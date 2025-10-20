from __future__ import annotations
from typing import (
    List,
    Union,
    Tuple,
    Any,
    Callable,
    FrozenSet,
    Iterable
)

Boolean = bool
Integer = int
IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IntegerTuple]
IntegerSet = FrozenSet[Integer]
Grid = Tuple[Tuple[Integer], ...]
Cell = Tuple[Integer, IntegerTuple]
Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IntegerTuple]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
Element = Union[Object, Grid]
Piece = Union[Grid, Patch]
TupleTuple = Tuple[Tuple[Any, ...], ...]
ContainerContainer = Union[Tuple[Tuple[Any, ...], ...], FrozenSet[FrozenSet[Any]]]
# Generic container type for functions that accept various container types
Container = Union[Tuple[Any, ...], FrozenSet[Any], Iterable[Any]]
