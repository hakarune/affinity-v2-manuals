# Undo Brush Tool

The **Undo Brush Tool** can be used to selectively undo modifications to individual pixels, restoring them to a previous history state or a saved snapshot.

After setting a brush source, you can blend the image's current state back to a previous state, like painting backwards in time.

### Settings

The following settings can be adjusted from the context toolbar:

- **Width**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
- **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
- **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
- **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
- **More**—click to display the Brushes dialog to access advanced brush settings.
- **Force pressure to control size**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
- **Stabilizer**—enables stroke stabilization using either a **Rope stabilizer** or **Window stabilizer** mode; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing rope **Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
- **Symmetry**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The center axis point can be repositioned by click-dragging it.
- **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
- **Lock**—when checked, prevents the symmetry line from being moved.
- **Blend Mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
- **Blend**—when selected (default), pixels which do not overlap those in the selected history or snapshot state are unaffected, allowing the blending of the current document state with the selected, previous state. If this option is off, all pixels are returned to the previous state when painted.
- **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions.

> **Note:** This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying brushes](../../23-painting-and-erasing/06-modifying-brushes.md) topic.

**To paint from history or a saved snapshot:**

1. Display the History or Snapshot panel.
2. Click the **Set Undo Brush Source** icon on the history state or snapshot you want to paint back to.
3. Begin painting with the Undo Brush Tool.

#### SEE ALSO:

- [History panel](../../33-panels/11-history-panel.md)
- [Using snapshots](../../30-design-aids/04-using-snapshots.md)
