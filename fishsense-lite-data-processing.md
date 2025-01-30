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

## Label the Lasers

Add the processed `JPG` files into a folder under `\\e4e-nas.ucsd.edu\label_studio`.  The folder name here should match the name of the project you will be using in Label Studio by convention.

### Using an existing project

If it is appropriate, you may add your images to an existing project.  After you do so, open the project's settings -> Cloud Stroage -> Click the Sync button that matches your cloud storage.

### Creating a new project

If it is appropriate, you may create a new project in Label Studio.  If you do, you should use the following code for your labeling interface as the CLI tools expect this structure:

```xml
<View>
  <KeyPointLabels name="kp-1" toName="img-1">
    <Label value="Red Laser" background="#FFA39E"/>
    <Label value="Green Laser" background="#26a269"/>
  </KeyPointLabels>
  <Image name="img-1" value="$img" zoom="true" zoomControl="true"/>
</View>
```

You can then sync this project with the Synology backend by adding a new Import Cloud Storage with the following configuration:

```yml
Storage Type: Synology
Storage Title: your-folder-name
URL: https://e4e-nas.ucsd.edu:6021
Path: /label_studio/your-folder-name
Username: label_studio
Password: ********
File Filter Regex: .*JPG
Treat every bucket object as a source file: True

```

Click "Add Storage" to save it.  Then click the "Sync" button.  Confirm that your images have been added.

## Laser Calibration

The laser needs to be recalibrated each dive.  In order to perform this calibration, we need to have completed laser labels in the steps above.  Once complete, navigate to the Label Studio project and export the data as a `JSON`.  You will need this to perform the laser calibration.

## Checkerboard Calibration

In order to perform the checkerboard calibration, you will need the following information

1. Lens Calibration
2. Laser Labels
3. The number of inside corners of your checkerboard
4. The square size of your checkerboard

With this information in hand, execute the following

```bash
fsl calibrate-laser *.ORF --lens-calibration fsl-01d-lens-raw.pkg --rows 17 --columns 24 --square-size 30 --output fsl-01d-laser.pkg --label-studio-json path/to/the/exported/label-studio.json
```

## Dive Slate Calibration

TODO