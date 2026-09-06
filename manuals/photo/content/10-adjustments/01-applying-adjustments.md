# Applying adjustments

There are a range of adjustments which can be applied to your photo as a new layer for creative or corrective purposes.

Adjustments are applied to your image from the **Adjustment** panel and most include customizable settings alongside general adjustment options. Once applied, they can be identified as both an adjustment and a specific adjustment type by using unique symbols.

![Adjustment layer type](../../assets/shared/adjustment_layertype.png)
*Curves adjustment layer indicating it is an adjustment (A) and a Curves adjustment type (B).*

**Available adjustments:**

- ![Black and white adjustment type](../../assets/shared/ui/black_and_white_adjustment_type.png)[Black & White](03-color-adjustments/02-adjustment-blackandwhite.md)
- ![brightness contrast adjustment type](../../assets/shared/ui/brightness_contrast_adjustment_type.png)[Brightness / Contrast](02-tonal-adjustments/01-adjustment-brightnesscontrast.md)
- ![channel mixer adjustment type](../../assets/shared/ui/channel_mixer_adjustment_type.png)[Channel Mixer](03-color-adjustments/03-adjustment-channelmixer.md)
- ![color balance adjustment type](../../assets/shared/ui/colour_balance_adjustment_type.png)[Color Balance](03-color-adjustments/04-adjustment-clrbalance.md)
- ![curves adjustment type](../../assets/shared/ui/curves_adjustment_type.png)[Curves](02-tonal-adjustments/02-adjustment-curves.md)
- ![exposure adjustment type](../../assets/shared/ui/exposure_adjustment_type.png)[Exposure](02-tonal-adjustments/03-adjustment-exposure.md)
- ![gradient map adjustment type](../../assets/shared/ui/gradient_map_adjustment_type.png)[Gradient Map](03-color-adjustments/05-adjustment-gradientmap.md)
- ![hsl adjustment type](../../assets/shared/ui/hsl_adjustment_type.png)[HSL](03-color-adjustments/01-adjustment-hsl.md)
- ![invert adjustment type](../../assets/shared/ui/invert_adjustment_type.png)[Invert](04-other-adjustments/02-adjustment-invert.md)
- ![lens filter adjustment type](../../assets/shared/ui/lense_filter_adjustment_type.png)[Lens Filter](03-color-adjustments/06-adjustment-lensfilter.md)
- ![levels adjustment type](../../assets/shared/ui/levels_adjustment_type.png)[Levels](02-tonal-adjustments/04-adjustment-levels.md)
- ![lut adjustment type](../../assets/shared/ui/lut_adjustment_type.png)[LUT](04-other-adjustments/01-adjustment-3dlut.md)
- ![normals adjustment type](../../assets/shared/ui/Normals_adjustment_type.png)[Normals](04-other-adjustments/03-adjustment-normals.md)
- ![ocio adjustment type](../../assets/shared/ui/ocio_adjustment_type.png)[OCIO (OpenColorIO)](03-color-adjustments/07-adjustment-ocio.md)
- ![posterize adjustment type](../../assets/shared/ui/posterise_adjustment_type.png)[Posterize](04-other-adjustments/04-adjustment-posterize.md)
- ![recolor adjustment type](../../assets/shared/ui/recolour_adjustment_type.png)[Recolor](03-color-adjustments/08-adjustment-reclr.md)
- ![selective color adjustment type](../../assets/shared/ui/selective_colour_adjustment_type.png)[Selective Color](03-color-adjustments/09-adjustment-selectiveclr.md)
- ![shadows highlight adjustment type](../../assets/shared/ui/shadows_highlight_adjustment_type.png)[Shadows / Highlights](02-tonal-adjustments/05-adjustment-shadowshighlights.md)
- ![soft proof adjustment type](../../assets/shared/ui/soft_proof_adjustment_type.png)[Soft Proof](04-other-adjustments/05-adjustment-softproof.md)
- ![split toning adjustment type](../../assets/shared/ui/split_toning_adjustment_type.png)[Split Toning](03-color-adjustments/10-adjustment-splittoning.md)
- ![threshold adjustment type](../../assets/shared/ui/threshold_adjustment_type.png)[Threshold](03-color-adjustments/11-adjustment-threshold.md)
- ![vibrance adjustment type](../../assets/shared/ui/vibrance_adjustment_type.png)[Vibrance](03-color-adjustments/12-adjustment-vibrance.md)
- ![white balance adjustment type](../../assets/shared/ui/white_balance_adjustment_type.png)[White Balance](03-color-adjustments/13-adjustment-whitebalance.md)

