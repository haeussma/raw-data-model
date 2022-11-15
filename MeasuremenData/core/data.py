import sdRDM

from typing import Optional, Union
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Data(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dataINDEX"),
        xml="@id",
    )

    replicates: List[float] = Field(
        description="Measurement series.", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a609d6a21561682ca3b5e350138a35e2ba3ccdc7"
    )
