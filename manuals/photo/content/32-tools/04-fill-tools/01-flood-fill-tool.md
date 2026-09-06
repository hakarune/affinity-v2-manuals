# Flood Fill Tool

The **Flood Fill Tool** allows you to fill in areas of your page, selection, or object with a single click.

The **Flood Fill Tool** works by replacing the color of pixels on the current layer with the Fill color set on the Color panel. The pixels affected are determined by the following:

- The color of the pixel under the tool when you click on your page.
- Whether the pixels are within the same selection area.
- The pixels are directly connected to the clicked pixel or any others that are affected.
- The tool's **Tolerance** and **Blend Mode** settings (see below).

### Settings

The following settings can be adjusted from the context toolbar:

- **Tolerance**—sets the range of pixels affected (filled) when a pixel is clicked. For lower tolerance settings, pixels must be very close in value to the clicked pixel. For higher tolerance settings, pixel color can vary widely from the clicked pixel.
- **Contiguous**—if enabled, the flood will only be applied to affected pixels that are in the same area of the image. If disabled, the flood will be applied to all the pixels that match the tolerance setting regardless of where they are in the image.
- Blend mode—determines how the Fill color and pixels in the filled area are combined, like when [blending the contents of two or more layers](../../06-layers/05-layer-blending.md). When set to **Normal**, the Fill color simply replaces pixel colors in the filled area.
- **Source**—choose whether the tool determines the area to be filled by inspecting pixels in the current layer, the current layer and all those below it, or only layers beneath the current one.

#### SEE ALSO:

- [Flood Erase Tool](../06-erase-tools/03-flood-erase-tool.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
