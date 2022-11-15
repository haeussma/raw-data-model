import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .data import Data


@forge_signature
class Measurements(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementsINDEX"),
        xml="@id",
    )

    initial_substrate: Optional[float] = Field(
        description="Initial substrate concentration of the reaction.", default=None
    )

    data: Optional[Data] = Field(
        description="Replicates of a measurement", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a609d6a21561682ca3b5e350138a35e2ba3ccdc7"
    )
