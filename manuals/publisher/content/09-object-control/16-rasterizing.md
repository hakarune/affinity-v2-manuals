# Rasterizing

Lines, curves, shapes and text can be rasterized to create pixel layers. This is only a requirement if the appearance of complex vector gradients or effects need to be honored, particularly for print artwork.

> **Warning:** When rasterizing a layer that has layer effects applied to it, a dialog offers an option to **Preserve layer FX**. Clear the checkbox to include the effects in the rasterization process along with the layer's shape, line or text content. Leave it ticked to rasterize only the layer's content and still be able to edit the effects afterwards.

## Converting pixel layers

The data in pixel layers is ordinarily stored within the Affinity Publisher document.

A pixel layer can be converted to an image layer or a picture frame. By doing this, the resulting layer’s contents become listed in the **Resource Manager**, where you can select **Make Linked** to save them to an external file or **Replace** to overwrite them with data from an external file.

**To rasterize a shape, line or text layer:**

- In the **Layers** panel, `Click`-click a layer and select **Rasterize**.

> **Note:** Multiple objects, on adjacent or non-adjacent layers, can be rasterized simultaneously. Each selected layer is converted to a discrete pixel layer, i.e. the layers are not flattened.

**To convert a pixel layer to an image layer or a picture frame:**

- Select the image within the document view or on the **Layers** panel.
- From the **Layer** menu, select **Convert to Image Resource** or **Convert to Picture Frame** as needed.

#### SEE ALSO:

- [Draw curves and shapes](../06-drawing-curves-and-shapes/02-draw-curves-and-shapes.md)
- [Draw and edit shapes](../06-drawing-curves-and-shapes/05-draw-and-edit-shapes.md)
- [Working with text](../10-text/01-working-with-text.md)
- [Resource Manager](../12-placing-external-content/06-resource-manager.md)
