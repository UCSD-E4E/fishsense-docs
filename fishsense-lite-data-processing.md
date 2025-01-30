# FishSense Lite Data Processing

This document is intended to detail how to process data using the FishSense Lite Data Processing CLI.

## Prerequisites

Before you begin, you will need your camera number.  The following steps will be specific to a specific camera.  The FishSense Lite CLI is only supported on Ubuntu 24.04 on x86-64.

## Naming Conventions

All FishSense Lite cameras will have a serial number of the form `FSL-xxD` or `FSL-xxF`, where `xx` represents a 0-padded, two digit number. `D` denotes the corrective optic. `F` denotes cameras without the corrective optic.

## Lens Calibration

### Generate New Lens Calibration Tables

TODO

### Existing Lens Calibration

Existing FishSense Lite Calibration parameters can be found here: `\\e4e-nas.ucsd.edu\fishsense\Fishsense Lite Calibration Parameters`.  Ensure that you grab the one that matches your camera configuration.

## Generating a Ray Config

Before running the CLI, you must generate a Ray config.  This is necessary before continuing.  This will control the number of CPUs and GPUs the CLI will request.  Execute the following command

```bash
fsl generate-ray-config --max-cpu <cpu count> --max-gpu <gpu count>
```

## Preprocessing the Images for Labeling

Now that you have selected your camera calibration, it is now time to rectify the images you have collected. To do so, run the following command

```bash
fsl preprocess *.ORF --format JPG --lens-calibration fsl-01d-lens-raw.pkg --output-path laser-calibration.pkg
```