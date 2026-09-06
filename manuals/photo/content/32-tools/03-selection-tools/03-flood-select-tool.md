# Flood Select Tool

The **Flood Select Tool** enables you to select pixels of a similar color.

Pixels added to a selection are determined by the color of the pixel or adjacent pixels under the tool when you click or drag across the page, respectively. The dragging operation controls the selection tolerance, i.e. how much the selection will grow to encompass pixels of similar color values under the cursor.

### Settings

The following settings can be adjusted from the context toolbar:

- **Mode**—select from **New**, **Add**, **Subtract**, and **Intersect**.
- **Source**—the source determines the layer(s) from which the pixels are sampled. Select from the pop-up menu.
- **Tolerance**—sets the range of pixels affected when a pixel is clicked. For lower tolerance settings, pixels must be very close in value to the clicked pixel. For higher tolerance settings, pixel color can vary widely from the clicked pixel.
- **Contiguous**—when enabled, only selects a range of pixels within the same area. If disabled, similar pixel ranges will be selected even if they are separated and in different parts of the image.
- **Antialias**—when enabled (default), the option helps to prevent jagged and/or pixelated edges.
- **Refine**—click to display the [Refine Selection](../../08-selections/06-refining-pixel-selection-edges.md) dialog to access advanced selection settings.

### About selection modes

The four modes available from the context toolbar affect how your selection develops.

- **New**—cancels all current selections and creates a new selection.
- **Add**—adds areas to the current selection. If there is no selection in place, a new selection will be created.
- **Subtract**—removes areas from the current selection.
- **Intersect**—a new selection area is created from the overlap between the newly added selection area and the current selection.

> **Note — Modifier keys:** The following modifier keys can be used to aid in the creation of selections:
>
> - **Drag** while making selections to set tolerance and to select areas.
> - **macOS:** Pressing the `Shift`  while dragging adds to the current selection.
> - **Windows:** Pressing the `Shift`  while dragging adds to the current selection.
> - **macOS:** Pressing the `Alt`  while dragging removes areas from the current selection.
> - **Windows:** Pressing the `Alt`  while dragging removes areas from the current selection.

#### SEE ALSO:

- [Creating pixel selections](../../08-selections/01-creating-pixel-selections/01-overview.md)
- [Refining pixel selection edges](../../08-selections/06-refining-pixel-selection-edges.md)
- [Selection Brush Tool](02-selection-brush-tool.md)
- [Marquee Selection Tools](04-marquee-selection-tools.md)
