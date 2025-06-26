from .operation import (
    AddStrategy,
    SubtractStrategy,
    MultiplyStrategy,
    DivideStrategy,
    power,
    root,
    modulus,
    int_divide,
    percent,
    abs_diff,
)

# ---------------------------------------------------------------------------
# Factory helper
# ---------------------------------------------------------------------------

def get_operation(name: str):
    """
    Return a callable that performs the requested operation.

    Parameters
    ----------
    name : str
        The operation keyword as typed in the REPL
        (e.g. "add", "divide", "power", …).

    Returns
    -------
    Callable[[float, float], float]
        Either a Strategy instance (with an .execute method) *or*
        a plain function that takes (a, b) and returns a numeric result.

    Raises
    ------
    ValueError
        If an unknown operation name is supplied.
    """
    operations = {
        # ── strategy instances ───────────────────────────────────────────────
        "add":        AddStrategy(),
        "subtract":   SubtractStrategy(),
        "multiply":   MultiplyStrategy(),
        "divide":     DivideStrategy(),
        # ── helper functions ────────────────────────────────────────────────
        "power":      power,
        "root":       root,
        "modulus":    modulus,
        "int_divide": int_divide,
        "percent":    percent,
        "abs_diff":   abs_diff,
    }

    try:
        return operations[name]
    except KeyError as err:
        raise ValueError(f"Unknown operation: {name!r}") from err