# Device Support List Checker (dsbcheck.py)

## Introduction:
The `dsbcheck.py` script is the main tool of this Python project, designed to automate the process of checking if a specific device model is officially supported in Infoblox NetMRI Device Support Lists (DSLs). Leveraging various technologies and libraries, it extracts text from PDF files, formats the text, and searches for the device model across multiple DSLs. Additionally, it integrates with JIRA to search for new device tickets if the device is not officially supported.

## Technologies Used:
- **Python 3.x:** The primary programming language used for scripting and automation.
- **PyPDF2:** A Python library for reading PDF files and extracting text content.
- **JIRA Python Library:** Enables integration with JIRA for searching new device tickets.
- **Subprocess Module:** Used for executing shell commands, such as installing Python packages via pip.
- **YAML:** Utilized for storing and loading authentication credentials securely.
- **Neotermcolor:** Provides colored output for a more user-friendly experience.

## Features:
- Extracts text from PDF files containing DSLs
- Formats the extracted text to remove unnecessary information
- Searches for the specified device model across DSLs
- Displays the DSL versions that officially support the device model
- Utilizes JIRA to search for new device tickets if the device is not officially supported

## Skills Demonstrated:
- **Scripting and Automation:** Developed in Python, the script demonstrates proficiency in scripting and automating repetitive tasks.
- **PDF Processing:** Leveraging the PyPDF2 library, the script efficiently extracts text from PDF files.
- **API Integration:** Integrated with the JIRA API to search for new device tickets, showcasing proficiency in API usage and integration.
- **Error Handling:** Implemented error handling to gracefully handle missing modules and files, ensuring smooth execution.
- **User Interaction:** Utilizes user input to prompt for device model and provides clear output for easy interpretation.
- **Dependency Management:** Automatically installs missing dependencies via pip to ensure smooth execution, demonstrating knowledge of dependency management.

## Installation:
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing `dsbcheck.py`.
3. Install required dependencies using the following commands:

python3 -m pip install PyPDF2 jira neotermcolor

## Usage:
1. Run the `dsbcheck.py` script using the command:

python3 dsbcheck.py

2. Follow the on-screen prompts to enter the device model and view the output.

## Important Notes:
- Ensure that PDF files containing DSLs are located in the specified directory (`pdfdir`).
- Review and customize the output format and search criteria according to your specific requirements.
- Make sure to have proper permissions to access JIRA for searching new device tickets.

## Authors:
- Sanith
- Arun
- Ramees

## License:
This project is licensed under the [MIT License](LICENSE).

