import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime
from pydantic import Field
from typing import List
from typing import Optional

from .measurements import Measurements


@forge_signature
class MeasurementData(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementdataINDEX"),
        xml="@id",
    )
    pH: Optional[float] = Field(
        description="pH of the experiment.",
        default=None,
    )

    name: Optional[str] = Field(
        description="Name of the experiment.",
        default=None,
    )

    date: Optional[datetime] = Field(
        description="Date of the measurement.",
        default=None,
    )

    time: List[float] = Field(
        description="Time axis of the experiment.",
        default_factory=ListPlus,
    )

    temperature: Optional[float] = Field(
        description="Temperature of the reaction.",
        default=None,
    )

    measurements: Optional[Measurements] = Field(
        description="Date of the measurement.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8bfaa1cb3110ea502b070ae750da439859fd71fe"
    )
