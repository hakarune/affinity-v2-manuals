# ![Flood Select Tool](../../assets/shared/ui/magic_wand_tool.png)

 Flooding pixel selections

Using the **Flood Select Tool** in the Pixel Persona you can define a selection of similar colour value pixels with a single click.

## Flooding and tolerance

When using the [Flood Select Tool](../22-tools/selection-tools/01-flood-select-tool.md), Affinity Designer will analyse the target (clicked) pixel and use its colour value to create a selection which includes pixels with similar colour values.

![Before](../../assets/shared/selections_flood_before.jpg)
![After](../../assets/shared/selections_flood_contiguous.jpg)
*Before and after pixel clicked.*

The number of pixels selected is determined by the tool's tolerance setting. The higher the tolerance the more variance allowed between the target pixel and selected pixels. Therefore a higher tolerance will likely lead to more pixels being included in the selection.

This makes selecting an area of similar colour and tone effortless.

## Contiguous behaviour

By default, flood selecting is contiguous. This means pixels with similar colour values must be adjacent to one another to be selected. Therefore, pixels must be directly connected to the target pixel (or other selected pixels) to be selected. If there is a high contrast edge between areas of similar colour, the pixels on the opposite side of the edge will not be selected using a single click.

As an alternative, the contiguous behaviour can be switched off. This will mean pixels of similar colour to the target pixel will be selected regardless of their position within the image.

![Contiguous](../../assets/shared/selections_flood_contiguous.jpg)
![Non-contiguous](../../assets/shared/selections_flood_noncontiguous.jpg)
*Difference in selection method with contiguous on (before) and off (after).*

**![Flood Select Tool](../../assets/shared/ui/magic_wand_tool.png)

 To create a pixel selection:**

With the **Flood Select Tool** selected:

1. (Optional) On the context toolbar, set the **Tolerance**.
2. Click on your page.

**![Flood Select Tool](../../assets/shared/ui/magic_wand_tool.png)

 To create a pixel selection using multiple target pixels:**

With the **Flood Select Tool** selected:

1. On the context toolbar, set the **Mode** to **Add**.
2. Click on your page.
3. Repeat step 2 as needed.

> **Note:** Alternatively, you can subtract or intersect a 'flood selection' from the current selection using the other **Mode** options. For more information on the available selection modes, see [Creating pixel selections](01-creating-pixel-selections.md).

**![Flood Select Tool](../../assets/shared/ui/magic_wand_tool.png)

 To switch off contiguous selection:**

- With the **Flood Select Tool** selected, on the context toolbar, ensure the **Contiguous** option is off.

#### SEE ALSO:

- [Flood Select Tool](../22-tools/selection-tools/01-flood-select-tool.md)
- [Creating pixel selections](01-creating-pixel-selections.md)
- [Modifying pixel selections](04-modifying-pixel-selections.md)
- [Refining pixel selection edges](05-refining-pixel-selection-edges.md)
