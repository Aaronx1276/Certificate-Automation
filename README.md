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

 **To install Pillow, use**: 
```bash
pip install pillow
```

**To install Tkinter, use**:
```bash
pip install tk
```

## Prepare the input files:
1. Template File:
- Place your certificate template image in the project folder and name it template.jpg.
- The template should have space reserved for the participant's name and event name.
2. Participant Names:
- Create a requirements.txt file in the project folder.
- Add the names of participants, one name per line.

## Run this Project:
1. Clone or download the repository.
2. Open a terminal in the project folder and run:
   ```bash
   python certificate_automation.py
   ```
3. Enter the event name in the text box provided in the GUI.
4. Click the Generate Certificates button.

## Check the Output:
- The certificates will be generated in the certificates folder within the project directory.
- Each certificate will be named as <participant_name>_certificate.jpg.

## Example:
**Input**:
requirements.txt:
```bash
Alice Johnson
Bob Smith
Charlie Brown
```
Event Name: "Python Workshop"

**Output**:
Certificates in the certificates folder:

- Alice Johnson_certificate.jpg
- Bob Smith_certificate.jpg
- Charlie Brown_certificate.jpg

## Screenshot
![image](https://github.com/user-attachments/assets/a3a01cdf-7626-41fa-8cfc-dfb390eaac63)


## Contributions
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

