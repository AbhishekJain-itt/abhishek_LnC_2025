# Data Processing System (Clean Code Refactoring)

##  Overview

This project is a refactored version of a legacy data processing system. The original implementation violated several Clean Code principles such as Single Responsibility Principle, tight coupling, and poor separation of concerns.

The system processes data from an input file, validates it, transforms it, and exports the results into multiple formats (CSV, JSON, XML).

---

##  Objectives

* Convert legacy C# code into Python
* Identify Clean Code violations
* Refactor the system using best practices
* Improve maintainability, scalability, and testability

---

##  Features

*  Read data from CSV file
*  Validate records
*  Transform data (uppercase names, formatted dates, derived values)
*  Calculate statistics
*  Export to multiple formats:

  * CSV
  * JSON
  * XML
*  Logging support

---

##  Project Structure

```
data_processing_app/
│
├── main.py
├── config.py
│
├── models/
│   └── record.py
│
├── services/
│   ├── file_reader.py
│   ├── parser.py
│   ├── validator.py
│   ├── transformer.py
│   └── statistics.py
│
├── exporters/
│   ├── base_exporter.py
│   ├── json_exporter.py
│   ├── xml_exporter.py
│   └── csv_exporter.py
│
├── processor/
│   └── data_processor.py
│
├── utils/
│   └── logger.py
│
├── data/
│   └── (input/output files)
│
└── README.md
```

---

##  How to Run

### 1. Clone the repository

### 2. Run the application

```
python main.py
```

---

## Output

The system generates:

* `output.csv`
* `output.json`
* `output.xml`
* `log.txt`

---

##  Clean Code Improvements

###  Before Refactoring

* God Class (`DataProcessor`)
* Multiple responsibilities in a single class
* Tight coupling with file system and logic
* Use of primitive data structures (`Dictionary`)
* Long methods and poor readability
* Hardcoded logic (switch statements)

---

### After Refactoring

#### 1. Single Responsibility Principle (SRP)

Each component has a single responsibility:

* FileReader → reading files
* Parser → parsing data
* Validator → validation
* Transformer → transformation
* Exporters → output handling

---

#### 2. Separation of Concerns

Business logic is split into independent modules.

---

#### 3. Dependency Injection

Dependencies are injected into `DataProcessor`, making it:

* Testable
* Flexible
* Decoupled

---

#### 4. Strategy Pattern

Export functionality is implemented using interchangeable strategies:

* `JsonExporter`
* `XmlExporter`
* `CsvExporter`

---

#### 5. Domain Modeling

Replaced primitive structures with a proper `Record` class.

---

#### 6. Improved Readability

* Smaller functions
* Meaningful names
* Modular structure

---

## Example Flow

1. Read data from file
2. Parse into objects
3. Validate records
4. Transform data
5. Calculate statistics
6. Export results

---

