# Pixel Tool

The **Pixel Tool** draws pixel-aligned, hard-edged lines. This is in contrast to the **Paint Brush Tool** which may have a slight pixel variance due to its antialiasing.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the line thickness in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the [Brushes](../../23-painting-and-erasing/06-modifying-brushes.md) dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabilizer**—enables stroke stabilization using either a **Rope stabilizer** or **Window stabilizer** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Symmetry**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The center axis point can be repositioned by click-dragging it.
- **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
- **Lock**—when checked, prevents the symmetry line from being moved.
- **Blend mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
- **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions.
- **Alternate**—changes the behavior of the alternate modifier (`Cmd`-Click):
  - **Erase**—erases created pixels.
  - **Background color**—temporarily switches to the background color in the swatch.
  - **Undo from snapshot**—paints-in from a chosen snapshot (see [Using snapshots](../../30-design-aids/04-using-snapshots.md)).

> **Note:** You can erase pixel brush strokes while the `Cmd`  is pressed.

> **Note:** This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

#### SEE ALSO:

- [Pixel-aligned painting](../../23-painting-and-erasing/03-pixel-aligned-painting.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