Adjustment layers only affect layers which are below them. Alternatively, you can make an adjustment a child of a layer (or layer group), thereby affecting that layer (or layer group) only.

Some adjustments (i.e., Curves, Levels, or Channel Mixer) can be made in any color space independently of the document color space.

> **Note:** There are additional adjustments available in **Develop Persona** which are arranged on various panels. For more information, see [Developing a raw image](../04-develop-persona-raw/01-developing-raw-images.md).

> **Tip:** For specific targeting of adjustments, [create a pixel selection](../08-selections/01-creating-pixel-selections/01-overview.md) before applying an adjustment layer. Only those pixels included in the selection are affected by the adjustment layer. (A [layer mask](../06-layers/12-layer-masks.md) is applied.) For more information, see the [Using adjustment layers](../06-layers/07-adjustment-layers.md) topic.

### Settings

The following general settings are available from all adjustment dialogs:

- **Add Preset**—adds the current adjustment settings as a preset for use with later images and projects.
- **Merge**—merges the current adjustment layer with the layer immediately below it in the layer order.
- **Delete**—closes the dialog and deletes the adjustment layer, removing the adjustment from the image.
- **Reset**—reverts all dialog settings to default.
- **Opacity**—how see-through the adjustment layer is.
- **Blend mode**—changes how the applied pixels interact with existing pixels on the layer below. Choose mode type from a pop-up menu.
- ![Blend Options](../../assets/shared/ui/cogicon.png) **Blend Options**—click to access a dialog for setting the blend ranges, blend gamma and antialiasing settings for the selected layer.

> **Note:** You can reset any adjustment setting back to its default by double-clicking on its slider handle.

> **Note:** Not all adjustments have a dedicated dialog or customizable settings.

**To apply an adjustment:**

1. On the **Adjustment** panel, select an adjustment.
2. Click one of the adjustment preset thumbnails. The adjustment is added directly above the selected layer, or at the top of the stack if no layer was selected.
3. If a dialog appears for the adjustment, follow the steps below:
  1. Adjust the settings in the dialog.
  2. (Optional) Click **Add Preset** to make your custom settings available in step 2 for future sessions.
  3. Close the dialog.

**To rename or delete a saved adjustment:**

- On the **Adjustment** panel, `Click`-click a custom adjustment, then select an option.

**To view an applied adjustment's settings:**

- On the **Layers** panel, double-click the adjustment layer's thumbnail.

**To reorder adjustment presets:**

1. On the **Adjustment** panel, select an adjustment.
2. Drag an adjustment preset thumbnail to move it to a different position.

**To apply an adjustment from the Layers panel:**

1. On the **Layers** panel, select a layer.
2. Click **Adjustments** and select an adjustment from the pop-up menu. The adjustment is added directly above the selected layer.
3. If a dialog appears for the adjustment, follow the steps below:
  1. Adjust the settings in the dialog.
  2. Close the dialog.

> **Note:** Adjustments are also available from the **Layer** menu's **New Adjustment Layer** submenu.

#### SEE ALSO:

- [Using adjustment layers](../06-layers/07-adjustment-layers.md)
- [Developing a raw image](../04-develop-persona-raw/01-developing-raw-images.md)
