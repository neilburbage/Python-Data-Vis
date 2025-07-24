from __future__ import annotations

from typing import Optional, Sequence, Union, TYPE_CHECKING

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from seaborn.axisgrid import PairGrid

data = sns.load_dataset("iris")

__all__ = [
    "sns_line",
    "sns_scatter",
    "sns_bar",
    "sns_box",
    "sns_violin",
    "sns_pair",
    "sns_corr",
    "sns_heat",

]

def _get_ax(ax: Optional[Axes] = None) -> Axes:
    if ax is None:
        _, ax = plt.subplots()
    return ax

def sns_line(
        data: pd.DataFrame,
        *,
        x: str,
        y: str,
        ax: Optional[Axes] = None,
        **lineplot_kwargs,
)  -> Axes:
        ax = _get_ax(ax)
        sns.lineplot(data=data, x=x, y=y, ax=ax, **lineplot_kwargs)
        return ax

def sns_scatter(
        data: pd.DataFrame,
        *,
        x: str,
        y: str,
        ax: Optional[Axes] = None,
        **scatter_kwargs,
) -> Axes:
    ax = _get_ax(ax)
    sns.scatterplot(data=data, x=x, y=y, ax=ax, **scatter_kwargs)
    return ax

def sns_bar(
        data: pd.DataFrame,
        *,
        x: str,
        y: str,
        ax: Optional[Axes] = None,
        **bar_kwargs,
) -> Axes:
    ax = _get_ax(ax)
    sns.barplot(data=data, x=x, y=y, ax=ax, **bar_kwargs)
    return ax

def sns_box(
        data: pd.DataFrame,
        *,
        x: str,
        y: str,
        ax: Optional[Axes] = None,
        **box_kwargs,
) -> Axes:
    ax = _get_ax(ax)
    sns.boxplot(data=data, x=x, y=y, ax=ax, **box_kwargs)
    return ax

def sns_violin(
        data: pd.DataFrame,
        *,
        x: str,
        y: str,
        ax: Optional[Axes] = None,
        **violin_kwargs,
) -> Axes:
    ax = _get_ax(ax)
    sns.violinplot(data=data, x=x, y=y, ax=ax, **violin_kwargs)
    return ax

def sns_heat(
        data: Union[np.ndarray, pd.DataFrame],
        *,
        ax: Optional[Axes] = None,
        cmap: str = "icefire",
        cbar: bool = True,
        **heatmap_kwargs,
) -> Axes:
    if isinstance(data, np.ndarray):
        heat_data = data
    else:
        heat_data = data.values

    ax = _get_ax(ax)
    sns.heatmap(heat_data, cmap=cmap, cbar=cbar, ax=ax, **heatmap_kwargs)
    return ax

def sns_corr(
        data: pd.DataFrame,
        *,
        method: str = "pearson",
        ax: Optional[Axes] = None,
        cmap: str = "coolwarm", center=0,
        annot: bool = False,
        mask_upper: bool = True,
        **heatmap_kwargs,
) -> Axes:
    corr = data.corr(method=method)
    mask = np.triu(np.ones_like(corr, dtype=bool)) if mask_upper else None

    ax = _get_ax(ax)
    sns.heatmap(corr, mask=mask, cmap=cmap, annot=annot, ax=ax, **heatmap_kwargs)
    return ax

def sns_pair(
        data: pd.DataFrame,
        *,
        hue: Optional[str] = None,
        diag_kind: str = "hist",
        corner: bool = False,
        plot_kws: Optional[dict] = None,
        **pairplot_kwargs,
) -> "PairGrid":
    grid = sns.pairplot(
        data=data,
        hue=hue,
        diag_kind=diag_kind,
        corner=corner,
        plot_kws=plot_kws or {},
        **pairplot_kwargs,
    )
    return grid
