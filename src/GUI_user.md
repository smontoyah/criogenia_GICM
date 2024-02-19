# Cryo-GICM Test Application

This is a Python application for conducting Cryogenic Gas Insulated Cable Monitoring (Cryo-GICM) tests. The application allows users to input test parameters, run the test, record data, and visualize the results. The test involves measuring temperature readings at different heights during a vertical movement of a sensor.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Test Procedure](#test-procedure)
- [Data Storage](#data-storage)
- [Data Visualization](#data-visualization)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Cryo-GICM is a specialized test for monitoring temperature variations and electronics devides response along the height of a cylindrical dewar filled with LN. This application is designed to facilitate and automate the test procedure, ensuring accurate data collection and analysis.

## Requirements

Before using this application, ensure you have the following components and dependencies:

- Python 3.x
- PyQt5 library
- DAQ_multimetros library (for interfacing with measurement devices)
- motor_paso library (for controlling a motor)
- Matplotlib library (for data visualization)

You should also have the necessary hardware components, such as a motor and a multimetro, properly connected to your system.

## Usage

1. Install the required dependencies using `pip`:
   ```
   pip install PyQt5 DAQ_multimetros motor_paso matplotlib
   ```

2. Connect the motor and multimetro devices to your system.

3. Run the application by executing the script:
   ```
   python <script_name>.py
   ```

4. Fill in the test parameters in the application window:
   - Name of the Test
   - Name of the Experimentator
   - Total Height of the Scan (in centimeters)
   - Measurement Interval (in seconds)
   - Motor Step Value (in centimeters)

5. Click the "Correr Prueba" (Run Test) button to start the test.

## Test Procedure

The application conducts the Cryo-GICM test according to the following procedure:

1. Collect user-input test parameters.

2. Create a folder with the test name and current date for data storage.

3. Initialize and connect the motor and multimetro devices.

4. Perform temperature measurements while moving the sensor vertically.

5. Record the temperature values and motor positions in a text file and CSV file.

6. Generate a temperature vs. height graph and save it as an image.

7. Display the graph for visualization.

## Data Storage

The application stores the collected data in the following formats:

- Text File (.txt): Contains test parameters and temperature values.
- CSV File (.csv): Contains temperature values and corresponding heights.
- Graph Image (.png): Displays temperature vs. height graph.

All data files are saved in a folder named after the test with the current date.

## Data Visualization

The application generates a temperature vs. height graph using Matplotlib to visualize the temperature variations during the test.

## Contributors

- [Sebastian Montoya]

## License

This application is provided under the [MIT License](LICENSE).

---

