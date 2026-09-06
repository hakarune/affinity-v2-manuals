# Soft Proof adjustment

Preview the effect of creating an output for a specific color space or device.

![Before](../../assets/shared/adjustment_softproofing_before.jpg)
![After](../../assets/shared/adjustment_softproofing_after.jpg)
*Soft Proofing with a custom paper profile and Gamut Check enabled.*

This adjustment allows you to preview different output options for your publication. It can also be used creatively for tonal effects. As it behaves like a standard adjustment layer, it must be hidden or removed before exporting or sending to print, otherwise its effect will be included in the output.

![Adjustment](../../assets/shared/ui/adjustmentLayerIcon.png) Apply this adjustment via the **Adjustment** button on the **Layers** panel or via **Layer** > **New Adjustment**.

### Settings

The following settings can be adjusted in the dialog:

- **Proof Profile**—determines the color profile used. Select from the menu or use the up/down arrow keys to cycle through options.
- **Rendering Intent**—sets the visual purpose for applying the adjustment. Select from the pop-up menu.
- **Black point compensation**—when selected (default), the design's black point is adjusted to honor the current contrast within the current proof profile. If this option is off, the design's black point is not adjusted and image contrast may not be honored.
- **Gamut check**—when selected, RGB colors without a CMYK equivalent will display as gray.

#### SEE ALSO:

- [Applying adjustments](01-applying-adjustments.md)
- [Export](../14-publishing-and-sharing/02-export-as-graphic.md)
- [Print](../14-publishing-and-sharing/01-print.md)
