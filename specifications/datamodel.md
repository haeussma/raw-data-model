# RawData

### MeasurementData

- __pH__
  - Type: float
  - Description: pH of the experiment.
- __name__
  - Type: string
  - Description: Name of the experiment.
- __date__
  - Type: datetime
  - Description: Date of the measurement.
- __time__
  - Type: float
  - Description: Time axis of the experiment.
  - Multiple: True
- __temperature__
  - Type: float
  - Description: Temperature of the reaction.
- __measurements__
  - Type: Measurements
  - Description: Date of the measurement.
  - Multiple: True

### Measurements

- __initial_substrate__
  - Type: float
  - Description: Initial substrate concentration of the reaction.
- __data__
  - Type: Data
  - Description: Replicates of a measurement
  - Multiple: True

### Data

- __replicates__
  - Type: float
  - Description: Measurement series.
  - Multiple: True
