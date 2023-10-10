# AutomatedKerberoasting

A brief description of your project.

## Table of Contents

- [Overview](#overview)
- [Scripts and Usage](#scripts-and-usage)
  - [kerb2.bat and kerb2.ps1](#kerb2bat-and-kerb2ps1)
  - [main.py](#mainpy)
  - [obtainer.py](#obtainerpy)
  - [systemsetup.bat and systemsetup.ps1](#systemsetupbat-and-systemsetupps1)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

Provide a high-level overview of your project, its goals, and any relevant background information.

## Scripts and Usage

### kerb2.bat and kerb2.ps1

#### Description

These scripts are related to Kerberoasting, a technique used to extract service account credentials from Active Directory.

#### Usage

- **kerb2.bat**: A batch script that executes `kerb2.ps1`.
- **kerb2.ps1**: A PowerShell script that queries the domain for Service Principal Names (SPNs) associated with user accounts.
  - To execute, run `kerb2.ps1`.
  - Optionally, use the `-Request` switch to request Kerberos tickets for identified SPNs.
  - The script saves the results to a file named `kerbout.txt`.

### main.py

#### Description

This Python script appears to perform various actions. Please provide more detailed comments or explanations of its functionality.

#### Usage

- Execute `main.py` to run the script.
- Ensure that the required Python dependencies are installed.

### obtainer.py

#### Description

This Python script collects system information from a Windows system.

#### Usage

- Execute `obtainer.py` to run the script.
- Ensure that the required Python dependencies are installed.

### systemsetup.bat and systemsetup.ps1

#### Description

These scripts are related to setting up a system or making specific system modifications.

#### Usage

- **systemsetup.bat**: A batch script that executes `systemsetup.ps1`.
- **systemsetup.ps1**: A PowerShell script that modifies Windows Defender settings (disables real-time monitoring) and downloads another script (Invoke-Kerberoast.ps1).
  - It then invokes `Invoke-Kerberoast.ps1` and saves the output to a file named `nothingyouneedtobeworriedabout.txt`.

## Installation

Provide installation instructions if any external dependencies or setup steps are required to use your project. If not, you can mention that there are no specific installation requirements.

## Usage

Explain how to use your project, including examples of command-line usage or any specific configurations. Provide step-by-step instructions for running each script or batch file.

## Dependencies

List the external libraries, tools, or software that your project depends on. Include version numbers if applicable.

## Contributing

Explain how others can contribute to your project, whether through bug reporting, feature requests, or code contributions. Provide guidelines for submitting contributions and contact information for getting in touch with you.

## License

Specify the license under which your project is distributed. Include any licensing information, terms, and conditions.
