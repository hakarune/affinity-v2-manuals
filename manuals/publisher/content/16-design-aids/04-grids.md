# Grids

A non-printing, non-exporting grid can be displayed in order to help you to create interesting and well-constructed page layouts.

![Grids](../../assets/shared/grids.png)

The grid is overlaid over your page to help you align objects. They are gray by default but can be any color you choose.

Grids default to the applied master page or spread grid settings but can be overridden by selecting a page or facing page spread and tweaking settings in the **Grid and Snapping Axis** dialog (**View>Grid and Axis**). Optionally, a grid can be applied to an individual page or spread which doesn't use master pages.

Grids can be automatic or fixed—the former (as default) changes the frequency of grid subdivisions as you zoom in/zoom out, the latter always keeps the grid frequency constant (irrespective of zoom level).

Grids work best when combined with snapping, in particular when the **Snap to Grid** option is enabled. They can be based on any document unit and will line up perfectly with [rulers](08-rulers.md) (when switched on).

> **Note:** If you are having difficulty seeing the grid clearly, try changing the grid color to something that contrasts with the background color.

**To show or hide the automatic grid:**

- On the **View** menu, select **Show Grid**.

**To adjust automatic grid spacing:**

With the **Zoom Tool** selected, do one of the following:

- Zoom in to see smaller grid divisions.
- Zoom out to see larger grid divisions.

At all zoom levels the grid shows as grid 'blocks' further split into grid subdivisions.

**To create a fixed square grid:**

1. From the **View** menu, select **Grid and Axis**.
2. Select **Basic** mode.
3. Set the **Spacing** and **Divisions** values.
4. Click **Close**.

**To customize grid color/opacity:**

1. From the **View** menu, select **Grid and Axis**.
2. Click the **Grid lines** or **Subdivision lines** swatch to display a pop-up panel to set the line color(s).
3. Drag the sliders to set the opacity of either, or both, line colors.
4. Click **Close**.

> **Note:** For a different color or opacity for the subdivision lines compared to the main grid lines, click the **Link the grid colors** symbol next to the swatches.

**To create a rectangular grid:**

1. From the **View** menu, select **Grid and Axis**.
2. Select **Advanced** and uncheck **Uniform**.
3. Do one of the following:
  - Set the **Spacing** and **Divisions** for the first and second axis.
  - Select **Fixed aspect ratio**, set the **Spacing** and **Divisions** for the first axis and then set the **Aspect ratio** and **Divisions** for the second axis.
4. Click **Close**.

**To create a fixed angular grid:**

1. From the **View** menu, select **Grid and Axis**.
2. Select **Advanced**.
3. From the **Grid type** pop-up menu, select **Two axis custom**.
4. Set the **Angle** of either axis.
5. Click **Close**.

## Presets

To make grid setup quick and easy, one of several grid presets can be chosen depending on how you plan to work (e.g., for UI design, image placement, etc.).

**To select a preset:**

1. From the **View** menu, select **Grid and Axis**.
2. From the **Preset** pop-up menu, select a preset.

> **Note:** Available grid presets will vary depending on the type of document units used. To use different grid presets, you will have to change document units.

**To customize a preset:**

1. From the **View** menu, select **Grid and Axis**.
2. Select a preset on which to base your new grid options.
3. Check individual options on/off to override the current preset's options.

The options will be in effect immediately.

**To save as a custom preset for future use:**

1. Click the **Options** menu adjacent to the **Preset** pop-up menu.
2. Select **Create preset**.

The custom preset is in effect immediately.

**To manage grid presets:**

1. On the **Grid and Axis** dialog, choose a preset or create your own.
2. Click **Panel Preferences**.
3. Select **Set as Default** or **Clear Default**, as required.

## About pixel grid

When working with images at large magnification levels, zooming in an undetermined amount, a pixel grid serves as a handy visual aid. Pixel art and working with object detail are just a couple of examples of its use. A different grid color can also aid work where there is little color variance in the image.

> **Note:** ![Force Pixel Alignment](../../assets/shared/ui/force_pixel_alignment.png) ![Move By Whole Pixels](../../assets/shared/ui/move_by_whole_pixels.png) Enabling **Snap to grid** option will not initiate snapping to the pixel grid. However, you can snap to it by turning **Force Pixel Alignment** on and **Move by Whole Pixels** off.

**To create a pixel grid:**

1. From the **View** menu, do one of the following:
  - Select **Show Pixel Grid**.
  - Select **Grid and Axis**. In the dialog, check **Show pixel grid**.
2. Optionally, for the latter option, modify **Pixel grid lines** color for better grid visibility.

> **Note:** ![Force Pixel Alignment](../../assets/shared/ui/force_pixel_alignment.png) Enable **Force Pixel Alignment** (Photo Persona) to ensure you are snapping to the pixel grid while working.

#### SEE ALSO:

- [Snapping](12-snapping.md)
- [Isometric and axonometric grids](04-grids/01-grids-axonometric.md)
- [Zooming](../04-get-started/09-zooming.md)
- [Zoom Tool](../20-tools/01-layout-tools/15-zoom-tool.md)
- [Document units](../04-get-started/07-document-units.md)
- [Preview mode](11-preview-mode.md)
