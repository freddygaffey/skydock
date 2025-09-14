# SkyDock Project: Environment Setup and Dependencies

This document outlines the setup process for the SkyDock project using the Hailo-8 AI accelerator and its pre-configured virtual environment.

---

## 1. Prerequisites

Follow the Core Electronics guide on YOLO object detection on the Raspberry Pi AI Hat:
[YOLO Object Detection on the Raspberry Pi AI Hat](https://core-electronics.com.au/guides/raspberry-pi/yolo-object-detection-on-the-raspberry-pi-ai-hat-writing-custom-python/)

> This guide installs all necessary Hailo tools, drivers, and automatically creates the Hailo virtual environment that will be used for the project.

---

## 2. Using the Hailo Virtual Environment

The Hailo setup creates its own virtual environment inside the `hailo_rpi_examples` folder. Use this environment whenever working on the project:

```bash
# Navigate to the Hailo examples folder
cd ~/hailo_rpi_examples

# Activate the environment and setup Hailo tools
source setup.sh
```

> The environment created here (`venv_hailo_rpi_examples`) is used as the main environment for running the SkyDock project.
> This step should be run each time you start a new terminal session before working on the project.

---

## 3. Installing SkyDock Project Dependencies

After activating the Hailo environment, navigate to the SkyDock software folder and install the Python dependencies:

```bash
cd ~/skydock/software
pip install -r requirements.txt
```

> This ensures all project-specific Python packages are installed on top of the Hailo virtual environment.

---

## 4. Recommended Workflow

Each time you begin working on the project:

1. Activate the Hailo virtual environment and setup Hailo tools:

```bash
cd ~/hailo_rpi_examples
source setup.sh
```

2. Navigate to the SkyDock software folder:

```bash
cd ~/skydock/software
```

3. Ensure project dependencies are installed:

```bash
pip install -r requirements.txt
```

> After completing these steps, you can run and develop SkyDock within the pre-configured Hailo virtual environment.

---

If you like, I can also make a **compact quickstart version** of this workflow so it’s just a few copy-paste commands to get going. It would exactly mirror your daily workflow with minimal steps. Do you want me to do that?

note: thanks ChatGpt for making this doc nice 
