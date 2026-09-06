# Mesh Warp

The Mesh Warp filter can be used to distort specific areas of an image without affecting other areas.

For example, it can be used for dramatic warping effects on a landscape image or for more subtly focused retouching of facial features.

![Before](../../../assets/shared/warp_before.jpg)
![After](../../../assets/shared/warp_after.jpg)
*Warping an image*

## About the Mesh Warp filter

This filter is applied on its own layer as a [non-destructive, live filter](../../06-layers/08-using-live-filters.md). It can be accessed via the **Layer** menu, by selecting from the **New Live Filter Layer**>**Distort**>**Mesh Warp**.

### Settings:

The following settings can be adjusted from the context toolbar:

- Choose between **Destination** and **Source** mode from the pop-up menu. **Source** mode allows you to set default mesh points that can then be restored with **Synchronize**.
- **Reset**—restores the grid to a uniform rectangular shape. Nodes which have been added are distributed evenly across the grid.
- **Hide/Show Mesh**—hides/shows the grid. The warp mesh can still be adjusted when hidden (indicated by the cursor change).
- **Convert**—switches the selected node to **Sharp** or **Smooth**.
- **Done**—accepts the current warp applied to the image and exits the warp operation.

> **Note:** The Mesh Warp Tool and Mesh Warp live filter provide the same settings on their context toolbars.

#### SEE ALSO:

- [Using live filters](../../06-layers/08-using-live-filters.md)
- [Applying filters](../01-applying-filters.md)
- [Mesh warping](../../05-sizing-cropping-and-warping/06-mesh-warping.md)
