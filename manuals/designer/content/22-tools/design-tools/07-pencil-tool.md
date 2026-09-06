# ![Pencil Tool](../../../assets/shared/ui/pencil_tool.png)

 Pencil Tool

With the **Pencil Tool** you can create a hand-drawn look by drawing freehand, variable width, lines as if you were drawing on paper.

As you draw, nodes are created automatically along the stroke which can optionally be smoothed as you draw by enabling the **Stabiliser** feature. A **Sculpt** mode also lets you reform or continue your pencil stroke at any time, although you can use the **Node Tool** to edit too. When using a combination of sculpting and Use Fill, you can form conjoined pencil strokes that can take a fill with the stroke's concave area.

Its variable width lines can be controlled either by velocity—most useful when drawing with a mouse—or by pressure—for use when drawing with a pressure sensitive pen tablet.

## Adjusting the tool's appearance

Line styles are applied using the **Stroke** panel. For brush textures, pick a brush from the **Brushes** panel.

> **Tip:** Tool shortcut : `N`

### Settings

The following settings can be adjusted from the context toolbar:

- **Stroke**—the colour of your stroke. Click the colour swatch to select from solid colours, a picked colour, colour gradients or from your preset or custom colour swatches.
- **Width**—the line thickness in points. Type directly in the text box or drag the pop-up slider to set the value.
- ![Sculpt Mode](../../../assets/shared/ui/SculptMode.png)

   **Sculpt**—when enabled, any selected pencil stroke can be reshaped or continued; the former by drawing new start and end stops anywhere along the pencil stroke, the latter by drawing from either stroke end node.
- **Controller**—controls whether the tool is sensitive to real pressure (*Pressure*) or speed of mouse movement (*Velocity* or *Inverse Velocity*). Select *None* to use neither.
- **Stabiliser**—enables stroke stabilisation using one of two modes:
   - ![Rope stabilisation mode](../../../assets/shared/ui/stabiliser_rope.png)

     **Rope mode**—drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope *Length* (radius) values by redirecting the slackened rope.
  - ![Window stabilisation mode](../../../assets/shared/ui/stabiliser_window.png)

     **Window mode**—smoothes the stroke by averaging sampled input positions within a *Window* whose size is configurable.
- **Use Fill**—when checked, the concave area of the stroke is filled with the currently set fill colour (from **Colour** panel) as you draw. In Sculpt mode, continuing strokes remains as one object, which allows the fill to be applied along the stroke's length.
- **Auto Close**—when enabled, the start and end nodes of the pencil stroke are connected to form a closed shape. The nodes become smooth nodes so a natural curve is created on closing.

#### SEE ALSO:

- [Draw curves and shapes](../../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md)
- [Edit curves and shapes](../../05-drawing-curves-and-shapes/03-edit-curves-and-shapes.md)
- [Node Tool](02-node-tool.md)
- [Pen Tool](06-pen-tool.md)
- [Stroke panel](../../23-panels/16-stroke-panel.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
