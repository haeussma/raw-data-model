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
        default="a609d6a21561682ca3b5e350138a35e2ba3ccdc7"
    )

    def add_to_measurements(
        self,
        initial_substrate: Optional[float] = None,
        data: Optional[Data] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Measurements' to the attribute 'measurements'.

        Args:


            id (str): Unique identifier of the 'Measurements' object. Defaults to 'None'.


            initial_substrate (Optional[float]): Initial substrate concentration of the reaction. Defaults to None


            data (Optional[Data]): Replicates of a measurement. Defaults to None
        """

        params = {"initial_substrate": initial_substrate, "data": data}
        if id is not None:
            params["id"] = id
        measurements = [Measurements(**params)]
        self.measurements = self.measurements + measurements
