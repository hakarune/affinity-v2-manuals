# ![Pixel Persona](../../assets/shared/ui/pixel_persona_on.png)

 Creating custom pixel brushes

In Pixel Persona, you can create a custom brush from scratch using a raster image, from a copied preset or from a pixel selection. You can also edit existing brushes and either override them or duplicate to save your altered versions.

**![Edit Brush](../../assets/shared/ui/manager.png)

 To edit an existing brush do one of the following:**

- With the Paint Brush Tool selected, on the context toolbar, click **More**.
- On the **Brushes** panel, `Click`-click the brush you would like to modify and select **Edit Brush**.
- On the **Brushes** panel, double-click the brush you woud like to alter.

**To update or reset brush settings:**

1. `Click`-click the brush you would like to modify and select the option.

**![Panel Preferences](../../assets/shared/ui/moremenuicon.png)

 To create a custom preset brush stroke from scratch:**

On the **Brushes** panel, click Panel Preferences and then select:

- **New Intensity Brush**—creates a brush stroke based on the opacity values of a raster image. In the pop-up dialog, navigate to and select a file, and click **Open**.
- **New Round Brush**—creates a brush stroke based on a circular shape.
- **New Square Brush**—creates a brush stroke based on a rectangular shape.
- **New Image Brush**—creates a brush stroke based on the colour values of a raster image. In the pop-up dialog, navigate to and select a file, and click **Open**.

The new brush is added to the selected category using default settings. To edit the default settings, follow the procedure below from step 3 immediately below.

**![Edit Brush](../../assets/shared/ui/manager.png)

 To create a custom preset brush stroke from a preset:**

1. On the **Brushes** panel, select a brush and click **Edit Brush**.
2. In the dialog, click **Duplicate** and then **Close**.
3. Select the new brush at the bottom of the panel and click **Edit Brush**.
4. Adjust the settings in the dialog. See [Modifying brushes](02-modifying-pixel-brushes.md) for more information.
5. Click **Close**.

**![Panel Preferences](../../assets/shared/ui/moremenuicon.png)

 To create a custom image brush from a pixel selection:**

1. Make a selection using a pixel selection tool.
2. On the **Brushes** panel, choose a category to save your brush to.
3. click Panel Preferences and then select **New Brush From Selection**.

The image brush is added to the end of the current brush category. Custom intensity brushes can also be created from a mask layer that has a pixel selection in place by using the same process.

> **Note:** If you are creating a brush from a selection on a placed image, its image layer needs to be rasterised first.

**![Edit Brush](../../assets/shared/ui/manager.png)

 To create a multi-brush:**

1. On the **Brushes** panel, create a main brush or duplicate a selected brush.
2. Select the new brush and click **Edit Brush**.
3. Click the Sub Brushes tab.
4. Click **Add Bitmap**, select a nib file for your sub brush and click **Open**.
5. Double-click the brush entry appearing in the window to launch the Sub-Brush Editor.
6. Edit the sub brush settings as you would for your base brush, then click **Close**.
7. In the Brush Editing dialog, change sub brush settings to control:
   - **Drawing**—controls where the sub brush is drawn in relation to the main brush.
  - **Blending**—controls how the sub brush blends with the main brush.
  - **Sync size**—when checked, sets the default width of the stroke to match that of the main brush.
  - **Sync spacing**—when checked, sets the distance between each nozzle point to match that of the main brush.

> **Note:** You can add additional sub brushes with the topmost sub brush affecting the lower sub brush, and the resulting stroke affecting the main brush. Sub-brushes can be reordered by dragging within the Sub Brushes window.

> **Tip:** Additional options from ![Panel Preferences](../../assets/shared/ui/moremenuicon.png)
>
>  Panel Preferences allow you to create, rename, delete, import and export brush categories.
>
>
> Move brushes to any created category by `Click`-clicking and selecting a category name from the **Move Brush to Category** menu option. Custom categories adopt the naming convention 'Brushes', 'Brushes 2', 'Brushes 3', etc.

#### SEE ALSO:

- [Brushes panel](../23-panels/04-brushes-panel.md)
- [Modifying pixel brushes](02-modifying-pixel-brushes.md)
- [Rasterising](../08-object-control/18-rasterising.md)
