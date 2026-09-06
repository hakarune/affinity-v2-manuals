# ![Pixel Persona only](../../../assets/shared/ui/pixelpersonaonly.png)

 ![Paint Brush Tool](../../../assets/shared/ui/paint_brush_tool.png)

 Paint Brush Tool

The **Paint Brush Tool** lays down pixels on the page, creating strokes with antialiased edges. This creates a natural transition between the stroke and the surrounding pixels.

Its variable width lines can be controlled either by velocity—most useful when drawing with a mouse—or by pressure—for use when drawing with a pressure-sensitive device.

Other brush-based tools in Pixel Persona use similar settings to control the appearance of the applied pixels, although there may be slight variations.

Most brushes use a soft, round nozzle as their default. Alternative styles can be selected from the **Brushes** panel.

> **Tip:** With any brush tool selected, you can quickly decrease or increase the size (width) of your brush by holding `Ctrl` and `Alt` then dragging left or right, respectively. If the brush tool has a hardness attribute, this can be adjusted in a similar way by holding `Ctrl` and `Alt` then dragging up or down.
>
>
> With any brush tool selected, you can quickly decrease or increase the size (width) of your brush by holding `Cmd` and `Alt` then dragging left or right, respectively. If the brush tool has a hardness attribute, this can be adjusted in a similar way by holding `Cmd` and `Alt` then dragging up or down.

> **Tip:** With any brush tool selected in Pixel Persona, you can quickly change the opacity of your brush using numerical keys. For more information, see the [Transparency](../../06-colour/13-transparency.md) topic.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the pixel brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the pixel brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the Brushes dialog to access advanced brush settings.
- **Force pressure**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabiliser**—enables stroke stabilisation using one of two modes:
   - ![Rope stabilisation mode](../../../assets/shared/ui/stabiliser_rope.png)

     **Rope mode**—drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope *Length* (radius) values by redirecting the slackened rope.
  - ![Window stabilisation mode](../../../assets/shared/ui/stabiliser_window.png)

     **Window mode**—smoothes the stroke by averaging sampled input positions within a *Window* whose size is configurable.
- **Symmetry**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The centre axis point can be repositioned by click-dragging it.
- **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
- **Lock**—when checked, prevents the symmetry line from being moved.
- **Blend Mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
- **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolour effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.
- **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions.

> **Note:** The tool can be associated with a particular brush when editing it in the **Brushes** panel. For more information, see the [Modifying brushes](../../11-pixel-painting/02-modifying-pixel-brushes.md) topic.

#### SEE ALSO:

- [Painting pixel brush strokes](../../11-pixel-painting/01-painting-pixel-brush-strokes.md)
- [Brushes Panel](../../23-panels/04-brushes-panel.md)
- [Pressure sensitivity](../../05-drawing-curves-and-shapes/14-pressure-sensitivity.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
