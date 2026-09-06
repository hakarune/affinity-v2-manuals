# Swatches panel (Photo Persona only)

The **Swatches** panel makes it easy to use predefined colors, and also to define, store and reuse your own selection of colors.

> **Note:** This panel is hidden by default. It can be switched on via the **Window** menu.

## About the Swatches panel

**macOS:**

The **Swatches** panel stores your recently used colors and lets you access a range of predefined palettes, each containing solid or gradient fill swatches. These can be selected for use with various tools and for applying directly to objects. You can also create and store your own swatches as custom color palettes either for the document, app or system-wide, as well as import any exported Affinity .afpalette from other users or import Adobe Swatch Exchange (ASE) palettes.

**Windows:**

The **Swatches** panel stores your recently used colors and lets you access a range of predefined palettes, each containing solid or gradient fill swatches. These can be selected for use with various tools and for applying directly to objects. You can also create and store your own swatches as custom color palettes either for the document or app, as well as import any exported Affinity .afpalette from other users or import Adobe Swatch Exchange (ASE) palettes.

As well as accessing various palettes, you can create global, spot, and overprint colors for vector content. Your registration color can also be customized.

The panel contains a search facility for displaying only named swatches which match the typed description.

![Swatches panel](../../assets/images/panel_swatches.png)
*Swatches panel: (A) Set Foreground/Set Background color selectors with color 'none' swatch and 'swap' arrow, (B) Color Picker Tool and picked color swatch, (C) Category list, (D) Category color palette swatches, (E) Search, (F) Panel Preferences, (G) Opacity control, (H) Recently used colors, (I) None, Black, Mid-gray and White swatches, (J) Add current color to palette as a global color, (K) Add current color to palette, (L) Registration color, (M) Global color, (N) Overprint color, (O) Spot color.*

![Swatches thumbnail](../../assets/shared/swatches_thumbnail.png)
*Markings which distinguish specialist color swatches: (A) Global, (B) Overprint, (C) Spot.*

The active color selector is shown at the front of the two color selectors. Choosing a new color will apply it to the active color selector.

For vector shapes, lines and text, the color selector is for stroke and fill color instead of Foreground and Background color, respectively.

The Swatches panel also shows None, Black, Mid-gray and White swatches, recently used colors and an opacity control. Swatches are organized into color palettes by category.

> **Note:** ![Panel Preferences](../../assets/shared/ui/moremenuicon.png) To add a customized registration color for professional printing, click **Panel Preferences**, then select **Add Registration Color**.

> **Note:**
>
> **macOS:**
>
> Preset color palettes (available from the category list pop-up menu) include macOS color palettes such as Apple, Web Safe Colors, System, and Crayons.
>
> **Windows:**
>
> Preset color palettes (available from the category list pop-up menu).
>
> ![Panel Preferences](../../assets/shared/ui/moremenuicon.png) To list swatches by name instead of thumbnail, click **Panel Preferences**, then select **Show as List**.

> **Note:** The active swatch is whichever is shown in front of the other. You can switch between the Foreground and Background color selectors by pressing the **X** .

> **Note:** You can set the Foreground and Background color selectors to white and black, respectively, by pressing the **D** .

> **Note:** ![Gradient Tool](../../assets/shared/ui/fill_tool.png) The **Gradient Tool** changes the appearance of the **Swatches** panel. Only one color selector swatch is shown to represent the color of the currently selected stop on the gradient.

> **Tip:** Hold down the `Alt`  when selecting a swatch to honor the opacity and/or noise already applied to any vector shape, line or text (i.e. only the color will update).

## Working with palettes

The ten most recently used colors are automatically added to the panel on a temporary basis. You can permanently store custom colors and gradients that you use most often in any of the palettes or you can create custom palettes to host them.

> **Tip:** Although you can add colors to any of the predefined palette categories, we recommend that you always create your own.

The following types of palette exist within Affinity Photo 2:

- **Document**—these palettes are saved within the current document.
- **Application**—these palettes are saved within Affinity Photo 2. These palettes are available to any Affinity Photo 2 document.
- **macOS:** **System**—these palettes are saved to your operating system. These palettes are available within Affinity Photo 2 and other apps installed on your system.
- **PANTONE®**—these palettes are based on PANTONE® Colors. These palettes are available to any Affinity document.

## Saving and deleting custom color palettes

**To create a new palette:**

- Click Panel Preferences and choose an 'Add Palette' option.

> **Note:** From Panel Preferences, you can also rename, delete, duplicate and link the selected palette.

**To save a color or gradient to a palette:**

1. On the **Swatches** panel, select a palette from the palette pop-up menu.
2. Do one of the following:
  - `Click`-click an object, then from the pop-up menu, click **Add to>Swatches** and choose to add color from fill, stroke or both.
  - Select **Add current color to palette**. Use the Stroke/Fill color selector to target the color.

**To edit a saved swatch:**

- Double-click a saved swatch.

**To delete a saved swatch:**

- `Click`-click the swatch you want to remove and choose **Delete Fill** from the pop-up menu.

## Generating a palette from document

You can generate a palette from the colors used throughout your document.

**To generate a palette from document:**

- Click Panel Preferences and choose an option from **Create Palette from Document**.

A new palette is created (named after the document) using all the colors currently in the document.

## Generating a palette from an image

You can generate a palette of colors from any supported image file.

**To generate a palette from an image:**

- Click Panel Preferences and choose **Create Palette From Image**.
- From the **Create Palette From Image** dialog, click **Select Image** or click-drag an image onto the dialog to load it.
- Change the **Number of Colors** slider to generate more or fewer colors from the selected image.
- Use the **Location** option to specify whether the generated palette should be system-wide (Mac only), app-wide, or limited to the current document. You can also add the colors to the current active palette too.
- Click **Create** to complete the palette generation.

## Importing and exporting custom color palettes

Custom color palettes can be exported to and imported from external files (add-ons) via the Panel Preferences menu. For more information on add-ons, see the [About add-ons](../29-add-ons/01-about-add-ons.md) topic.

## Setting default palettes

Any palette can be set as the default used for specific color formats. For example, you can set **RGB/8** documents to have a different default palette to **CMYK/8** documents.

**To set a default palette:**

1. On the **Swatches** panel, select a palette from the palette pop-up menu.
2. Click Panel Preferences and choose a color format option from the **Set as Default for** from the pop-up menu.

To revert to using a system palette, choose **Remove Default for <color format>** from Panel Preferences.

#### SEE ALSO:

- [Selecting colors](../12-color/06-selecting-colors.md)
- [Color panel](08-color-panel.md)
- [Color chords](../12-color/07-color-chords.md)
- [Customizing the workspace](../31-workspace/04-customize/02-workspace.md)
- [About add-ons](../29-add-ons/01-about-add-ons.md)
- [Importing add-ons](../29-add-ons/04-importing-add-ons.md)
- [Exporting add-ons](../29-add-ons/03-exporting-add-ons.md)
