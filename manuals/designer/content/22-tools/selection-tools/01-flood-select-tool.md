# ![Flood Select Tool](../../../assets/shared/ui/magic_wand_tool.png)

 Flood Select Tool

The **Flood Select Tool** enables you to select pixels of a similar colour.

Pixels added to a selection are determined by the colour of the pixel or adjacent pixels under the tool when you click or drag across the page, respectively. The dragging operation controls the selection tolerance, i.e. how much the selection will grow to encompass pixels of similar colour values under the cursor.

### Settings

The following settings can be adjusted from the context toolbar:

- **Mode**—select from **New**, **Add**, **Subtract**, and **Intersect**.
- **Source**—the source determines the layer(s) from which the pixels are sampled. Select from the pop-up menu.
- **Tolerance**—sets the range of pixels affected when a pixel is clicked. For lower tolerance settings, pixels must be very close in value to the clicked pixel. For higher tolerance settings, pixel colour can vary widely from the clicked pixel.
- **Contiguous**—when enabled, only selects a range of pixels within the same area. If disabled, similar pixel ranges will be selected even if they are separated and in different parts of the image.
- **Refine**—click to display the [Refine Selection](../../13-selections/05-refining-pixel-selection-edges.md) dialog to access advanced selection settings.

### About selection modes

The four modes available from the context toolbar affect how your selection develops.

- **New**—cancels all current selections and creates a new selection.
- **Add**—adds areas to the current selection. If there is no selection in place, a new selection will be created.
- **Subtract**—removes areas from the current selection.
- **Intersect**—a new selection area is created from the overlap between the newly added selection area and the current selection.

#### SEE ALSO:

- [Creating pixel selections](../../13-selections/01-creating-pixel-selections.md)
- [Refining pixel selection edges](../../13-selections/05-refining-pixel-selection-edges.md)
- [Selection Brush Tool](03-selection-brush-tool.md)
- [Marquee Selection Tool](02-marquee-selection-tools.md)
