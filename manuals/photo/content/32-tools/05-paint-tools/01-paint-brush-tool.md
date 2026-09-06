# Paint Brush Tool

The Paint Brush Tool lays down pixels on the page, creating strokes with antialiased edges. This creates a natural transition between the stroke and the surrounding pixels.

Its variable width lines can be controlled either by velocity—most useful when drawing with a mouse—or by pressure—for use when drawing with a pressure-sensitive device.

## About the Paint Brush Tool

Other brush-based tools use similar settings to control the appearance of the applied pixels, although there may be slight variations.

Most brushes use a soft, round brush as their default. Alternative styles can be selected from the **Brushes** panel.

> **Tip:** With any brush tool selected in Photo Persona, you can quickly change the opacity of your brush using numerical keys. For more information, see the [Painting brush strokes](../../23-painting-and-erasing/01-painting-brush-strokes.md) topic.

When using the **Paint Brush Tool** on a RAW or image layer, a new nested pixel layer is created with the strokes applied onto it. This aids non-destructive, layer-based workflows whereby the newly created layer can be switched off from view to investigate the effects of painting quickly. This also aids layer data management as the original image or RAW layer is not rasterized.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the pixel brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the pixel brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the Brushes dialog to access advanced brush settings.
- **Force pressure**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabilizer**—enables stroke stabilization using one of two modes:
  - ![Rope stabilization mode](../../../assets/shared/ui/stabiliser_rope.png) **Rope mode**—drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope *Length* (radius) values by redirecting the slackened rope.
  - ![Window stabilization mode](../../../assets/shared/ui/stabiliser_window.png) **Window mode**—smoothes the stroke by averaging sampled input positions within a *Window* whose size is configurable.
- **Symmetry**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The center axis point can be repositioned by click-dragging it.
- **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
- **Lock**—when checked, prevents the symmetry line from being moved.
- **Blend Mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.
- **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions.

> **Note:** The tool can be associated with a particular brush when editing it in the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

#### SEE ALSO:

- [Painting brush strokes](../../23-painting-and-erasing/01-painting-brush-strokes.md)
- [Pen Tool](../02-vector-line-tools/01-pen-tool.md)
- [Node Tool](../02-vector-line-tools/02-node-tool.md)
- [Brushes panel](../../33-panels/05-brushes-panel.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
