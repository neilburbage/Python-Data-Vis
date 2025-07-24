# src/__init__.py

"""
High level helpers for the Python-Data-Vis project.
Usage:
    from src import demo_line, demo_scatter
"""

from .plot01_line import line_plot             # re-export
from .plot02_scatter import scatter_plot       # re-export
from .plot03_bar import bar_plot               # re-export
from .plot04_hist import hist_plot             # re-export
from .plot05_pie import pie_plot               # re-export
from .plot06_box import box_plot               # re-export
from .plot07_heat import heat_plot             # re-export


__all__ = [
    "line_plot",
    "scatter_plot",
    "bar_plot",
    "hist_plot",
    "pie_plot",
    "box_plot",
    "heat_plot",
]