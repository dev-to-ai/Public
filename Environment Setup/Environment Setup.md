# Environment Setup Guide

This guide walks you through setting up a clean Python development environment using **Python**, **VS Code**, and a **virtual environment**, with common data science tools installed.

---

## Step 1: Install Python (3.14+)

Download and install **Python 3.14 or newer** from the official Python website.

### Verify Installation

Open a terminal (or Command Prompt) and run:

```bash
python --version
```

Expected output:

```text
Python 3.x.x
```

Check that `pip` is installed:

```bash
pip --version
```

Expected output:

```text
pip x.x.x
```

---

## Step 2: Install Visual Studio Code (VS Code)

Download and install **Visual Studio Code** from the official VS Code website.

---

## Step 3: Set Up Project Folder and Open VS Code

Navigate to your project folder:

```bash
cd YOUR_FOLDER
```

Open the folder in VS Code:

```bash
code .
```

---

## Step 4: Install VS Code Extensions

In VS Code, install the following extensions:

* **Python** (by Microsoft)
* **Jupyter** (by Microsoft)

These extensions provide syntax highlighting, debugging, virtual environment support, and notebook integration.

---

## Step 5: Set Up a Virtual Environment

Open the **VS Code Terminal** and run:

```bash
python -m venv venv
```

### Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of the terminal prompt, indicating the environment is active.

---

## Step 6: Install Required Packages

### Install `uv`

`uv` is a fast Python package and project manager written in Rust.

```bash
pip install uv
```

### Install Core Packages

```bash
uv pip install numpy pandas jupyter notebook
```

---

## Step 7: Verify Package Installation

Run the following commands to confirm everything is installed correctly:

```bash
python -c "import numpy; print('NumPy version:', numpy.__version__)"
```

```bash
python -c "import pandas; print('Pandas version:', pandas.__version__)"
```

```bash
python -c "import notebook; print('Jupyter Notebook version:', notebook.__version__)"
```

---

✅ Your Python environment is now ready for development!
