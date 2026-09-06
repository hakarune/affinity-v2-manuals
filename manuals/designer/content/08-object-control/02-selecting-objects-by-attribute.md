# Selecting objects by attribute

The **Layers** panel and the **Select** menu provide ways to select objects by their type or a shared attribute, adding or removing matching objects to or from the current selection.

> **Note:** These selection methods are complementary to [traditional methods of selecting objects](01-selecting-objects.md).

## Select Same Tag Colour and Select Same Name

From the **Layers** panel, you can select all layers that share a name or an assigned tag colour.

## Select Same and Select Object

These powerful selection methods allow you to quickly make bulk changes to your design all at once, e.g. to convert objects that share a non-global colour to use a global one.

Both commands are available from the **Select** menu. Each offers a range of options in its submenu.

The **Select Same** command selects all objects in your document that match an attribute on your currently selected object.

Select Same matches objects with the same Fill Colour, Stroke Colour, Fill & Stroke Colour, Stroke Weight, Transparency, Blend Mode, Shape, Width, Height, Rotation, Name, or Tag Colour.

Select Same can also match objects whose Width, Height, or Stroke Weight is less than, less than or equal, greater than, or greater than or equal to that of the currently selected object.

![Select same fill](../../assets/shared/selecting_same_fill.png)
*Selecting the same fill colour across objects.*

**macOS:**

> **Tip:** With Select Same's **Width**, **Height**, or **Stroke Weight** submenu open, hold the `Alt`  to change the **Less than** and **Greater than** to **Less (or equal)** and **Greater (or equal)**, respectively.

The **Select Object** command selects all objects of a matching type within your document. For example, you can select all groups, symbols, art text, artboards, pixel layers, unfilled objects, transparent objects, and any objects which do/don't have a stroke, etc.

![Select object stroked](../../assets/shared/selecting_object_stroked.png)
*Selecting objects with strokes applied.*

Both commands also work well in conjunction with each other, allowing you to first group all layers of each fill colour (using Select Same) and then select all of the grouped layers (using Select Object), for example, effectively organising the layers in your image.

> **Tip:** To specify whether Select Object or Select Same will include or exclude hidden objects in its resultant selections, select or deselect **Select Hidden Objects** from the corresponding command's submenu.

## Edit All Layers and Select Same/Select Object

The behaviour of the Select Same and Select Object commands depends on the **Edit All Layers** setting on the **Layers** panel:

- When the setting is enabled, the Select Same/Select Object commands will match objects across all artboards.
- When the setting is disabled, the Select Same/Select Object commands will match only objects on the current artboard.

**To select all layers sharing the same name:**

- With a layer selected on the **Layers** panel, `Click`-click it and choose **Select Same Name** from the pop-up menu.

**To select all layers sharing a tag colour:**

- With a layer selected on the **Layers** panel, `Click`-click it and choose **Select Same Tag Colour** from the pop-up menu.

**To select all objects sharing a chosen attribute with the currently selected object:**

- With an object selected, from the **Select** menu, choose **Select Same** and select an attribute from the menu.

**To select all objects of a certain type:**

- From the **Select** menu, choose **Select Object** and select an object type from the menu.

> **Note:** ### Modifier keys
>
>
> When using the Select Object command, the following modifier keys can be used to aid object selection:
>
>
> - The `Shift`  adds matching objects to the current selection.
> - The `Alt`  removes matching objects from the current selection.
> - The `Cmd`  removes matching objects from the current selection.
> - The `Shift`+`Alt`  combination selects matching objects only from within the current selection, i.e. non-matching objects are removed from the current selection.
>
>
>
>
> **macOS:**
>
> When using the Select Same command to match objects by Width, Height or Stroke Weight, the `Alt`  modifies the **Less** option to **Less (or Equal)** and the **Greater** option to **Greater (or Equal)**.

#### SEE ALSO:

- [Move Tool](../22-tools/design-tools/01-move-tool.md)
- [Selecting objects](01-selecting-objects.md)
- [Grouping objects](03-grouping-objects.md)
- [Layers panel](../23-panels/11-layers-panel.md)
- [Tagging layers](../07-layers/13-tagging-layers.md)
- [Selecting and editing layers](../07-layers/04-selecting-and-editing-layers.md)
