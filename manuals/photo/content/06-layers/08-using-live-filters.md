# Using live filters

Live filters allow you to apply filter effects such as blurring, sharpening, noise and distortion non-destructively, meaning you can modify or remove the effects without having to use the **History** panel to undo other operations on your work.

![Before](../../assets/shared/live_filter_before.png)
![After](../../assets/shared/live_filter_after.png)
*Using the Motion Blur live filter to imitate motion in the scene.*

## About live filters

Live filters provide a way of applying creative effects to your images while retaining the ability to modify the effect settings or remove the effect altogether. The filter is added to the active layer, similar to applying [Adjustment Layers](07-adjustment-layers.md).

Once applied, they can be identified as both a filter and a specific live filter type by using unique symbols.

![Live filter layer type](../../assets/shared/livefilter_layertype.png)
*Perspective Live filter layer (named 01) indicating it is a filter (A) and a Perspective filter type (B).*

**Available live filters:**

- **Blur**
  - ![Gaussian blur live filter type](../../assets/shared/ui/gaussian_blur_live_filter.png) [Gaussian Blur](../11-filters-and-effects/02-blur-filters/08-filter-gaussianblur.md)
  - ![Box blur live filter type](../../assets/shared/ui/box_blur_live_filter.png) [Box Blur](../11-filters-and-effects/02-blur-filters/05-filter-boxblur.md)
  - ![Median blur live filter type](../../assets/shared/ui/median_blur_live_filter.png) [Median Blur](../11-filters-and-effects/02-blur-filters/11-filter-medianblur.md)
  - ![Bilateral blur live filter type](../../assets/shared/ui/bilateral_blur_live_filter.png) [Bilateral Blur](../11-filters-and-effects/02-blur-filters/04-filter-bilateralblur.md)
  - ![Motion blur live filter type](../../assets/shared/ui/motion_blur_live_filter.png) [Motion Blur](../11-filters-and-effects/02-blur-filters/13-filter-motionblur.md)
  - ![Radial blur live filter type](../../assets/shared/ui/radial_blur_live_filter.png) [Radial Blur](../11-filters-and-effects/02-blur-filters/14-filter-radialblur.md)
  - ![Lens blur live filter type](../../assets/shared/ui/lens_blur_live_filter.png) [Lens Blur](../11-filters-and-effects/02-blur-filters/09-filter-lensblur.md)
  - ![Depth of Field blur live filter type](../../assets/shared/ui/dof_blur_live_filter.png) [Depth Of Field Blur](../11-filters-and-effects/02-blur-filters/01-filter-dofblur.md)
  - ![Field blur live filter type](../../assets/shared/ui/field_blur_live_filter.png) [Field Blur](../11-filters-and-effects/02-blur-filters/02-filter-fieldblur.md)
  - ![Diffuse glow live filter type](../../assets/shared/ui/diffuse_glow_live_filter.png) [Diffuse Glow](../11-filters-and-effects/02-blur-filters/07-filter-diffuseglow.md)
  - ![Maximum blur live filter type](../../assets/shared/ui/maximum_blur_live_filter.png) [Maximum Blur](../11-filters-and-effects/02-blur-filters/10-filter-maximumblur.md)
  - ![Minimum blur live filter type](../../assets/shared/ui/median_blur_live_filter.png) [Minimum Blur](../11-filters-and-effects/02-blur-filters/12-filter-minimumblur.md)
- **Sharpen**
  - ![Clarity live filter type](../../assets/shared/ui/clarity_live_filter.png) [Clarity](../11-filters-and-effects/09-shadows-highlights/01-filter-clarity.md)
  - ![Unsharp mask live filter type](../../assets/shared/ui/Unsharp_mask_live_filter.png) [Unsharp Mask](../11-filters-and-effects/07-sharpen-filters/02-filter-unsharpmask.md)
  - ![High pass live filter type](../../assets/shared/ui/high_pass_live_filter.png) [High Pass](../11-filters-and-effects/07-sharpen-filters/01-filter-highpass.md)
