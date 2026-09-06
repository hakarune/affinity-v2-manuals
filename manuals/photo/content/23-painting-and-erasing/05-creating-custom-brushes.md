# Creating custom brushes

You can create a custom brush from scratch using a raster image, from a copied preset or from a pixel selection. You can also edit existing brushes and either override them or duplicate to save your altered versions.

## About custom brushes

By default, unmodified brushes in the panel are presented with a blue outline around their entry. When modifying brush settings, the customized brush will be presented with a red outline and a red dot in its top-left entry.

**To edit an existing brush do one of the following:**

- With the Paint Brush Tool selected, on the context toolbar, click **More**.
- On the **Brushes** panel, -click the brush you would like to modify and select **Edit Brush**.
- On the **Brushes** panel, double-click the brush you would like to alter.
- On the **Brushes panel**, click **Edit Brush**.

**To update or reset brush settings:**

1. -click the brush you would like to modify and select the option.

**To create a custom preset brush stroke from scratch:**

On the **Brushes** panel, click Panel Preferences and then select:

- **New Intensity Brush**—creates a brush stroke using a raster image, with darker pixels from the image rendered more opaque and lighter pixels more transparent. In the pop-up dialog, navigate to and select a file, and click **Open**.
- **New Round Brush**—creates a brush stroke based on a circular shape.
- **New Square Brush**—creates a brush stroke based on a rectangular shape.
- **New Image Brush**—creates a brush stroke based on the color values of a raster image. In the pop-up dialog, navigate to and select a file, and click **Open**.

The new brush is added to the selected category using default settings. To edit the default settings, follow the procedure below from step 3 immediately below.

**To create a custom preset brush stroke from a preset:**

1. On the **Brushes** panel, select a brush.
2. `Ctrl`-click the brush entry and select **Duplicate Brush**.
3. Select the duplicated brush (below the original), `Ctrl` click it and choose **Edit Brush**.
4. Adjust the settings in the dialog. See [Modifying brushes](06-modifying-brushes.md) for more information.
5. Click **Close**.
6. (Optional) Move your brush to a category via `Ctrl`-clicking the newly created brush and selecting the option.

> **Tip:**
>
> **macOS:** Alternatively, to duplicate a brush, on the **Brushes** panel press the `Alt`  and drag the selected brush in place.
>
> **Windows:** Alternatively, to duplicate a brush, on the **Brushes** panel press the `Alt`  and drag the selected brush in place.

**To create a custom image brush from a pixel selection:**

1. Make a selection using a pixel selection tool.
2. On the **Brushes** panel, choose a category to save your brush to.
3. Click Panel Preferences and then select **New Brush From Selection**.

The image brush is added to the end of the current brush category. Custom intensity brushes can also be created from a mask layer that has a pixel selection in place by using the same process.

> **Note:** If you are creating a brush from a selection on a placed image, its image layer needs to be rasterized first.

**To update or reset a modified brush:**

1. -click the brush and choose an option.

> **Tip:** Additional options from ![Panel Preferences](../../assets/shared/ui/moremenuicon.png) Panel Preferences allow you to create, rename, delete, move or copy brushes, as well as import and export brush categories.
>
> For organization purposes, it is suggested to move or copy custom brushes to any created category by `Click`-clicking and selecting a category name from the **Move Brush to Category** or **Copy Brush to Category** menu option. Custom categories adopt the naming convention 'Brushes', 'Brushes 2', 'Brushes 3', etc.

#### SEE ALSO:

- [Brushes panel](../33-panels/05-brushes-panel.md)
- [Modifying brushes](06-modifying-brushes.md)
- [Creating multi-brushes](05-creating-custom-brushes/01-pixel-multibrushes.md)
- [Rasterizing](../07-layer-operations/19-rasterizing.md)
