# Healing Brush Tool

The **Healing Brush Tool** enables you to repair and retouch unsightly areas of an image. It conveniently remembers last-used settings.

> **Tip:** The **Healing Brush Tool** can clone from other images (called Global Sources) using the [Sources panel](../../33-panels/24-sources-panel.md).

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the [Brushes](../../23-painting-and-erasing/06-modifying-brushes.md) dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabilizer**—enables stroke stabilization using either a **Rope stabilizer** or **Window stabilizer** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Aligned**—when selected, the origin of the sample remains a fixed distance from the pointer. If this option is off, the origin of the sample always returns to the sample location defined initially.
- **Source**—the source determines the layer(s) from which the pixels are sampled. Select from the pop-up menu.
- **Add Global Source**—sets the currently defined sample origin as a global source for use in other images. Remember to select a source using `Alt`-click first.
- **Rotation**—sets the degree of rotation applied to the sample. The result can be previewed inside the brush cursor. Type directly in the text box or drag the pop-up slider to set the value.
- **Scale**—sets the scale of the sample between 1% and 1000%. Type directly in the text box or drag the pop-up slider to set the value. The result can be previewed inside the brush cursor.
- **Flip**—allows for horizontal and vertical flipping of the resulting healing area relative to the sampled area. Choose horizontal, vertical or both directions from a pop-up menu.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.

> **Tip:** The **Rotation** setting can be adjusted using the left and right arrow keys. The **Scale** setting can be adjusted using the up and down arrow keys.

> **Note:** This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

#### SEE ALSO:

- [Cloning and healing](../../09-retouching/04-cloning-and-healing.md)
- [Patch Tool](11-patch-tool.md)
- [Blemish Removal Tool](12-blemish-removal-tool.md)
- [Inpainting Brush Tool](13-inpainting-brush-tool.md)
- [Clone Brush Tool](04-clone-brush-tool.md)
- [Sources panel](../../33-panels/24-sources-panel.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
