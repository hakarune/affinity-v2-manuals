# Erasing

Designer lets you erase areas of a pixel or vector layer using a combination of the Erase Brush Tool, the Brushes panel and the tool's context toolbar. Typically you'd erase previously unwanted pixel brush strokes on a pixel layer.

## Erasing on a pixel layer

If you're working on a pixel layer, you can use the Erase Brush Tool to erase unwanted pixels directly on the layer.

**![Erase Brush Tool](../../assets/shared/ui/eraser_tool.png)

 To erase on a pixel layer:**

1. From the Tools panel, select the **Erase Brush Tool**.
2. From the Brushes panel, select a brush thumbnail of your choice.
3. Adjust the brush width and other brush-related properties from the context toolbar above your workspace.
4. Drag on the page in the direction that you want the erase brush stroke to follow.

## Erasing on a vector layer

Pixels don't exist on a vector layer so a pixel mask is created and applied over the vector layer instead; the vector layer remains unaffected. By painting with pixel brushes directly on the mask, you can decide what can be shown or hidden on the underlying vector layer.

**![Erase Brush Tool](../../assets/shared/ui/eraser_tool.png)

 To erase on a vector layer:**

1. From the Layers panel, select the vector layer, group or object contained within it.
2. Switch to Pixel Persona.
3. From the Tools panel, select the **Erase Brush Tool**.
4. The tool uses a soft-round brush by default. To use a different brush style, choose one from the **Brushes** panel.
5. On the context toolbar, change the brush values as desired.
6. Paint on the vector layer to erase.

You'll notice a vector mask thumbnail appear next to the layer, group or object. While this remains selected you can continue erasing. Selecting the adjacent vector thumbnail allows you to edit the vector layer, or group or object again.

> **Note:** Using the **Assistant** you can control how pixel erasing works on vector layers. You can optionally rasterise the layer, group or object completely (flattening the layer) or take no action (preventing erasing from occurring).

#### SEE ALSO:

- [Erase Brush Tool](../22-tools/design-tools/23-erase-brush-tool.md)
- [Brushes panel](../23-panels/04-brushes-panel.md)
- [Painting pixel brush strokes](01-painting-pixel-brush-strokes.md)
- [Assistant Settings](../27-settings-preferences/01-settings-preferences.md)
- [Keyboard shortcuts for painting operations](../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
