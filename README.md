# Certificate Automation

Certificate Automation is a Python-based project that allows you to generate personalized certificates for a list of participants. This project leverages the **Tkinter** library for a user-friendly GUI and the **Pillow** library for image manipulation.

## Features

- Generates certificates using a predefined template.
- Reads participant names from a text file (`requirements.txt`).
- Allows adding the event name dynamically through a GUI text box.
- Saves certificates in a dedicated folder (`certificates`).

## Project Structure

- certificate-automation/
- ├── certificates/ # Folder where generated certificates will be saved
- ├── template.jpg # Certificate template image
- ├── requirements.txt # Input file with participant names (one per line)
- ├── certificate_automation.py # Main Python script
- └── README.md # Project documentation


## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.7 or higher**
2. Required Python libraries:
   - **Pillow** (for image processing)
   - **Tkinter** (built into Python)

## To install Pillow, use: 

## Prepare the input files:
Template File:

Place your certificate template image in the project folder and name it template.jpg.
The template should have space reserved for the participant's name and event name.
Participant Names:

Create a requirements.txt file in the project folder.
Add the names of participants, one name per line.

