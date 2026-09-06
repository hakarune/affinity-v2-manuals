# Viewing

There are a variety of viewing choices available which let you preview your designs before output using view modes, make mode comparisons and arrange your document view.

## About view modes

Vector

Pixel

Retina pixel

Outline (wireframe)

X-ray (wireframe)

Hairline

![](../../assets/shared/viewmode_vector.jpg)

The view mode is made up of two distinct components:

- how objects are displayed on screen, and
- how your project page is presented.

#### Pixel view mode

During design, vector objects are presented as if they are constructed from individual pixels. This is an accurate representation of how your design will appear once exported and viewed as an image.

#### Retina pixel view mode

As for Pixel mode above, but represents how your design will display on retina and high DPI displays.

#### Vector view mode

Drawn objects are displayed as vectors by default. This means that, regardless of the current zoom level, objects (and applied effects) are always presented with smooth vector edges and transitions.

#### X-ray (wireframe) view mode

As for Outline view mode, but page objects still display their fills at reduced opacity. On more complex designs, perhaps when zoomed in, this helps to interpret the view better.

#### Outline (wireframe) view mode

During design, page objects are presented as paths only (with no fills or strokes). All otherwise obscured paths are exposed, and selection behavior changes so grouped objects can immediately be selected just like ungrouped ones. In complex designs, this can be used to more easily target unlocked and locked objects for selection.

#### Hairline view mode

For CAD documents, Hairline mode displays designs as CAD apps would display them. All lines are displayed as thin lines so line weights are ignored, regardless of zoom level.

### View mode options

These are not modes but additional options that can be applied to any view mode.

#### Grayscale

This gives the option of viewing your document in grayscale. This is useful when evaluating contrast and dynamic range more easily.

#### Hide Effects

This hides any layer effects applied to your document. It helps to improves performance on more complex documents where extensive layer effects are used.

You can apply different option settings to different sides of a split view.

![View mode options](../../assets/shared/viewmodeoptions.png)
*Grayscale and Hide Effect view mode options when enabled.*

### Views

You can switch from the default single view to split view to compare any two combinations of view modes.

![Views](../../assets/shared/views.png)
*Single and split views. The latter showing a 'Vector - X-ray (wireframe)' view mode comparison.*

#### Single View

Presents the selected mode in isolation on a single page.

#### Split View

Simultaneously presents two modes side-by-side on the same page, allowing for a visual comparison to be made. A sliding divider can be repositioned to view different areas of the design in either mode. Either view is selectable, allowing you to set different combinations of view modes.

## Clip to Canvas

This option, set by default, restricts the document view, so you can only see objects which are placed on the page. If objects extend beyond the page, the area which lies on the page is visible while the area which lies on the pasteboard is hidden. Objects which are entirely on the pasteboard are hidden.

When **Clip to Canvas** is switched off, the pasteboard is visible, as are all the objects placed on it.

Clip to Canvas can be used in conjunction with any of the above view options.

**To display specific modes:**

1. From the top menu, click **View>Customize Toolbar**.
2. Locate the **View Mode/Advanced View Mode** section tools and drag onto the Toolbar, as required.
3. From the toolbar, do one of the following:
  - Click **Pixel view mode** to display vector designs as individual pixels.
  - Click **Retina pixel view mode** to display vector designs as individual pixels. Use for Retina displays.
  - Click **Wireframe view mode** to display vector designs in either Outline or X-ray view modes depending on which was last selected via **View>View Mode>Wirefame**.

> **Tip:** Ensure all icons are deselected to return to Vector mode.

> **Note:** You can also switch between view modes via the **View** menu (**View Mode** submenu). The **Hairline** view mode on the submenu displays designs as if viewed in CAD apps (stroke/line weights are ignored).

**To work in Split View:**

1. From the **View** menu's **View Mode** submenu, select **Split View**.
2. Click one side of the divider. The divider label displays as black for the selected side (otherwise displayed as gray).
3. From the Toolbar or **View** menu, select a mode.

**To enable or disable view mode options:**

- From the **View** menu's **View Mode** submenu, enable or disable **Grayscale** or **Hide Effects**.

**To activate/deactivate Clip to Canvas:**

- From the **View** menu, select **View Mode** and then select **Clip to Canvas**.

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

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../25-settings-preferences/01-settings-preferences.md):
>
> - **Performance>View Quality**

#### SEE ALSO:

- [App and document windows](../19-workspace/01-application-and-document-windows.md)
- [Zooming](09-zooming.md)
- [Zoom Tool](../20-tools/01-layout-tools/15-zoom-tool.md)
- [Preview mode](../16-design-aids/11-preview-mode.md)
- [Keyboard shortcuts for the document view](../24-keyboard-shortcuts/01-keyboard-shortcuts.md)