- **Distort**
  - ![Ripple live filter type](../../assets/shared/ui/ripple_live_filter.png) [Ripple](../11-filters-and-effects/04-distortion-filters/15-filter-ripple.md)
  - ![Twirl live filter type](../../assets/shared/ui/twirl_live_filter.png) [Twirl](../11-filters-and-effects/04-distortion-filters/18-filter-twirl.md)
  - ![Spherical live filter type](../../assets/shared/ui/sphere_live_filter.png) [Spherical](../11-filters-and-effects/04-distortion-filters/17-filter-spherical.md)
  - ![Displace live filter type](../../assets/shared/ui/displacement_live_filter.png) [Displace](../11-filters-and-effects/04-distortion-filters/03-filter-displace.md)
  - ![Pinch/Punch live filter type](../../assets/shared/ui/pinch_punch_live_filter.png) [Pinch/Punch](../11-filters-and-effects/04-distortion-filters/11-filter-pinchpunch.md)
  - ![Lens distortion live filter type](../../assets/shared/ui/lens_distortion_live_filter.png) [Lens Distortion](../11-filters-and-effects/04-distortion-filters/06-filter-lensdistortion.md)
  - ![Perspective live filter type](../../assets/shared/ui/perspective_live_filter.png) [Perspective](../11-filters-and-effects/04-distortion-filters/10-filter-perspective.md)
  - ![Liquify live filter type](../../assets/shared/ui/liquify_live_filter.png) [Liquify](../11-filters-and-effects/04-distortion-filters/07-filter-liquify.md)
  - ![Mesh Warp live filter type](../../assets/shared/ui/mesh_warp_live_filter.png) [Mesh Warp](../11-filters-and-effects/04-distortion-filters/08-filter-meshwarp.md)
- **Noise**
  - ![Denoise live filter type](../../assets/shared/ui/denoise_live_filter.png) [Denoise](../11-filters-and-effects/06-noise-filters/03-filter-denoise.md)
  - ![Add noise live filter type](../../assets/shared/ui/noise_live_filter.png) [Add Noise](../11-filters-and-effects/06-noise-filters/01-filter-addnoise.md)
  - ![Diffuse live filter type](../../assets/shared/ui/diffuse_live_filter.png) [Diffuse](../11-filters-and-effects/06-noise-filters/04-filter-diffuse.md)
  - ![Dust & Scratches live filter type](../../assets/shared/ui/dust_and_scratches_live_filter.png) [Dust & Scratches](../11-filters-and-effects/06-noise-filters/05-filter-dustscratches.md)
- **Colors**
  - ![Vignette live filter type](../../assets/shared/ui/vignette_live_filter.png) [Vignette](../11-filters-and-effects/03-color-filters/14-filter-vignette.md)
  - ![Defringe live filter type](../../assets/shared/ui/defringe_live_filter.png) [Defringe](../11-filters-and-effects/03-color-filters/02-filter-defringe.md)
  - ![Voroni live filter type](../../assets/shared/ui/zoom_blur_live_filter.png) [Voronoi](../11-filters-and-effects/03-color-filters/15-filter-voronoi.md)
  - ![Halftone live filter type](../../assets/shared/ui/halftone_live_filter.png) [Halftone](../11-filters-and-effects/03-color-filters/06-filter-halftone.md)
  - ![Procedural texture live filter type](../../assets/shared/ui/procedural_texture_live_filter.png) [Procedural Texture](../11-filters-and-effects/03-color-filters/09-filter-proceduraltexture.md)
- **Lighting**
  - ![Lighting live filter type](../../assets/shared/ui/lighting_live_filter.png) [Lighting](../11-filters-and-effects/10-lighting.md)
  - ![Shadows / highlights live filter type](../../assets/shared/ui/shadows_highlight_live_filter.png) [Shadows / Highlights](../11-filters-and-effects/09-shadows-highlights.md)

**To create a new live filter:**

Do one of the following:

- From the **Layers** panel, click **Live Filters** and select a filter from the list.
- From the **Layer** menu, select **New Live Filter Layer**.

**To modify, merge or delete a live filter:**

1. On the **Layers** panel, double-click the live filter that you want to modify.
2. Adjust the settings in the dialog; the changes will be applied in real time.
3. Close the dialog to apply the changes, **Merge** to apply the changes and merge the adjustment with the layer beneath, or **Delete** to remove the filter layer entirely.

**To move a live filter:**

Do one of the following:

- Drag the live filter to the top of the **Layers** panel so it affects all layers below it.
- Drag the live filter above or below layers to affect more or fewer layers in the project.
- Drag the live filter onto a layer or group to apply the filter to that layer or group only.

**To mask a live filter:**

1. On the **Layers** panel, select the live filter.
2. Do any of the following:
  - To 'erase' from the mask, paint with the **Erase Brush Tool**.
  - To 'restore' the mask, select the **Paint Brush Tool** and paint.
  - To apply a gradient mask, select the **Gradient Tool** from the **Tools** panel and drag across the layer. Adjust the gradient colors from the settings.

> **Note:** If you have a [pixel selection](../08-selections/01-creating-pixel-selections/01-overview.md) in place when you add a live filter, the area is automatically masked.

#### SEE ALSO:

- [Applying filters](../11-filters-and-effects/01-applying-filters.md)
- [Layer masks](12-layer-masks.md)
- [Creating pixel selections](../08-selections/01-creating-pixel-selections/01-overview.md)
- [Settings (or Preferences)](../37-settings-preferences/01-settings-preferences.md)
