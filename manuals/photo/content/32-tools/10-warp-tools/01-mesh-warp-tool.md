# Mesh Warp Tool

The **Mesh Warp Tool** allows you to distort an image (or portion of an image) using a highly customizable grid comprising of nodes and lines.

![Before](../../../assets/shared/warp_before.jpg)
![After](../../../assets/shared/warp_after.jpg)
*Warping an image*

## Mesh Warp Tool vs Mesh Warp live filter

A mesh warp can be applied as a [non-destructive, live filter](../../06-layers/08-using-live-filters.md). It can be accessed via the **Layer** menu, from the **New Live Filter Layer>Distort** category. Its provides the same context toolbar settings as the Mesh Warp Tool.

The live filter allows the effect to be edited (or removed) at any time after its initial application, using all of the original image's pixel data.

In contrast, the Mesh Warp Tool can be reapplied but each time it uses the already warped image and so useful pixel data may have been lost.

### Settings

The following settings can be adjusted from the context toolbar:

- **Apply**—accepts the current warp applied to the image and exits the warp operation.
- Choose between **Destination** and **Source** mode from the pop-up menu. **Source mode** allows you to set default mesh points that can then be restored with **Synchronize**.
- **Synchronize**—restores the original, unwarped image while maintaining any adjusted mesh grid.
- **Reset**—restores the grid to a uniform rectangular shape. Nodes which have been added are distributed evenly across the grid.
- **Hide Mesh**—hides/shows the grid. The warp mesh can still be adjusted when hidden (indicated by the cursor change).
- **Convert**—switches the selected node to **Sharp** or **Smooth**.

#### SEE ALSO:

- [Mesh warping](../../05-sizing-cropping-and-warping/06-mesh-warping.md)
