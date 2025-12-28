# Air-Floating Substrate Handler Calibration Routine

## Overview
This repository contains a version-controlled calibration routine for an air-floating system used to handle 8K generation glass substrates in a slit coater. The routine ensures positioning accuracy of ±5 μm by performing systematic calibration steps and compensation for real-world factors like substrate warpage.

## Hardware Specification
The calibration routine is designed for **Air-Floating Handler Model XJ-2000**, integrated into AOI systems and slit coaters for TFT Array and Color Filter manufacturing. The system uses precision air bearings to float glass substrates, minimizing contact and enabling high-accuracy positioning.

## Environment Setup

### Prerequisites
- Python 3.8 or later
- Git
- Access to the air-floating handler's control interface (simulated in this script)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/michelnydiccd/airfloat-calibration-v2.git
   cd airfloat-calibration-v2
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. No external dependencies are required for the basic calibration script. Future enhancements may add requirements.

### Running the Calibration
Execute the calibration script:
```bash
python calibrate.py
```

The script will simulate the calibration steps and output status messages.

## Version History
See the [Releases](https://github.com/michelnydiccd/airfloat-calibration-v2/releases) page for detailed version notes and changes.