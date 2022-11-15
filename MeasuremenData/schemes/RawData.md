```mermaid
classDiagram
    MeasurementData *-- Measurements
    Measurements *-- Data
    
    class MeasurementData {
        +float pH
        +string name
        +datetime date
        +float[0..*] time
        +float temperature
        +Measurements measurements
    }
    
    class Measurements {
        +float initial_substrate
        +Data data
    }
    
    class Data {
        +float[0..*] replicates
    }
    
```