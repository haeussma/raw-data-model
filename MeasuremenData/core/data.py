import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List


@forge_signature
class Data(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dataINDEX"),
        xml="@id",
    )
    replicates: List[float] = Field(
        description="Measurement series.",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8bfaa1cb3110ea502b070ae750da439859fd71fe"
    )
