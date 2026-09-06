# Crop Tool

The **Crop Tool** allows you to remove portions of your photo or image. Crops can be non-destructive or can resample, and can use specific aspect ratios as required.

### Settings

The following settings can be adjusted from the context toolbar:

- **Apply**—applies the crop to your image once you've defined the crop area (based on the positioned overlay).
- **Cancel**—exits the dialog without applying the crop to your image.
- ![Preset Manager](../../../assets/shared/ui/cogicon.png) **Presets**—opens a list of presets and also allows access to the **Preset manager**.
- **Mode**—sets the aspect ratio of the crop area. Select one of the following from the pop-up menu:
  - **Unconstrained**—Allows you to size the crop area freely.
  - **Original Ratio**—Retains your image's original aspect ratio.
  - **Custom Ratio**—Uses the adjacent input boxes to set the ratio—width in the left box, height in the right box. Can be saved as a preset.
  - **Resample**—Use the adjacent **Width** and **Height** settings to set dimensions for the crop area at your chosen **DPI** and you measurement **Units**.
- Crop dimension boxes—for **Custom Ratio** and **Resample** modes, sets the width and height, respectively.
- **Units**—sets the units used by the crop area.
- **DPI**—choose the DPI for resampling to unit measurements.
- **Crop**—lists the current pixel resolution based off the unit measurements and DPI value.
- **Rotate**—rotates the crop area by 180°.
- **Straighten**—switches to Straighten mode to align crooked photos horizontally or vertically.
- **Overlay**—offers various overlays for better photo composition.
- **Reset**—resets all settings to their defaults.
- **Darken**—renders areas outside of the crop boundary darker for easier previewing.
- **Reveal**—when checked, displays areas of the document outside of the current crop. Useful if you have already cropped the canvas and need to expand it again.

> **Note — Modifier keys:** When using the Vector Crop Tool, the following modifier keys can be used while applying a crop:
>
> - Holding down `Shift` while cropping in the **Unconstrained** mode constrains the current aspect ratio.
> - The left and right arrow s can be used to nudge the area in single-pixel increments. Holding down `Shift` while pressing the left and right arrow s nudges the crop area in 10-pixel increments.
> - The `Alt`  temporarily disables global snapping.
> - **macOS:** Holding down the `Cmd`  and dragging on the page (not using handles) toggles the crop area overlay and enters the **Straighten** mode. When pressed while cropping using one of the handles, the tool's bounding box allows to recompose the image around its center.
> - **Windows:** Holding down the `Ctrl` and dragging on the page (not one of the handles) toggles the crop area overlay and enters the **Straighten** mode. When pressed while cropping using one of the handles, the tool's bounding box allows to recompose the image around its center.
> - **macOS:** The `Ctrl`  allows the crop area to be rotated about its opposite handle.
> - **Windows:** Upon starting the rotation process, pressing the right mouse button lets you rotate the crop area around its opposite handle.
> - You can quickly toggle between overlay modes by pressing **O**.
>
> These modifiers can be used in combination.

#### SEE ALSO:

- [Cropping](../../05-sizing-cropping-and-warping/04-cropping-and-straightening.md)
- [Snapping](../../30-design-aids/11-snapping.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
