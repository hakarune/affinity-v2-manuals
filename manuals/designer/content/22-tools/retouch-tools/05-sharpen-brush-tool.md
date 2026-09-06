# ![Pixel Persona only](../../../assets/shared/ui/pixelpersonaonly.png)

 ![Sharpen Brush Tool](../../../assets/shared/ui/sharpen_brush_tool.png)

 Sharpen Brush Tool

Sharpening increases the contrast of neighbouring pixels. The **Sharpen Brush Tool** gives you full control over the areas that are sharpened and has a cumulative affect. You can easily apply clarity and unsharp mask sharpening selectively with a few strokes of a brush!

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the [Brushes](../../11-pixel-painting/02-modifying-pixel-brushes.md) dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabiliser**—enables stroke stabilisation using either a **Rope stabiliser** or **Window stabiliser** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Symmetry**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The centre axis point can be repositioned by click-dragging it.
- **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
- **Lock**—when checked, prevents the symmetry line from being moved.
- **Mode**—determines the sharpening effect to be applied. Select from the pop-up menu.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolour effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.

### About the sharpening modes

The three modes available from the context toolbar have slightly different effects on the underlying pixels.

- **Clarity**—increases local contrast.
- **Unsharp Mask**—increases contrast of edge pixels.
- **Harsh**—increases contrast on all pixels.

> **Tip:** When using this brush you'll get the best results by using either low opacity or flow settings and then gradually building up the effect.

> **Tip:** For a blur effect while the tool is still active, press the `Alt`  as you paint.

#### SEE ALSO:

- [Paint Brush Tool](../design-tools/21-paint-brush-tool.md)
- [Painting pixel brush strokes](../../11-pixel-painting/01-painting-pixel-brush-strokes.md)
- [Blur Brush Tool](04-blur-brush-tool.md)
