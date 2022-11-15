import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .data import Data


@forge_signature
class Measurements(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementsINDEX"),
        xml="@id",
    )
    initial_substrate: Optional[float] = Field(
        description="Initial substrate concentration of the reaction.",
        default=None,
    )

    data: Optional[Data] = Field(
        description="Replicates of a measurement",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8bfaa1cb3110ea502b070ae750da439859fd71fe"
    )
