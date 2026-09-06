# Draw and edit geometric shapes

Geometric and other special shapes that would be otherwise hard to draw can be easily created using one of the corresponding shape tools. Once drawn, both the shape and its stroke can be made into curves for more freeform design.

![Shapes example](../../assets/shared/shapes_edit.png)

**To draw a new shape:**

1. Choose one of the shape tools, e.g., **Rounded Rectangle** from the Tools panel.
2. Do one of the following:
  - For precise *Object data entry*: `Cmd`-click on the page, then enter your shape dimensions and properties into the dialog (use the `Tab`  and up/down keyboard keys to jump between and increment values, respectively).  
To add the same shape again, double-click on the page while the `Cmd`  is still pressed.  
  
On the page/pasteboard, shapes will always be centered under the current cursor position, but can be positioned in relation to a repositioned anchor point on the dialog.  
  
With **Snapping** enabled, shapes can also be created and centered on a shape’s bounding box (including corner handles) by `Cmd`-clicking.  
  
To cancel the operation, press the `Esc`  (settings will be remembered).

    ![Object data entry](../../assets/images/shapes_dataentry.png)
  - For sizing *'by eye'*: Drag on the page, using the `Shift`  to constrain the shape's proportions if needed.  
 ![Drag shape](../../assets/shared/shapes_dragShape2.png)

With either method, modify options as required, either by changing the values on the context toolbar or by dragging the red handle(s) (if available).  
 ![Drag handle](../../assets/shared/shapes_dragNode2.png)

> **Tip:** When you hover over a handle, a red guide line will appear to suggest the direction of drag needed to modify your shape.

> **Note:** Every subsequent shape of the same type you create will assume previously used settings.

**To reset a shape handle to its initial position:**

- Double-click the red handle that has been previously moved. Any other repositioned handles on the shape will not be affected.

**To edit an existing shape:**

1. Click the **Node Tool**.
2. Select the shape, either by clicking the shape or by clicking the layer entry in the **Layers** panel.
3. Edit the shape as required by either by directly dragging the red handle(s), or by changing the values on the context toolbar.

> **Tip:** Shapes have special snapping properties which allow lines to snap to various angles within the shape.

**To convert a shape to curves:**

- Click **Convert to Curves**, found in either the **Layer** menu or on the context toolbar.

  ![Convert to Curves](../../assets/shared/shapes_convertToCurves.png)

The shape is now made from curves. Segments and nodes can be modified with the **Node Tool**.

> **Note — Modifier keys:** As you create shapes, the following modifier keys can be used while the shape is being drawn:
>
> - The `Shift`  constrains shape's proportions at the time of creation.
> - The `Cmd`  draws or resizes from center (can be combined with the `Shift` ).
> - Where appropriate, on many shapes, the `Cmd`  moves the red handles in pairs.
> - **macOS:** The `Ctrl`  lets you rotate a shape about its opposite handle.
> - **Windows:** Pressing the right mouse button lets you rotate a shape about its opposite handle.
> - The `Spacebar` lets you reposition a shape at the time of creation.
> - You can pick up color as you design by using the `Alt`  and dragging.

## Presets

Presets can be applied to shape tools from the context toolbar. These allow you to take variations of standard shapes and reuse them instantly. A number of master presets have been supplied, but you can also create and define your own presets using the **Preset Manager**.

**To apply tool presets:**

1. Select the shape you wish to access presets for.
2. From the shape's context toolbar, click the **Presets** icon.
3. A pop-up panel containing a list of available presets for the shape will be displayed. By clicking on a preset, you can apply it to the selected shape.
4. Where applicable, select a different category from the menu at the top of the panel to switch preset categories.

> **Note:** Master presets which have been supplied by Affinity will have an Affinity logo in the bottom right hand corner; user defined or custom presets will have a user logo in this corner instead.

**To create new custom tool presets:**

1. Select the shape you wish to create a new preset for and edit it to your liking.
2. From the shape's context toolbar, click the **Presets** icon.
3. From the pop up panel, select **Create Preset** from the preferences menu. Enter a name and category for your new preset, then click **Create**.

**To manage tool presets:**

1. Select the shape you wish to access presets for.
2. From the shape's context toolbar, click the **Presets** icon.
3. A pop up panel containing a list of available presets for the shape will be displayed. From this panel, select **Manage Presets** from the preferences menu.
4. The **Preset Manager** will be displayed. From here, you can do the following:
  - Drag and drop preset thumbnails into an existing category to move them into that category.
  - Right-click on a preset to rename it, delete it, export it, or revert any changes you have made to it.
  - Click on a category menu to rename it, delete it, restore master presets to it, import user presets directly to it, or export presets from it.
  - To create a new preset category, select **Create Category** and enter a name for your new category.
  - To return all master presets to their original uncategorized state, select **Restore Master Presets**.
  - To export any user defined presets from the **Preset Manager**, select **Export User Presets**. Type a name for the exported file along with any tags you would like it to have, choose the disk location you want to save it to and click **Export** or **Save**.
  - To import presets to the **Preset Manager**, select **Import Presets**. Locate the .aftoolpresets file you want to import and click **Import**.
  - To view presets for a different shape, select the shape from the **Filter:** menu.

#### SEE ALSO:

- [About geometric shapes](06-about-geometric-shapes.md)
- [About lines and shapes](01-about-lines-and-shapes.md)
- [Edit lines and shapes](03-edit-vector-lines-and-shapes.md)
- [Frame text](../26-text/04-frame-text.md)
- [Keyboard shortcuts for vectors](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
