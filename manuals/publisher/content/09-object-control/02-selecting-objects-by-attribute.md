# Selecting objects by attribute

The **Layers** panel and the **Select** menu provide ways to select objects by their type or a shared attribute, adding or removing matching objects to or from the current selection.

> **Note:** These selection methods are complementary to [traditional methods of selecting objects](01-selecting-objects.md).

## Select Same Tag Color and Select Same Name

From the **Layers** panel, you can select all layers that share a name or an assigned tag color.

## Select Same and Select Object

These powerful selection methods allow you to quickly make bulk changes to your design all at once, e.g. to convert objects that share a non-global color to use a global one.

Both commands are available from the **Select** menu. Each offers a range of options in its submenu.

The **Select Same** command selects all objects in your document that match an attribute on your currently selected object.

Select Same matches objects with the same Fill Color, Stroke Color, Fill & Stroke Color, Stroke Weight, Transparency, Blend Mode, Shape, Width, Height, Rotation, Name, or Tag Color.

Select Same can also match objects whose Width, Height, or Stroke Weight is less than, less than or equal, greater than, or greater than or equal to that of the currently selected object.

![Select same fill](../../assets/shared/selecting_same_fill.png)
*Selecting the same fill color across objects.*

**macOS:**

> **Tip:** With Select Same's **Width**, **Height**, or **Stroke Weight** submenu open, hold the `Alt`  to change the **Less than** and **Greater than** to **Less (or equal)** and **Greater (or equal)**, respectively.

The **Select Object** command selects all objects of a matching type within your document. For example, you can select all groups, symbols, art text, frame text, path text, picture frames, tables, data merge layouts, objects according to their fill, stroke or opacity, and so on.

![Select object stroked](../../assets/shared/selecting_object_stroked.png)
*Selecting objects with strokes applied.*

> **Tip:** To specify whether Select Object or Select Same will include or exclude hidden objects in its resultant selections, select or deselect **Select Hidden Objects** from the corresponding command's submenu.

## Edit All Layers and Select Same/Select Object

**Edit All Layers** (on the **Layers** panel) determines the scope of Select Same and Select Object.

When enabled, the commands select matching objects across all spreads in your document. When disabled, they select matching objects only on the current spread.

**To select all layers sharing the same name:**

- With a layer selected on the **Layers** panel, `Click`-click it and choose **Select Same Name** from the pop-up menu.

**To select all layers sharing a tag color:**

- With a layer selected on the **Layers** panel, `Click`-click it and choose **Select Same Tag Color** from the pop-up menu.

**To select all objects sharing a chosen attribute with the currently selected object:**

- With an object selected, from the **Select** menu, choose **Select Same** and select an attribute from the menu.

**To select all objects of a certain type:**

- From the **Select** menu, choose **Select Object** and select an object type from the menu.

> **Note — Modifier keys:** When using the Select Object command, the following modifier keys can be used to aid object selection:
>
> - The `Shift`  adds matching objects to the current selection.
> - **macOS:** The `Alt`  removes matching objects from the current selection.
> - **Windows:** The `Cmd`  removes matching objects from the current selection.
> - The `Shift`+`Alt`  combination selects matching objects only from within the current selection, i.e. non-matching objects are removed from the current selection.
>
> **macOS:**
>
> When using the Select Same command to match objects by Width, Height or Stroke Weight, the `Alt`  modifies the **Less** option to **Less (or Equal)** and the **Greater** option to **Greater (or Equal)**.

#### SEE ALSO:

- [Move Tool](../20-tools/01-layout-tools/01-move-tool.md)
- [Selecting objects](01-selecting-objects.md)
- [Grouping objects](03-grouping-objects.md)
- [Layers panel](../21-panels/14-layers-panel.md)
- [Selecting and editing layers](../08-layers/04-selecting-and-editing-layers.md)
- [Tagging layers](../08-layers/05-tagging-layers.md)
- [Select and view pages](../05-pages-spreads-and-sections/07-select-and-view-pages.md)
