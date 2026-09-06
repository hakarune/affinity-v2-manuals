# Rasterising

Lines, curves, shapes and text can be rasterised to create pixel layers.

Rasterisation has various uses:

- For when the appearance of complex vector gradients or effects needs to be honoured, particularly for print artwork.
- To convert a placed image layer to a pixel layer (for pixel manipulation). By default, many brush tools rasterise image layers before painting.

**To rasterise an object:**

Do one of the following:

- From **Layer** menu, select **Rasterise**.
- On the **Layers** panel, `Click`-click a layer and select **Rasterise**.

> **Note:** Partly off-canvas objects will not be trimmed with this operation; if completely off canvas, the object will be kept.

> **Note:** Multiple objects, on adjacent or non-adjacent layers, can be rasterised simultaneously. Each selected layer is converted to a discrete pixel layer, i.e. the layers are not flattened.

**To rasterise an object and trim off-canvas content:**

- On the **Layers** panel, `Click`-click a layer and select **Rasterise & Trim**.

> **Note:** Partly off-canvas objects will be trimmed with this operation; if completely off canvas, the object will be removed.

**To rasterise an object to a mask:**

- From **Layer** menu, select **Rasterise to Mask**.

> **Warning:** When rasterising a layer that has layer effects applied to it, a dialog offers an option to **Preserve layer FX**. Clear the checkbox to include the effects in the rasterisation process along with the layer's shape, line, curve or text content. Leave it ticked to rasterise only the layer's content and still be able to edit the effects afterwards.

#### SEE ALSO:

- [Draw curves and shapes](../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md)
- [Draw and edit shapes](../05-drawing-curves-and-shapes/06-draw-and-edit-shapes.md)
- [Working with text](../12-text/01-working-with-text.md)
- [Selecting objects](01-selecting-objects.md)
