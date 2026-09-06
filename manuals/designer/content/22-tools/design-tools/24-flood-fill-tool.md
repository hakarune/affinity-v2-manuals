# ![Pixel Persona only](../../../assets/shared/ui/pixelpersonaonly.png)

 ![Flood Fill Tool](../../../assets/shared/ui/flood_fill_tool.png)

 Flood Fill Tool

The **Flood Fill Tool** allows you to fill in areas of your page, selection, or object with a single click.

The **Flood Fill Tool** works by replacing the colour of pixels on the current layer with the Fill colour set on the **Colour** panel. The pixels affected are determined by the following:

- The colour of the pixel under the tool when you click on your page.
- Whether the pixels are within the same selection area.
- The pixels are directly connected to the clicked pixel or any others that are affected.
- The tool's **Tolerance** and **Blend Mode** settings (see below).

### Settings

The following settings can be adjusted from the context toolbar:

- **Tolerance**—sets the range of pixels affected (filled) when a pixel is clicked. For lower tolerance settings, pixels must be very close in value to the clicked pixel. For higher tolerance settings, pixel colour can vary widely from the clicked pixel. Clicking and dragging on a pixel will adjust the tolerance.
- **Contiguous**—if enabled, the flood will only be applied to affected pixels that are in the same area of the page. If disabled, the flood will be applied to all the pixels that match the tolerance setting regardless of where they are on the page.
- Blend mode—determines how the Fill colour and pixels in the filled area are combined, like when [blending the contents of two or more layers](../../07-layers/07-layer-blending.md). When set to **Normal**, the Fill colour simply replaces pixel colours in the filled area.
- **Source**—choose whether the tool determines the area to be filled by inspecting pixels in the current layer, the current layer and all those below it, or only layers beneath the current one.

#### SEE ALSO:

- [Fill Tool](10-fill-tool.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
