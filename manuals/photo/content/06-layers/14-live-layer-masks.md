# Live layer masks

Live layer mask are non-destructive masks, based on hue, luminosity and frequency, that update automatically based on the properties of the underlying image.

![Before](../../assets/shared/live_hue_range_mask_before.jpg)
![After](../../assets/shared/live_hue_range_mask_after.jpg)
*Vibrance Adjustment added onto a live Hue Range Mask targeting warm tones.*

## About Live layer masks

Live masks are generated automatically from your image, i.e. they can detect and mask image information that is common to all images, e.g. color (hue), luminosity or frequencies. Compare this to traditional masks which are manually created from drawn pixel selections or Paint Brush tools, and are inherently tied to an image's subject matter.

Live layer masks, like Live filters, are non-destructive so can be edited at any later date, either for fine-tuning or complete reconfiguration. They possess configurable settings for initial set up or subsequent fine-tuning.

All live masks can be inverted, have mask blurring applied and operate independently of the pixel layer.

The following live masks are supported:

- **Live Hue Range mask**—targets a specific hue range in your image to be used as the mask.
- **Live Luminosity Range mask**—uses a graph to specify a luminosity mask that can be used to isolate shadows, midtones or highlights in tonal adjustments. It can also be used to blend bracketed images together, offering greater control than performing an automatic HDR merge.
- **Live Band-pass mask**—creates a mask based on a configurable frequency band range that focuses on the edges in your image. This mask type is useful for retouchers when applied to sharpening filters (effectively offering a live frequency separation layer), but also for artistic effects when applied to, e.g. blur filters.

As live masks are not tied to specific imagery, they are completely transferable to other image or adjustment layers.

**To create a live mask:**

1. On the **Layers** panel, select the layer to target.
2. Do one of the following:
  - On the **Layer** top menu, select an option from the **New Live Mask Layer** submenu.
  - **macOS:** ![Mask Layer](../../assets/shared/ui/add_mask_layer.png) On the **Layers** panel, `Alt`-click **Mask Layer** to reveal the options, then select the required mask.
  - **Windows:** ![Mask Layer](../../assets/shared/ui/add_mask_layer.png) On the **Layers** panel, `Click`-click **Mask Layer** to reveal the options, then select the required mask.
3. On the Settings pane, configure the mask.

Once created, the mask can be moved to anywhere within a layer stack and can have adjustment or filter layers applied to it (or the mask can be applied to an adjustment or filter); you can also just paint on the automatically generated mask.

**To edit a live mask:**

- On the **Layers** panel, click the live mask's thumbnail, then edit the mask's settings via the dialog.

#### SEE ALSO:

- [Live Hue Range Mask](14-live-layer-masks/02-mask-livehuerange.md)
- [Live Luminosity Range Mask](14-live-layer-masks/03-mask-liveluminosityrange.md)
- [Live Band-pass Mask](14-live-layer-masks/01-mask-livebandpass.md)
- [Using adjustment layers](07-adjustment-layers.md)
- [Applying filters](../11-filters-and-effects/01-applying-filters.md)
