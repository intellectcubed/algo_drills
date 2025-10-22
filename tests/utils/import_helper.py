import os
import importlib

def get_active_implementation():
    """Return the root package (practice_shells or implementations)."""
    active = os.getenv("ALGO_IMPL", "practice_shells")
    if "ALGO_IMPL" not in os.environ:
        print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")
    return active


def import_class(module_path: str, class_name: str):
    """
    Dynamically import a class from the active implementation.

    Example:
        ds = import_class("union_find.disjoint_set", "DisjointSet")
    """
    active = get_active_implementation()
    module = importlib.import_module(f"{active}.{module_path}")
    return getattr(module, class_name)

