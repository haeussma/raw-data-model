# RawData

### MeasurementData

- **pH**
  - Type: float
  - Description: pH of the experiment.
- **name**
  - Type: string
  - Description: Name of the experiment.
- **date**
  - Type: datetime
  - Description: Date of the measurement.
- **time**
  - Type: float
  - Description: Time axis of the experiment.
  - Multiple: True
- **temperature**
  - Type: float
  - Description: Temperature of the reaction.
- **measurements**
  - Type: Measurements
  - Description: Date of the measurement.

### Measurements

- **initial_substrate**
  - Type: float
  - Description: Initial substrate concentration of the reaction.
- **data**
  - Type: Data
  - Description: Replicates of a measurement.

### Data

- **replicates**
  - Type: float
  - Description: Measurement series.
  - Multiple: True
