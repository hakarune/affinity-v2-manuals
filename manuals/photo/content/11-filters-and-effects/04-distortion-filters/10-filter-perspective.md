# Perspective

The Perspective filter can be used to either correct converging perspective lines caused by lens distortion, or to apply perspective for a creative effect.

Lens distortion can often cause the perspective of a photo to be out, creating the appearance that lines are not vertical or horizontal when they should be.

![Before](../../../assets/shared/tool_perspective_before.jpg)
![After](../../../assets/shared/tool_perspective_after.jpg)
*Using the Perspective Tool to alter the appearance of a building/structure.*

## About the Perspective filter

The Perspective filter can be adjusted in single or dual plane mode, if applied via the **Filters** menu (**Distort** category). If using the [non-destructive, live filter](../../06-layers/08-using-live-filters.md), only single plane mode is available.

The live filter can be accessed via the **Layer** menu, from the **New Live Filter Layer** category.

### Settings

The following settings can be adjusted in the filter dialog:

- **Planes**—the initial grid layout options. Select from the pop-up menu.
- **Mode**—the preview options. Select from the pop-up menu.
  - **Source**—the image remains static as the perspective box is positioned. When the perspective filter is applied, the image is stretched and cropped to the original canvas size.
  - **Destination**—the image is directly linked to the perspective box and transforms with the box as the anchor points are dragged.
- **Show grid**—when selected, a grid is displayed between anchor points and lines. If this option is off, only anchor points and lines display.
- **Autoclip**—(Available in Dual Plane mode) Specifies whether or not to alter the image beyond the boundaries of the perspective grid points. If disabled, the image will look continuous; if enabled, the image will have visible seams where the perspective tool has been applied that can then be retouched.
- ![Rotate anti-clockwise](../../../assets/shared/ui/rotate_anti_clockwise.png) ![Rotate clockwise](../../../assets/shared/ui/rotate_clockwise.png) **Rotate clockwise** / **Rotate anti-clockwise**—rotates the image right or left in 90° increments.
- **Select Destination**—alters pixel selection to the whole document if no pixel selection has been performed. If however an area of an image has been targeted using any of the pixel selection tools, choosing this option will restrict the effect of the filter (e.g. rotation) to the specified region. This option is only available when applying Perspective as a destructive filter.
- ![No split view](../../../assets/shared/ui/standard_view.png) ![Split view](../../../assets/shared/ui/split_view.png) ![Mirror view](../../../assets/shared/ui/mirror_view.png) **No split view** / **Split view** / **Mirror view**—by default, your image shows the current perspective applied. 'Split view' offers the adjusted and original images simultaneously with a sliding divider which can be repositioned and shows 'Before' and 'After'; 'Mirror view' is as for Split view but the 'Before' and 'After' panes show the entire images side by side, without the ability to slide the divider.

> **Note:**
>
> **Select Destination** and **Autoclip** options aren't available when Perspective is applied via the **New Live Filter Layer** since the document can be changed at any point in time.

> **Tip:**
>
> **macOS:** To access the filter quickly, use the `Cmd` + `T` keyboard shortcuts combination.
>
> **Windows:** To access the filter quickly, use the `Cmd`+`T` keyboard shortcuts combination.

#### SEE ALSO:

- [Using live filters](../../06-layers/08-using-live-filters.md)
- [Applying filters](../01-applying-filters.md)
- [Perspective Tool](../../05-sizing-cropping-and-warping/07-perspective.md)
