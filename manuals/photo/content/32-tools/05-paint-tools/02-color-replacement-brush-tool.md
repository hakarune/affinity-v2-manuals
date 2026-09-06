# Color Replacement Brush Tool

The **Color Replacement Brush Tool** works by replacing the color of pixels on the current layer with the Foreground color selected on the **Color** panel.

The pixels affected by the Color Replacement Brush are determined by the following:

- The color of the pixel under the tool when you click on your page.
- Whether the pixels are within the same selection area.
- The pixels are included in the painted stroke.
- The tool's **Tolerance** settings (see below).

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the [Brushes](../../23-painting-and-erasing/06-modifying-brushes.md) dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabilizer**—enables stroke stabilization using either a **Rope stabilizer** or **Window stabilizer** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Tolerance**—sets the range of pixels affected when a pixel is clicked. For lower tolerance settings, pixels must be very close in value to the clicked pixel. For higher tolerance settings, pixel color can vary widely from the clicked pixel.
- **Sample continuously**—if this option is off (default), the initial click position determines the reference color to be replaced. When selected, new reference colors are determined as the cursor moves.
- **Contiguous**—when selected (default), only adjacent qualifying pixels under the stroke are recolored. If this option is off, all qualifying pixels under the stroke are recolored, even if they are non-adjacent.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.

> **Note:** This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

#### SEE ALSO:

- [Paint Brush Tool](01-paint-brush-tool.md)
- [Pixel Tool](03-pixel-tool.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
