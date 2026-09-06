# ![Pixel Persona only](../../../assets/shared/ui/pixelpersonaonly.png)

 ![Pixel Tool](../../../assets/shared/ui/pixel_tool.png)

 Pixel Tool

The **Pixel Tool** draws pixel-aligned, hard-edged lines. This is in contrast to the **Paint Brush Tool** which may have a slight pixel variance due to its antialiasing.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the line thickness in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the [Brushes](../../11-pixel-painting/02-modifying-pixel-brushes.md) dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush stroke size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabiliser**—enables stroke stabilisation using either a **Rope stabiliser** or **Window stabiliser** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Blend mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
- **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions.
- **Alternate**—changes the behaviour of the alternate modifier (`Cmd`-Click):
   - **Erase**—erases created pixels.
  - **Background colour**—temporarily switches to the background colour in the swatch.
  - **Undo from snapshot**—paints-in from a chosen snapshot (see [Using snapshots](../../17-design-aids/16-using-snapshots.md)).

> **Note:** ### Modifier keys
>
>
> As you paint pixel strokes, the following modifier key can be used:
>
>
> - When pressed, the `Cmd`  alters pixel strokes using the **Alternate** setting that has been selected (this is set to **Erase** by default).

#### SEE ALSO:

- [Paint Brush Tool](21-paint-brush-tool.md)
- [Painting pixel brush strokes](../../11-pixel-painting/01-painting-pixel-brush-strokes.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
