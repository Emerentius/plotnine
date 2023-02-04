from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from typing import (
        Any,
        Callable,
        Dict,
        Literal,
        Protocol,
        Sequence,
    )

    import numpy as np
    import numpy.typing as npt
    import pandas as pd
    from matplotlib.artist import Artist  # noqa
    from matplotlib.axes import Axes  # noqa
    from matplotlib.figure import Figure  # noqa
    from matplotlib.offsetbox import DrawingArea  # noqa
    from mizani.transforms import trans
    from typing_extensions import TypeAlias

    from plotnine.coords.coord import coord
    from plotnine.facets.facet import facet
    from plotnine.facets.layout import Layout  # noqa
    from plotnine.facets.strips import Strips  # noqa
    from plotnine.geoms.geom import geom
    from plotnine.ggplot import ggplot
    from plotnine.guides.guide import guide
    from plotnine.iapi import strip_label_details
    from plotnine.layer import Layers, layer  # noqa
    from plotnine.mapping.aes import aes
    from plotnine.positions.position import position
    from plotnine.scales.scale import scale, scale_continuous, scale_discrete
    from plotnine.scales.scales import Scales  # noqa
    from plotnine.stats.stat import stat
    from plotnine.themes.theme import theme
    from plotnine.watermark import watermark

    class PlotAddable(Protocol):
        """
        Object that can be added to a ggplot object
        """

        def __radd__(self, other: ggplot) -> ggplot:
            """
            Add to ggplot object
            """
            ...

    class DataFrameConvertible(Protocol):
        """
        Object that can be converted to a DataFrame
        """

        def to_pandas(self) -> pd.DataFrame:
            """
            Convert to pandas dataframe
            """
            ...

    # Input data can be a DataFrame, a DataFrame factory or things that
    # are convertible to DataFrames.
    # `Data` is mostly used internally and `DataLike` is the input type
    # before automatic conversion.
    # Input data can actually also contain DataFrameGroupBy which is
    # specially handled, but pandas doesn't expose that data type in
    # their type stubs and instead treats it the same as a DataFrame
    # (df.groupby() returns a DataFrame in the stubs).
    Data: TypeAlias = pd.DataFrame | Callable[[], pd.DataFrame]
    DataLike: TypeAlias = Data | DataFrameConvertible

    LayerData: TypeAlias = (
        pd.DataFrame | Callable[[pd.DataFrame], pd.DataFrame]
    )
    LayerDataLike: TypeAlias = LayerData | DataFrameConvertible
    ColorLike: TypeAlias = str | Literal['None', 'none']
    ColorsLike: TypeAlias = (
        ColorLike | list[ColorLike] | pd.Series[ColorLike] |
        npt.NDArray[np.str_]
    )

    # Facet strip
    StripLabellingFuncNames: TypeAlias = Literal[
        'label_value',
        'label_both',
        'label_context'
    ]

    # Function that can facet strips
    StripLabellingFunc: TypeAlias = Callable[
        [strip_label_details],
        strip_label_details
    ]

    StripLabellingDict: TypeAlias = (
        Dict[str, str] |
        Dict[str, Callable[[str], str]]
    )

    # Can be coerced to a StripLabellingFunc
    CanBeStripLabellingFunc: TypeAlias = (
        StripLabellingFuncNames |
        StripLabellingFunc |
        Callable[[str], str] |
        StripLabellingDict
    )

    # Plotnine Classes
    Aes: TypeAlias = aes
    Coord: TypeAlias = coord
    Facet: TypeAlias = facet
    Geom: TypeAlias = geom
    Ggplot: TypeAlias = ggplot
    Guide: TypeAlias = guide
    Layer: TypeAlias = layer
    Position: TypeAlias = position
    Scale: TypeAlias = scale
    ScaleContinuous: TypeAlias = scale_continuous
    ScaleDiscrete: TypeAlias = scale_discrete
    Stat: TypeAlias = stat
    Theme: TypeAlias = theme
    Watermark: TypeAlias = watermark

    # Plotnine Other

    ScaledAestheticsName: TypeAlias = Literal[
        'x',
        'y',
        'alpha',
        'color',
        'colour',
        'fill',
        'linetype',
        'shape',
        'size',
        'stroke',
    ]

    # Mizani
    Trans: TypeAlias = trans

    # Tuples
    TupleInt2: TypeAlias = tuple[int, int]
    TupleFloat2: TypeAlias = tuple[float, float]
    TupleFloat3: TypeAlias = tuple[float, float, float]
    TupleFloat4: TypeAlias = tuple[float, float, float, float]

    # Arrays (strictly numpy)
    BoolArray: TypeAlias = npt.NDArray[np.bool_]
    FloatArray: TypeAlias = npt.NDArray[np.float64]
    IntArray: TypeAlias = npt.NDArray[np.int64]
    AnyArray: TypeAlias = npt.NDArray[Any]

    # Series
    IntSeries: TypeAlias = pd.Series[int]
    FloatSeries: TypeAlias = pd.Series[float]
    AnySeries: TypeAlias = pd.Series[Any]

    # ArrayLikes
    IntArrayLike: TypeAlias = IntArray | IntSeries | Sequence[int]
    FloatArrayLike: TypeAlias = FloatArray | FloatSeries | Sequence[float]
