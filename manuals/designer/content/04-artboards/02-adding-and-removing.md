# Adding and removing artboards

Artboards can be created with new documents or added to your current document at a preset or custom size at any time.

## Adding artboards

When [creating a new document](../03-get-started/02-create-new-documents.md), you can automatically create your first artboard using the settings in the New Document dialog.

Once you have an [document open](../03-get-started/04-open-documents-and-images.md), you can add artboards using the [Artboard Tool](../22-tools/design-tools/13-artboard-tool.md).

Artboards can be created:

- using the original document's dimensions—perfect for creating multi-page documents
- using preset sizes—perfect for device-specific designing
- using the current selection's dimensions
- at a custom size
- by copying or [duplicating](../08-object-control/04-duplicating-objects.md) other artboards
- by converting a selected object

## Removing artboards

Artboards can be deleted from your project at any time. Any objects placed on the artboard will be deleted as well (you're prompted to confirm deletion).

As an alternative to deleting an artboard, you can convert it into a standard object. In this situation, any objects on the artboard will be nested within the new object, thereby preserving your design.

**To create a new document with an artboard:**

1. From the **File** menu, click **New**.
2. From the dialog, select a preset category and preset from the scrolling list.
3. (Optional) Adjust the settings in the dialog for a custom setup.
4. Check **Create artboard**. Some categories (e.g., Devices) automatically offer presets as artboards.
5. Click **Create**.

> **Note:** The settings applied will become the default size for future artboards.

> **Note:** You can apply a drawing scale factor to independent artboards via the New Document dialog or **File>Document Setup** by using the **Scale** tab. The **Measure Tool** also lets you apply a **Drawing Scale** factor, along with scaling based on a known measurement. Once created, additional scaled artboards can be created from a selected artboard using the **Artboard Tool** and **Size** set to Selection on the context toolbar.

**![Move Tool](../../assets/shared/ui/move_tool.png)

 ![Artboard Tool](../../assets/shared/ui/artboard_tool.png)

 To add artboards at preset dimensions:**

1. (Optional) With the **Move Tool**, select one or more objects.
2. On the **Tools** panel, select the **Artboard Tool**.
3. On the context toolbar, from the **Size** pop-up menu, select:
   - **Document**—to add an artboard at the current document's dimensions to the canvas.
  - **Selection**—to add an artboard at the same size and position as the selected artboard or object(s). You may need to reposition the new artboard to give it its own space on the pasteboard.
  - any other preset—to add another artboard at a device-specific preset's dimensions.
4. On the context toolbar, click **Insert Artboard**.

**![Artboard Tool](../../assets/shared/ui/artboard_tool.png)

 To add custom size artboards:**

- With the **Artboard Tool** selected, drag on the pasteboard.

> **Note:** ### Modifier keys
>
>
> When using the Artboard Tool, the following modifier keys can be used:
>
>
> - The `Shift`  constrains the artboard's proportions at the time of creation (to a square) or when resizing.
> - The `Cmd`  resizes the artboard from its centre.
> - The `Ctrl`  lets you rotate an artboard about its opposite handle.
> - Pressing the right mouse button lets you rotate an artboard about its opposite handle.

**![Move Tool](../../assets/shared/ui/move_tool.png)

 ![Artboard Tool](../../assets/shared/ui/artboard_tool.png)

 To copy or duplicate an artboard:**

- With an artboard selected, do one of the following:
   - With the **Move Tool** or **Artboard Tool**, `Cmd`-drag the artboard.
  - From the **Edit** menu, select **Duplicate**.

**To convert an object to an artboard:**

- With the single object selected, from the **Layer** menu, select **Convert Object to Artboard**.

> **Tip:** If an object has been converted to an artboard, that artboard remains editable as if it was the original object. For example, an artboard converted from a closed shape can still be edited as a closed shape and an artboard converted from artistic text can still be edited as text.

**![Artboard Tool](../../assets/shared/ui/artboard_tool.png)

 ![Remove Layers](../../assets/shared/ui/trash_can.png)

 To remove an artboard:**

1. Do one of the following:
   - Using the **Artboard Tool**, click to select a single artboard or `Shift`-click to select multiple artboards.
  - On the **Layers** panel, select one or more artboards.
2. Do one of the following:
   - Press the `Backspace` .
  - On the **Layers** panel, click **Remove Layer**.

**To convert an artboard to an object:**

- With the single artboard selected, from the **Layer** menu, select **Convert Artboard to Object**.

#### SEE ALSO:

- [Artboard Tool](../22-tools/design-tools/13-artboard-tool.md)
- [Selecting, moving and resizing artboards](03-selecting-moving-and-resizing.md)
- [Create new documents](../03-get-started/02-create-new-documents.md)
- [Open documents and images](../03-get-started/04-open-documents-and-images.md)
- [Duplicating objects](../08-object-control/04-duplicating-objects.md)
