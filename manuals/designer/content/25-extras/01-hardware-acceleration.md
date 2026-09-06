# Hardware acceleration

To improve the performance of some operations, Affinity Designer can use Apple's Metal technology to talk directly to your system's graphics hardware.

To improve the performance of some operations, Affinity Designer can use OpenCL technology to talk directly to your system's graphics hardware.

Hardware acceleration is available for many graphics processors (GPUs), whether integrated into your computer's CPU (central processing unit), a discrete graphics card or onboard processor, or external and connected via Thunderbolt 3. Affinity Designer can make use of multiple GPUs in parallel.

It is recommended that hardware acceleration is enabled unless you experience unusual performance problems or our technical support team instructs you to disable it.

> **Note:** Hardware acceleration is enabled by default. If you experience poorer performance than expected, try disabling it to see if CPU-based processing works better on your system.

## Benefits

In practice, the performance boost depends on the task at hand.

Hardware acceleration is of great benefit to many raster-based tasks. Vector operations and specific features like blend ranges are performed on the CPU.

Tools, adjustments, canvas previewing and other operations will use GPU resources to achieve improved performance.

## Cost

As a trade-off, memory requirements are increased and performance may be dependent on the amount of VRAM available to the GPU(s).

The VRAM requirement depends on the complexity of your workflow. Document resolution and bit depth, screen resolution, and layer complexity all contribute to it.

## System requirements

Affinity support for Metal compute acceleration requires macOS High Sierra 10.13 or later.

Affinity support for safe unplugging of eGPUs requires macOS Mojave 10.14 or later.

Affinity support for OpenCL compute acceleration requires Windows 10.0.19042 (May 2020) or later.

It also requires GPU support for [Direct3D 12 Feature Level 12.0](https://en.wikipedia.org/wiki/Feature_levels_in_Direct3D#Direct3D_12), meaning the GPU must feature AMD's GCN (Graphics Core Next), NVIDIA's Maxwell, or Intel HD Graphics 510 (Skylake) or a later microarchitecture.

**To enable or disable hardware acceleration:**

1. Select **Affinity Designer>Settings** (or **>Preferences**).
2. Select **Edit>Settings**.
3. Select **Performance**.
4. Set **Enable Metal compute acceleration** as required.
5. Set **Enable OpenCL compute acceleration** as required.

The setting is inaccessible if Affinity Designer is unable to detect a compatible GPU on your system.

When enabled, compatible GPUs in use by the setting are listed under it.

#### SEE ALSO:

- [Performance settings](../27-settings-preferences/01-settings-preferences.md)
