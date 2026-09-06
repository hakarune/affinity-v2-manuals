# ![Brush Tool](../../../assets/shared/ui/vector_brush_tool.png)

 Vector Brush Tool

With the **Vector Brush Tool** you can create a hand-painted look by painting freehand, variable width, lines and shapes as if you were painting on paper. Its vector characteristics means you can edit the stroke at any time.

Its variable width lines can be controlled either by velocity—most useful when drawing with a mouse—or by pressure—for use when drawing with a pressure-sensitive device.

The **Vector Brush Tool**, located on the Tools panel, paints by scaling or repeating an image along a path (line).

As you paint, nodes are created automatically and can be edited with the `Cmd`  or at any time with the **Node Tool**.

The tool uses many of the standard line settings to control the appearance of the applied stroke. Brush types are applied using the **Brushes** panel.

> **Tip:** With any brush tool selected, you can quickly decrease or increase the size (width) of your brush by holding `Ctrl` and `Alt` then dragging left or right, respectively. If the brush tool has a hardness attribute, this can be adjusted in a similar way by holding `Ctrl` and `Alt` then dragging up or down.
>
>
> With any brush tool selected, you can quickly decrease or increase the size (width) of your brush by holding `Cmd` and `Alt` then dragging left or right, respectively. If the brush tool has a hardness attribute, this can be adjusted in a similar way by holding `Cmd` and `Alt` then dragging up or down.

### Settings

The following settings can be adjusted from the context toolbar:

- **Colour**—the colour of your brush stroke. Click the colour swatch to select from solid colours, a picked colour, colour gradients or from your preset or custom colour swatches.
- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see through the brush stroke is. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the Brushes dialog to access advanced brush settings.
- **Stabiliser**—enables stroke stabilisation using either a **Rope stabiliser** or **Window stabiliser** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Blend Mode**—changes how the stroke's colour interacts with existing colours on a layer. Select from the pop-up menu.
- **Controller**—controls how the brush stroke responds to various inputs:
   - Brush Defaults—the brush variance and controller settings stored with the currently selected brush are used. Click **More** on toolbar to access.
  - Automatic—the input device (pen tablet, Force Touch device, mouse) is detected and the brush will work automatically with that device, using the brush variance settings but ignoring the brush controller setting. You can operate devices interchangeably.
  - Pressure—brush stroke is only responsive to pressure from a pen tablet, using the brush variance settings but ignoring the brush controller setting.
  - Velocity—brush stroke is only responsive to speed of mouse movement.

#### SEE ALSO:

- [Painting brush strokes](../../10-vector-painting/01-painting-vector-brush-strokes.md)
- [Pencil Tool](07-pencil-tool.md)
- [Pen Tool](06-pen-tool.md)
- [Node Tool](02-node-tool.md)
- [Brushes Panel](../../23-panels/04-brushes-panel.md)
- [Stroke Panel](../../23-panels/16-stroke-panel.md)
- [Pressure sensitivity](../../05-drawing-curves-and-shapes/14-pressure-sensitivity.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
