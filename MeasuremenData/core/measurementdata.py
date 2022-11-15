import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime
from .measurements import Measurements
from .data import Data


@forge_signature
class MeasurementData(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementdataINDEX"),
        xml="@id",
    )

    pH: Optional[float] = Field(description="pH of the experiment.", default=None)

    name: Optional[str] = Field(description="Name of the experiment.", default=None)

    date: Optional[datetime] = Field(
        description="Date of the measurement.", default=None
    )

    time: List[float] = Field(
        description="Time axis of the experiment.", default_factory=ListPlus
    )

    temperature: Optional[float] = Field(
        description="Temperature of the reaction.", default=None
    )

    measurements: List[Measurements] = Field(
        description="Date of the measurement.", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/haeussma/raw-data-model.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="ff1caee19bba76cb7f5f11ee5f195d5dab5b702a"
    )

    def add_to_measurements(
        self,
        data: List[Data],
        initial_substrate: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Measurements' to the attribute 'measurements'.

        Args:


            id (str): Unique identifier of the 'Measurements' object. Defaults to 'None'.


            data (List[Data]): Replicates of a measurement.


            initial_substrate (Optional[float]): Initial substrate concentration of the reaction. Defaults to None
        """

        params = {"data": data, "initial_substrate": initial_substrate}
        if id is not None:
            params["id"] = id
        measurements = [Measurements(**params)]
        self.measurements = self.measurements + measurements
