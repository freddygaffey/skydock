
# SkyDock Project: Environment Setup and Dependencies

This document outlines the setup process for the SkyDock project, including installing dependencies and preparing the virtual environment.

---

## 1. Prerequisites

Follow the guide from Core Electronics on installing YOLO object detection on the Raspberry Pi AI Hat:
[YOLO Object Detection on the Raspberry Pi AI Hat](https://core-electronics.com.au/guides/raspberry-pi/yolo-object-detection-on-the-raspberry-pi-ai-hat-writing-custom-python/)

This guide ensures all required software and drivers for the Hailo-8 AI accelerator are installed.

---

## 2. Virtual Environment

We use a dedicated Python virtual environment for the project:

```bash
# Create the virtual environment (if not already created)
python3 -m venv venv_hailo_rpi_examples

# Activate the virtual environment
source venv_hailo_rpi_examples/bin/activate
```

> The project should always be run inside the `(venv_hailo_rpi_examples)` virtual environment.

---

## 3. Setting Up the Hailo RPi Examples

Navigate to the Hailo RPi examples folder and run the setup script:

```bash
cd ~/hailo_rpi_examples
source setup.sh
```

> This prepares the environment with necessary Hailo tools and configurations.
> This step should be repeated whenever the project environment is refreshed.

---

## 4. Installing Project Dependencies

Next, navigate to the SkyDock software directory and install the Python dependencies:

```bash
cd ~/skydock/software
pip install -r requirements.txt
```

> Ensure this step is executed every time the virtual environment is recreated or updated.

---

## 5. Recommended Workflow

Each time you start working on the project:

1. Activate the virtual environment:

```bash
source ~/venv_hailo_rpi_examples/bin/activate
```

2. Set up the Hailo RPi examples:

```bash
cd ~/hailo_rpi_examples
source setup.sh
```

3. Navigate to the SkyDock software directory:

```bash
cd ~/skydock/software
```

note: thanks ChatGpt for making this doc nice 
