# Rasterizing

Shape, Line, Text and Image layers can be rasterized to create pixel layers. This "flattening" operation can be performed manually or automatically (when applying filters or retouch brushes).

Rasterization has various uses:

- For when the appearance of complex vector gradients or effects needs to be honored, particularly for print artwork.
- To convert a placed image layer to a pixel layer (for pixel manipulation). By default, many brush tools rasterize image layers before painting.
- Inpainting: after cropping, inpainting may be used to tidy up an image's corners, but the inpainting may be using information outside of the crop area. Rasterizing will discard this information and force the inpainting to use only what is visible.

**To rasterize a shape, line or text layer:**

Do one of the following:

- From **Layer** menu, select **Rasterize**.
- On the **Layers** panel, `Click`-click a layer and select **Rasterize**.

> **Note:** Off-canvas layer content will not be trimmed with this operation.

> **Warning:** When applying filters or retouch brushes to the above layers, automatic rasterization occurs. This means the layers can't be edited as vectors afterwards. Ensure shapes, lines and text are completely edited to your satisfaction beforehand.

> **Note:** Multiple adjacent or non-adjacent layers can be rasterized simultaneously. Each selected layer is converted to a discrete pixel layer, i.e. the layers are not flattened.

**To rasterize a shape, line or text layer and trim off-canvas content:**

Do one of the following:

- From **Layer** menu, select **Rasterize & Trim**.
- On the **Layers** panel, `Click`-click a layer and select **Rasterize & Trim**.

**To rasterize a shape, line or text layer to a mask:**

- From **Layer** menu, select **Rasterize to Mask**.

> **Warning:** When rasterizing a layer that has layer effects applied to it, a dialog offers an option to **Preserve layer FX**. Clear the checkbox to include the effects in the rasterization process along with the layer's shape, line, curve or text content. Leave it ticked to rasterize only the layer's content and still be able to edit the effects afterwards.

#### SEE ALSO:

- [Draw lines and shapes](../25-lines-and-shapes/02-draw-lines-and-shapes.md)
- [Draw and edit geometric shapes](../25-lines-and-shapes/07-draw-and-edit-shapes.md)
- [Working with text](../26-text/01-working-with-text.md)
- [Selecting](02-selecting.md)
