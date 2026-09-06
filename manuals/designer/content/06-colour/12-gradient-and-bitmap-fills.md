# Gradient and bitmap fills

The [Fill Tool](../22-tools/design-tools/10-fill-tool.md) lets you draw a simple colour gradient, solid or bitmap fill across your object. The created fill path can be edited directly on the object to introduce more than two colours along the gradient path, introduce opacity, reposition added colours or control colour transitions. You can also apply a more complex gradient via a Gradient Editor.

> **Note:** If needed, you can precisely define the fill path via the colour swatch on the tool's context toolbar. This should be done with no handles selected.

![Gradient and bitmap fill examples](../../assets/shared/gradient.png)
*(From left to right) Elliptical, Radial, Linear, Conical, and Bitmap fill types applied to a basic shape.*

> **Note:** You can also apply a gradient to pixel layers, adjustment layers and layer masks using the Fill Tool.

**![Fill Tool](../../assets/shared/ui/fill_tool.png)

 To apply a gradient:**

1. Use the **Move Tool** to select an object.
2. Select the **Fill Tool** from the Tools panel.
3. From the context toolbar, select either 'Stroke' or 'Fill' from the **Context** pop-up menu.
4. From the context toolbar, select a fill type from the **Type** pop-up menu.
5. Drag the cursor across the object's stroke or fill depending on what you selected previously.

  Hold down the `Shift`  to constrain the angle of the gradient path to 45°.

> **Tip:** Select and drag an end stop on the path to change the length and direction of the path. End stops can be recoloured and be given reduced opacity from the **Colour** panel. Use the `Cmd`  to reposition the gradient without affecting its length or direction.

> **Tip:** Create your own gradient fills by clicking the colour swatch, adjacent to the Type pop-up menu, on the context toolbar.

> **Note:** You can pick up colour as you design by holding the `Alt`-key and dragging.

**To create a bitmap fill:**

1. Use the **Move Tool** to select an object.
2. Select the **Fill Tool**.
3. Do one of the following:
   - From your Finder window, drag the file of choice and drop it onto either the **Swatches** panel, **Colour** panel or the Primary/Secondary colour selector.
  - From your Explorer window, drag the file of choice and drop it onto either the **Swatches** panel, **Colour** panel or the Primary/Secondary colour selector.
  - From the **Assets** panel, click an asset, e.g. a texture, shape or other.
  - From the **Stock** panel, click one of the photos from your search results.
4. Use the context toolbar settings and the tool's nodes to modify the fill as required.

> **Note:** Alternatively, with the **Fill Tool**, you can select **Bitmap** from the **Type** pop-up menu on the context toolbar, then navigate to the image you will use to fill.

> **Note:** Instead of using the **Fill Tool**, you can also crate a bitmap fill using the **Move Tool**. To do so, drag the file of choice from your Finder window and drop it onto the areas suggested above.
>
>
> Instead of using the **Fill Tool**, you can also crate a bitmap fill using the **Move Tool**. To do so, drag the file of choice from your Finder window and drop it onto the areas suggested above.

**To modify a bitmap fill:**

1. With the **Fill Tool** active, make a selection.
2. On the context toolbar, click **Rotate gradient** to change the orientation of the fill at 90° clockwise intervals.
3. Enable **Maintain aspect ratio** to ensure the bitmap fill is not stretched or squashed when edited.
   Set the **Extend** and **Quality** options as desired. The former option controls how the tile that makes up the bitmap is presented; the latter how the bitmap fill is resampled on object resize.
  Check **Scale with object** to allow for stretching or shrinking of the bitmap fill while resizing. Leave it unchecked to ensure stretching or shrinking isn't taking place thus preserving the texture of the image.

**To modify a gradient (directly on an object):**

With the **Fill Tool** selected, click an object with a gradient fill applied and then do any of the following:

- Click on the gradient path to add a stop.
- Click a stop to select it. Selected stops display larger than other stops.
- Drag a stop to reposition it along the gradient path. End stops can be repositioned (by dragging) to extend or contract the gradient's length; the angle of the gradient can also be changed by dragging.
- Drag a midpoint marker to adjust the spread of colours between two colour stops.
- Apply a colour (or opacity or noise value) to a selected stop from the **Colour** panel.
- Delete a selected stop by pressing `Backspace` .

> **Note:** When you scale or shear an object with a linear or radial gradient applied, the gradient will intelligently reapply itself to fit the modified object's new proportions.

**To modify a gradient (via the tool's context toolbar):**

1. With the **Fill Tool** selected, click an object.
2. Deselect any selected stops.
3. From the context toolbar, select the colour swatch.
4. Click the **Gradient** option which lets you modify your gradient using the following settings:
   - **Type**—determines the gradient type (linear, elliptical, etc.) via a pop-up menu.
  - **Position**—controls the position of the stop along the gradient from left (0%) to right (100%), with 50% representing the central point.
  - **Mid Point**—adjusts the spread of colours between the selected colour stop and the stop to its right.
  - **Colour**—click the colour swatch to display a pop-up panel where you can modify the selected stop's colour (including noise value).
  - **Opacity**—controls how see through the stop is. 100% represents fully opaque, 0% represents fully transparent.
  - **Insert**—adds a new stop between a selected stop and the stop to its right. The stop adopts the colour at its new position.
  - **Copy**—duplicates the selected stop, positioning it between the selected stop and the stop to its right.
  - **Delete**—removes the selected stop from the gradient.
  - **Reverse**—the gradient is reversed, i.e. like a mirror image.

## Scaling

### Scaling bitmap fills

It is possible to rescale a bitmap fill by either restricting or allowing for the bitmap fill to grow or shrink when transforming, depending on the desired effect. One benefit here is that it is possible to leave the bitmap image and its texture unaffected by shrinking or stretching.

![Scale with Object](../../assets/shared/scale_with_object.png)
*A bitmap fill's texture unaffected by stretching a square object.*

> **Note:** With an object selected when creating a bitmap fill, the image will be placed as a tiled or repeating pattern in the object.

### Scaling sheared objects with linear or radial gradient fills

When you scale or shear an object with a linear, radial or conical gradient applied, the gradient will reapply itself to fit the modified object's new shape. This is important when transforming two-dimensional objects onto an isometric grid plane as the gradient will also be intelligently transformed. On a transformed object, an additional dashed correction path and stop is shown (right) which indicates gradient transformation and allows you to control the shear and scale on the fill—the path and stop can be removed to ignore the gradient transform if needed.

![Transformed object](../../assets/shared/gradient2.png)
*Transformed object with a dashed correction path and stop.*

When an object with a linear or radial gradient fill is sheared (skewed) or transformed onto an isometric pane, an additional pair of correction points appears.

![Before](../../assets/shared/fillhandles_before.jpg)
![After](../../assets/shared/fillhandles_after.jpg)

These help produce a fill that more naturally follows the sheared object's shape without distortion when the object is scaled and sheared.

**To convert the transformed fill to a conventional gradient fill:**

- Double-click the correction end stop to remove the correction path.

> **Note:** Double-clicking end stops on an isometric plane resets the correction points instead of deleting them.

#### SEE ALSO:

- [Selecting colours](06-selecting-colours.md)
- [Transparency](13-transparency.md)
