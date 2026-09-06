# Viewing

There are a variety of viewing options available which lets you preview your designs before output using view modes, make mode comparisons and arrange your document view.

## About view modes

Vector

Pixel

Retina pixel

Outline (wireframe)

X-ray (wireframe)

Hairline

![](../../assets/shared/viewmode_vector.jpg)

#### Vector view mode

Drawn objects are displayed as vectors by default. This means that, regardless of the current zoom level, objects (and applied effects) are always presented with smooth, vector edges and transitions.

#### Pixel view mode

During design, vector objects are presented as if they are constructed from individual pixels. This is an accurate representation of how your design will appear once exported and viewed as an image.

#### Retina pixel view mode

As for Pixel mode above, but represents viewing on retina and high DPI displays.

#### Outline (wireframe) view mode

During design, page objects are presented as paths only (with no fills or strokes). All otherwise obscured paths are exposed, and selection behaviour changes so grouped objects can immediately be selected just like ungrouped ones. In complex designs, this can be used to more easily target unlocked and locked objects for selection.

#### X-ray (wireframe) view mode

As for Outline view mode, but page objects still display their fills at reduced opacity. On more complex designs, perhaps when zoomed in, this helps to interpret the view better.

#### Hairline view mode

For CAD documents, Hairline mode displays designs as CAD apps would display them. All lines are displayed as thin lines so line weights are ignored, regardless of zoom level.

### View

#### Single View

Presents the selected mode in isolation on a single page.

#### Split View

Presents two modes simultaneously on the same page. A sliding divider can be repositioned to view different areas of the design in either mode.

## Clip to Canvas

This option, set by default, restricts the document view, so you can only see objects which are placed on the page. If objects extend beyond the page, the area which lies on the page is visible while the area which lies on the pasteboard is hidden. Objects which are entirely on the pasteboard are hidden.

When **Clip to Canvas** is switched off, the pasteboard is visible, as are all the objects placed on it.

Clip to Canvas can be used in conjunction with any of the above view options.

> **Note:** This option is unavailable in documents containing [artboards](../04-artboards/01-about-artboards.md).

**![Pixel view mode](../../assets/shared/ui/pixel_view_mode.png)**

From the toolbar, do one of the following:

- Click **Pixel view mode** to display vector designs as individual pixels.
- Click **Retina pixel view mode** to display vector designs as individual pixels. Use for Retina displays.
- Click **Wireframe view mode** to display vector designs in either Outline or X-ray view modes depending on which was last selected via **View>View Mode>Wirefame**.

> **Tip:** Ensure all icons are deselected to return to Vector mode.

> **Note:** You can also switch between view modes via the **View** menu (**View Mode** submenu). The **Hairline view mode** on the submenu displays designs as if viewed in CAD apps (stroke/line weights are ignored).

**To work in Split View:**

1. From the **View** menu's **View Mode** submenu, select **Split View**.
2. Click one side of the divider.

  The divider label displays as black for the selected side (otherwise displayed as grey).
3. From the Toolbar or **View** menu, select a mode.

## New View

There are times when it is useful to view a design at different zoom levels simultaneously. This can be achieved by opening your current document in a New View. The views can then be set to different zoom levels. Changes made to any view are replicated in the other.

> **Tip:** The New View can also be set to different View and Zoom modes.

**To open the current document in a new view:**

- From the **View** menu, select **New View**. The document opens in a new tab/window which includes a numerical reference in its title.

**To switch between open documents and views:**

Do one of the following:

- Click a document tab.
- Click a document window header if the window is floating.
- From the **View** menu, select a document from the **Views** submenu.

> **Preferences:** ### Settings (or Preferences)
>
>
> Related behaviours can be adjusted from [the app's settings](../27-settings-preferences/01-settings-preferences.md):
>
>
> - **Performance>View Quality**

#### SEE ALSO:

- [Toolbar](../02-user-interface/02-toolbar.md)
- [Clip to Canvas](../17-design-aids/02-clip-to-canvas.md)
- [Keyboard shortcuts for the document view](../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
