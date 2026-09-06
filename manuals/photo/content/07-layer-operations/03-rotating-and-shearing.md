# Rotating and shearing

Layer content can be rotated and sheared directly on the page using the **Move Tool**.

![Before](../../assets/shared/rotateshear_before.jpg)
![After](../../assets/shared/rotateshear_after.jpg)
*Before and after rotate and shear applied.*

Positioning the cursor around the bounding box of your layer content and then dragging will allow you to rotate or shear the layer content. Feedback is provided by the following cursors.

![Rotate cursor](../../assets/shared/cursor/cursor_rotate_45.png) ![Rotate cursor](../../assets/shared/cursor/cursor_rotate_225.png) ![Shear cursor](../../assets/shared/cursor/cursor_shear_90.png) ![Shear cursor](../../assets/shared/cursor/cursor_shear_0.png)

Rotation is also possible about a custom transform origin positioned on your page.

**To rotate layer content:**

1. With the **Move Tool**, select layer content on a chosen layer.
2. Do one of the following:
  - Drag the selected layer content's rotation handle.
  - Position the cursor close to a corner handle and drag on the page.
  - From the **Arrange** menu, select a rotate option.

> **Note:** You can rotate layer content with more precision using the **Transform** panel.

**To rotate layers to same:**

1. Select multiple layers, ensuring the layer previously rotated is selected *first*. To do this, use `Shift`-click to target it first or a marquee selection that encompasses it first.
2. ![Match Rotation](../../assets/shared/ui/match-rotation.png) On the Toolbar, click **Alignment**, then set the **Make Same** option, choosing **Rotation**.
3. Click **Apply**.

**To rotate layers to a targeted rotated key object:**

1. Select multiple layers.
2. With the `Alt`  pressed, click the target rotated key object (i.e., a layer). The selected key object will possess a strong outline.
3. ![Match Rotation](../../assets/shared/ui/match-rotation.png) On the Toolbar, click **Alignment**, then set the **Make Same** option, choosing **Rotation**.

**To undo the rotation:**

- Double-click at any corner handle when you see the rotation cursor.

**To move the transform origin:**

1. Select layer content.
2. Select the **Move Tool**, then click **Enable Transform Origin** on the context toolbar. The origin shows centrally within the selected layer content.
3. Drag the origin to a new position in the selected layer content or anywhere on the page.

Once you've moved the origin, you can rotate your layer content about it as described above. If using the **Transform** panel, rotation is about this custom origin unless you choose to override this and use the panel's Anchor point selector instead.

> **Note:** For vector shapes, lines and text, you can snap the origin to the bounding box, center, key points, or the geometry of other objects (or even the same object).
>
> **macOS:**
>
> To retain its relative positioning and snapping, you can move an object by its custom transform origin; `Ctrl`-click *after* you start dragging the origin.

**To reset the transform origin back to its original position:**

- Double-click the transform origin.

**To shear layer content:**

1. Select layer content on a chosen layer.
2. Position the cursor close to a side handle and drag on the page.

> **Note:** You can shear with more precision using the **Transform** panel; this can optionally be about a custom transform origin.

**To undo the shear:**

- Double-click at any edge handle when you see the shear cursor.

> **Note — Modifier keys:** When using the Move Tool, the following modifier keys can be used to aid rotating and shearing:
>
> - The `Shift`  constrains rotation to 15° increments.
> - The `Cmd`  shears the opposite edge in the opposite direction by the same value.
> - **macOS:** When rotating from an object or selection's corner handle, the `Ctrl`  temporarily repositions the transform origin to the opposite corner.
> - **Windows:** When rotating from an object or selection's corner handle, holding the right mouse button temporarily repositions the transform origin to the opposite corner.

#### SEE ALSO:

- [Transforming](../05-sizing-cropping-and-warping/05-transforming.md)
- [Flipping](04-flipping.md)
- [Transform panel](../33-panels/30-transform-panel.md)
