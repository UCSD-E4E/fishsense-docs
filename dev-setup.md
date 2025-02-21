# Development Environment Setup
This document details how to setup the development environment for most FishSense projects. Some projects may have additional setup.

## Accelerator Access
Since most students are assumed to bring their own device (BYOD), we will focus on the most compatible configurations first.  Please note that the most compatible configuration will not be the most performant configuration. If performance is important, please jump to either the [Linux + Docker](#linux--docker--cuda-5) or [Ubuntu 24.04 + CUDA](#ubuntu-2404--cuda-5) sections.

Each section will be given a score from 1-5. 5 indicates full compatiblity with accelerators. 1 indicates no compatibility. Justification will be given for each.

### macOS + Docker (1)
This configuration supports no accelerators. Adding support for accelerators is not possible.

### Windows + WSL + CUDA (3)
CUDA is (mostly) supported out of the box. OpenCL support can be handled by building PoCL using CUDA. `wgpu` requires either DirectX or Vulkan. As WSL supports DirectX but not Vulkan, it should be possible to contribute to `wgpu` to get it to use DirectX on WSL.

### Windows + Docker + CUDA (2)
Our CUDA Docker container is not supported currently on Windows Docker Desktop as it expects access to hardware. We could introduce a container that would be explicitly for WSL.  This would allow CUDA + OpenCL but would still be without Vulkan. It is not currently possible to get hardware accelerated Vulkan in Docker on WSL.

### Windows + WSL (2)
This implementation would allow access to DirectX in `wgpu` if it was extended to support it.  See [Windows + Docker + CUDA](#windows--wsl--cuda-3) for additional details.

### Windows + Docker (1)
This configuration supports no accelerators. Adding support for accelerators is not possible.

### Linux + Docker + CUDA (5)
The current CUDA Docker container can run with access to OpenCL, Vulkan, and CUDA accelerators.  This provides access to the most accelerators out of all options.

### Linux + Docker (1)
Without an NVIDIA accelerator, we cannot pass the device through to container and thus cannot access the accelerator.

### Ubuntu 24.04 + CUDA (5)
This provides equal access to accelerators as [Linux + Docker + CUDA](#linux--docker--cuda-5).

### Ubuntu 24.04 (3)
This provides access to OpenCL and Vulkan as we are running on hardware.  Without an NVIDIA device, we cannot use CUDA.

## Setup

### Install VSCode
Install Visual Studio Code on your device by following the [instructions](https://code.visualstudio.com/).

### Install Docker
On Windows and macOS, install Docker Desktop by following the [instructions](https://www.docker.com/products/docker-desktop/). On Windows, ensure you enable to Docker WSL backend.

On Linux, follow your distro's instructions for installing Docker.  We recommend the instructions from [here](https://docs.docker.com/engine/install/ubuntu/) for Ubuntu.

### Install the Dev Containers Extension
Please install the dev containers extension from [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). You will also be prompted to install it when you open a repo.