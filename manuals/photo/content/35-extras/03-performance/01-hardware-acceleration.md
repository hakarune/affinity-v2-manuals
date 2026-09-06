# Hardware acceleration

**macOS:** To improve the performance of some operations, Affinity Photo 2 can use Apple's Metal technology to talk directly to your system's graphics hardware.

**Windows:** To improve the performance of some operations, Affinity Photo 2 can use OpenCL technology to talk directly to your system's graphics hardware.

Hardware acceleration is available for many graphics processors (GPUs), whether integrated into your computer's CPU (central processing unit), a discrete graphics card or onboard processor, or external and connected via Thunderbolt 3. Affinity Photo 2 can make use of multiple GPUs in parallel.

It is recommended that hardware acceleration is enabled unless you experience unusual performance problems or our technical support team instructs you to disable it.

> **Note:** Hardware acceleration is enabled by default. If you experience poorer performance than expected, try disabling it to see if CPU-based processing works better on your system. CPU and GPU performance can be numerically compared using Affinity Photo 2’s built-in benchmark.

## Benefits

In practice, the performance boost depends on the task at hand.

Hardware acceleration is of great benefit to many raster-based tasks. Vector operations and specific features like blend ranges are performed on the CPU.

Tools, adjustments, filters and other operations including RAW development will use GPU resources to achieve improved performance.

The benefits are especially noticeable when stacking several [Live filter layers](../../06-layers/08-using-live-filters.md) together—export times are significantly quicker and canvas previewing is snappier.

## Cost

As a trade-off, memory requirements are increased and performance may be dependent on the amount of VRAM available to the GPU(s).

The VRAM requirement depends on the complexity of your workflow. Document resolution and bit depth, screen resolution, and layer complexity all contribute to it.

Using a 4K display as a baseline, 1–2 GB of VRAM is sufficient for most light editing. For large amounts of compositing work, consider a GPU with 4GB—especially when working to 16-bit precision.

To perform 32-bit 3D rendering work with many layers, 4 GB is the minimum amount, though we recommend 8 GB.

**Windows:**

## System requirements

Affinity support for OpenCL compute acceleration requires Windows 10.0.19042 (May 2020) or later.

It also requires GPU support for [Direct3D 12 Feature Level 12.0](https://en.wikipedia.org/wiki/Feature_levels_in_Direct3D#Direct3D_12), meaning the GPU must feature AMD's GCN (Graphics Core Next), NVIDIA's Maxwell, or Intel HD Graphics 510 (Skylake) or a later microarchitecture.

## Comparing results

To assess the benefit of hardware acceleration to your system, use [Affinity Photo 2's built-in benchmark](02-benchmark.md) to measure and compare single- and multi-core CPU, single GPU and, where applicable, multi-GPU performance.

**To enable or disable hardware acceleration:**

1. **macOS:** Select **Affinity Photo 2>Settings** (or **>Preferences**).
2. **Windows:** Select **Edit>Settings**.
3. Select **Performance**.
4. **macOS:** Set **Enable Metal compute acceleration** as required.
5. **Windows:** Set **Enable OpenCL compute acceleration** as required.

The setting is inaccessible if Affinity Photo 2 is unable to detect a compatible GPU on your system.

When enabled, compatible GPUs in use by the setting are listed under it.

#### SEE ALSO:

- [Performance settings](../../37-settings-preferences/01-settings-preferences.md)
- [Benchmark](02-benchmark.md)
