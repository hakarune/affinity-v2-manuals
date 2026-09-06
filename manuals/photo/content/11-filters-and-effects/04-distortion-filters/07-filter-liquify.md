# Liquify

The Liquify filter can be used to apply non-destructive liquify distortions to the entire image or masked regions of it.

![Before](../../../assets/shared/filter_liquify_before.jpg)
![After](../../../assets/shared/filter_liquify_after.jpg)
*Switching off/on the Liquify live filter layer whose mask was painted to remove unwanted leftover distortion.*

## About the Liquify filter

This filter is applied as a [non-destructive, live filter](../../06-layers/08-using-live-filters.md). It can be accessed via the **Layer** menu, by selecting from the **New Live Filter Layer** category.

When a warp is applied to an image, the overlaid mesh will update to describe the warp on a grid. Furthermore, modifying the grid will update the warped image below.

When warping images using this filter, the active Persona will switch to the [Liquify Persona](../../22-liquify-persona/01-warping-using-liquify-persona.md) and this Persona's [Liquify tools](../../32-tools/11-liquify-tools-liquify-persona/01-liquify-tools.md) will become available. These tools can be divided into three types:

- Direct—these affect the image by painting over image pixels. These include the **Liquify Push Forward**, **Liquify Push Left**, **Liquify Twirl**, **Liquify Pinch**, **Liquify Punch**, **Liquify Turbulence** and **Liquify Reconstruct** tools.
- Indirect—these affect the mesh. These include the **Mesh Clone** Liquify tool.
- [Masking](../../22-liquify-persona/02-masking-in-liquify-persona.md)—these apply or remove masked areas. These include the **Freeze** and **Thaw** Liquify tools.

These Liquify tools are supported by a dedicated [Brushes panel](../../22-liquify-persona/03-brush-panel.md).

Warping can be further modified and controlled using the [Mesh](../../22-liquify-persona/05-mesh-panel.md) and [Mask](../../22-liquify-persona/04-mask-panel.md) panels.

You can reset the warp you have applied at any time by selecting **Reset Mesh**.

Clicking **Done** will commit your warping and create a filter layer; to undo your changes before committing, scroll back the history steps in the Persona's **History** panel.

This filter layer behaves like any other live filter layer in that it is has inherent masking properties, is non-destructive, and can be temporarily hidden or deleted from the **Layers** panel, and even moved up or down the layer stack for different results.

#### SEE ALSO:

- [Using live filters](../../06-layers/08-using-live-filters.md)
- [Warping using Liquify Persona](../../22-liquify-persona/01-warping-using-liquify-persona.md)
