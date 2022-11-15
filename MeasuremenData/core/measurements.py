import sdRDM

from typing import Optional, Union
from typing import Optional
from typing import List
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

    data: List[Data] = Field(
        description="Replicates of a measurement", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="ff1caee19bba76cb7f5f11ee5f195d5dab5b702a"
    )

    def add_to_data(self, replicates: List[float], id: Optional[str] = None) -> None:
        """
        Adds an instance of 'Data' to the attribute 'data'.

        Args:


            id (str): Unique identifier of the 'Data' object. Defaults to 'None'.


            replicates (List[float]): Measurement series.
        """

        params = {"replicates": replicates}
        if id is not None:
            params["id"] = id
        data = [Data(**params)]
        self.data = self.data + data
