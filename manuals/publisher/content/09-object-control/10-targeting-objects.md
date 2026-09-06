# Targeting objects

Targeting allows you to decide the z-order, or nesting, of an object during creation.

## Default targeting behavior

By default, drawn or placed objects are positioned:

- Directly above the current selection.
- At the top of the layer, if there is no selection.

## Alternative targeting behaviors

The default targeting behavior can be overridden so that objects are placed or drawn behind the selection, at the top of the layer (regardless of selection), or nested inside the selection.

You can override the default behavior for only the next object that is created, or 'lock' an alternative behavior so it's applied to new objects until you decide otherwise.

> **Tip:** After creation, you can reposition or nest objects using the **Layers** panel or the Order options on the Toolbar.

**To change targeting behavior:**

- (Optional) If you wish to use the 'behind' or 'at the top' behavior on an ongoing basis, hold the `Alt` .
- On the Toolbar, select one of the following:
  - ![Insert behind the selection](../../assets/shared/ui/insert_behind_selection.png) **Insert behind the selection**
  - **![Insert at the top of the layer](../../assets/shared/ui/insert_top_of_layer.png) Insert at the top of the layer**
  - **![Insert inside the selection](../../assets/shared/ui/insert_inside_selection.png) Insert inside the selection**

> **Note:** To revert to default targeting, click the Toolbar button of the currently selected behavior.

> **Note:** Alternatively, you can access the default and alternative targeting behaviors on the **Layer** menu's **Insertion** submenu.

#### SEE ALSO:

- [Layer clipping](../08-layers/11-layer-clipping.md)
- [Grouping objects](03-grouping-objects.md)
- [Arrange/manage layers](../08-layers/06-arrange-manage-layers.md)
- [Layers panel](../21-panels/14-layers-panel.md)
- [Ordering objects](09-ordering-objects.md)
