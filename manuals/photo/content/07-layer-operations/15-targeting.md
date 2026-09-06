# Targeting

Targeting controls where new layers are placed in the layer stack on creation.

## Default targeting behavior

By default, layers are positioned:

- Directly above the currently selected layer.
- At the top of the layer stack, if there is no layer selected.

## Alternative targeting behaviors

The default targeting behavior can be overridden so that layers are placed or drawn behind the selection, at the top of the layer stack (regardless of selection), or nested inside a layer.

You can override the default behavior for only the next layer that is created, or 'lock' an alternative behavior so it's applied to new layers until you decide otherwise.

> **Tip:** After creation, you can reposition or nest layers using the **Layers** panel or the Order options on the Toolbar.

**To change targeting behavior:**

- (Optional) If you wish to use the 'behind' or 'at the top' behavior on an ongoing basis, hold the `Alt` .
- On the Toolbar, select one of the following:
  - ![Insert behind the selection](../../assets/shared/ui/insert_behind_selection.png) **Insert behind the selection**
  - **![Insert at the top of the layer](../../assets/shared/ui/insert_top_of_layer.png) Insert at the top of the layer**
  - **![Insert inside the selection](../../assets/shared/ui/insert_inside_selection.png) Insert inside the selection**

> **Note:** To revert to default targeting, click the Toolbar button of the currently selected behavior.

> **Note:** Alternatively, you can access the default and alternative targeting behaviors on the **Arrange** menu.

#### SEE ALSO:

- [Copy and paste options](08-copying-and-pasting-content.md)
- [Layer clipping](07-layer-clipping.md)
- [Grouping](10-grouping.md)
- [Layers panel](../33-panels/13-layers-panel.md)
- [Ordering](14-ordering.md)
