# Using adjustment layers

Use adjustment layers to apply an adjustment to a specific layer, group, object or an image on your page. This is carried out non-destructively (i.e., without permanently affecting the original layer or object).

![Before](../../assets/shared/adjustment_blackandwhite_before.jpg)
![After](../../assets/shared/adjustment_blackandwhite_after.jpg)
*Black and White adjustment applied to placed image.*

## About adjustment layers

Adjustments are applied from the **Layers** panel and most include customizable settings alongside general adjustment options. Once applied, they can be identified as both an adjustment and a specific adjustment type by using unique symbols.

![Adjustment layer type](../../assets/shared/adjustment_layertype.png)
*Curves adjustment layer indicating it is an adjustment (A) and a Curves adjustment type (B).*

There may be times that you only want to apply an adjustment layer to either a single layer (e.g., a placed image) or a group of layers. This is easily achieved by [clipping](11-layer-clipping.md).

**Available adjustments:**

- ![Black and white adjustment type](../../assets/shared/ui/black_and_white_adjustment_type.png)[Black & White](../18-adjustments/02-black-and-white-adjustment.md)
- ![brightness contrast adjustment type](../../assets/shared/ui/brightness_contrast_adjustment_type.png)[Brightness / Contrast](../18-adjustments/03-brightness-and-contrast-adjustment.md)
- ![channel mixer adjustment type](../../assets/shared/ui/channel_mixer_adjustment_type.png)[Channel Mixer](../18-adjustments/04-channel-mixer-adjustment.md)
- ![color balance adjustment type](../../assets/shared/ui/colour_balance_adjustment_type.png)[Color Balance](../18-adjustments/05-color-balance-adjustment.md)
- ![curves adjustment type](../../assets/shared/ui/curves_adjustment_type.png)[Curves](../18-adjustments/06-curves-adjustment.md)
- ![exposure adjustment type](../../assets/shared/ui/exposure_adjustment_type.png)[Exposure](../18-adjustments/07-exposure-adjustment.md)
- ![gradient map adjustment type](../../assets/shared/ui/gradient_map_adjustment_type.png)[Gradient Map](../18-adjustments/08-gradient-map-adjustment.md)
- ![hsl adjustment type](../../assets/shared/ui/hsl_adjustment_type.png)[HSL](../18-adjustments/09-hsl-adjustment.md)
- ![invert adjustment type](../../assets/shared/ui/invert_adjustment_type.png)[Invert](../18-adjustments/10-invert-adjustment.md)
- ![lens filter adjustment type](../../assets/shared/ui/lense_filter_adjustment_type.png)[Lens Filter](../18-adjustments/11-lens-filter-adjustment.md)
- ![levels adjustment type](../../assets/shared/ui/levels_adjustment_type.png)[Levels](../18-adjustments/12-levels-adjustment.md)
- ![lut adjustment type](../../assets/shared/ui/lut_adjustment_type.png)[LUT](../18-adjustments/13-lut-adjustment.md)
- ![ocio adjustment type](../../assets/shared/ui/ocio_adjustment_type.png)[OCIO (OpenColorIO)](../18-adjustments/14-opencolorio-adjustment.md)
- ![Posterize adjustment type](../../assets/shared/ui/posterise_adjustment_type.png)[Posterize](../18-adjustments/15-posterize-adjustment.md)
- ![recolor adjustment type](../../assets/shared/ui/recolour_adjustment_type.png)[Recolor](../18-adjustments/16-recolor-adjustment.md)
- ![selective color adjustment type](../../assets/shared/ui/selective_colour_adjustment_type.png)[Selective Color](../18-adjustments/17-selective-color-adjustment.md)
- ![soft proof adjustment type](../../assets/shared/ui/shadows_highlight_adjustment_type.png)[Shadows / Highlights](../18-adjustments/18-shadows-highlights-adjustment.md)
- ![shadows highlight adjustment type](../../assets/shared/ui/soft_proof_adjustment_type.png)[Soft Proof](../18-adjustments/19-soft-proof-adjustment.md)
- ![split toning adjustment type](../../assets/shared/ui/split_toning_adjustment_type.png)[Split Toning](../18-adjustments/20-split-toning-adjustment.md)
- ![threshold adjustment type](../../assets/shared/ui/threshold_adjustment_type.png)[Threshold](../18-adjustments/21-threshold-adjustment.md)
- ![vibrance adjustment type](../../assets/shared/ui/vibrance_adjustment_type.png)[Vibrance](../18-adjustments/22-vibrance-adjustment.md)
- ![White balance adjustment type](../../assets/shared/ui/white_balance_adjustment_type.png)[White Balance](../18-adjustments/23-white-balance-adjustment.md)

When an item is selected, the adjustment layer is applied to just that item, i.e. it is [clipped](11-layer-clipping.md). With no selection in place, the adjustment is applied to the entire spread.

**To apply an adjustment:**

1. On the **Layers** panel, do one of the following:
  - Select a layer to add the adjustment as a child of the layer. It will affect all objects on the selected layer.
  - Select an object, group or image to add the adjustment to the item, affecting just that item only.
  - Deselect all items to add the adjustment at the top of the layer stack, applying the adjustment to all items below it (the entire spread).
2. Click **Adjustments** and select an adjustment from the pop-up menu.
3. If a dialog appears for the adjustment, follow the steps below:
  1. Adjust the settings in the dialog.
  2. Click **Close**.

**To modify, merge or delete an adjustment layer:**

1. In the **Layers** panel, double-click the adjustment layer that you want to modify.
2. Adjust the settings in the dialog.
3. Click **Close** to apply the changes, **Merge** to apply the changes and merge the adjustment with the layer beneath, or **Delete** to remove the adjustment layer entirely.

**To move an adjustment layer:**

On the **Layers** panel, do one of the following:

- Drag the adjustment to the top of the panel so it affects all layers below it.
- Drag the adjustment above or below objects within a layer to affect more or fewer objects on the layer.
- Drag the adjustment onto an object to make it a child of that object and confine its effect to that object only.

#### SEE ALSO:

- [Applying adjustments](../18-adjustments/01-applying-adjustments.md)
