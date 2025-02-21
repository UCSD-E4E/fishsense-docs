# System Requirements

All projects under the FishSense umbrella are intended to run on Ubuntu 24.04 unless otherwise stated. Either amd64 or aarch64 are considered to be compatible.

## Fully Supported Configurations
These are the only fully supported configurations. These will run with acceleration. If you cannot satisfy one of these, please review the [Partially Supported Configurations](#partiall-supported-configurations) sections.

* Ubuntu 24.04 amd64/arm64 + Vulkan + OpenCL
* Ubuntu 24.04 amd64 + Vulkan + OpenCL + CUDA
* Linux amd64 + Vulkan + OpenCL + CUDA

## Partiall Supported Configurations

* WSL Ubuntu 24.04 + CUDA + PoCL (Software Vulkan)
    * Rust WebGPU does not currently leverage DirectX in WSL and will fallback to software Vulkan.
* Windows + Docker (Software OpenCL, Software Vulkan, No CUDA)
    * The FishSense CUDA Docker container is not currently compatible with WSL.
* Apple Silicon Mac + Docker (Software OpenCL, Software Vulkan, No CUDA)
* Intel Mac + Docker (Software OpenCL, Software Vulkan, No CUDA)
* Linux amd64/arch64 without NVIDIA + Docker (Software OpenCL, Software Vulkan, No CUDA)
