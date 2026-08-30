# Passwordium 🔐

Developed By: Malek F Saleh 

A simple desktop password manager built with Python.

![Passwordium Screenshot](screenshot.png)

## Features

- 🔐 Password management
- 🔑 Password generation
- 💾 Local password storage
- 🖥️ Desktop interface
- 📝 Simple and easy to use

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

Since you're using Linux, I'll make the Linux instructions the main method.

## Installation & Setup

Follow these steps to install and run Passwordium from a fresh Linux installation.

### 1. Install Git

If Git is not already installed:

```bash
sudo apt update
sudo apt install git -y

Check that Git is installed:

git --version
2. Install Python

Install Python, pip, and the virtual environment package:

sudo apt install python3 python3-pip python3-venv -y

Check your Python version:

python3 --version

Check pip:

pip3 --version
3. Clone Passwordium

Clone the repository from GitHub:

git clone https://github.com/malek878saleh/passwordium.git
4. Enter the Passwordium folder
cd passwordium
5. Create a virtual environment

Create a Python virtual environment:

python3 -m venv venv
6. Activate the virtual environment
source venv/bin/activate

You should now see (venv) at the beginning of your terminal:

(venv) user@computer:~/passwordium$
7. Install the required dependencies

Install all required Python packages:

pip install -r requirements.txt
8. Start Passwordium

Run the application:

python3 app.py

Passwordium should now start.

##########################################

## Installation & Setup — Windows

Follow these steps to install and run Passwordium on Windows.

### 1. Install Git

Download and install Git for Windows:

https://git-scm.com/download/win

After installation, open **PowerShell** or **Command Prompt** and check:

```powershell
git --version
