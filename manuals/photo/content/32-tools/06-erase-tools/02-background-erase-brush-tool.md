# Background Erase Brush Tool

With the **Background Erase Brush Tool**, you can erase pixels of a similar color. This makes it useful for tasks such as erasing the background while leaving the foreground intact.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. 100% opacity erases pixels completely on the first pass. A lower opacity only partially erases the pixels.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **More**—click to display the [Brushes](../../23-painting-and-erasing/06-modifying-brushes.md) dialog to access advanced brush settings.
- **Stabilizer**—enables stroke stabilization using either a **Rope stabilizer** or **Window stabilizer** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Tolerance**—how dissimilar the pixels can be compared to the sampled pixel for the pixels to be erased. A low percentage affects only pixels very similar to the sampled pixel
- **Sample continuously**—if this option is off (default), samples the color only once on the first click. When selected, samples color continuously as you drag.
- **Contiguous**—when selected (default), affects neighboring pixels as well as the sampled pixel color. If this option is off, affects only the selected pixel color.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.

> **Note:** This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

#### SEE ALSO:

- [Erasing](../../23-painting-and-erasing/02-erasing.md)
- [Erase Brush Tool](01-erase-brush-tool.md)
- [Flood Erase Tool](03-flood-erase-tool.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
