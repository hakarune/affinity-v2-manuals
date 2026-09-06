# Selecting objects

Before you can move or modify vector objects, you must first select them.

![Selecting objects](../../assets/shared/selecting_objects.png)

> **Note:** The fundamental methods of selecting objects described here are complemented by advanced **Select Same** and **Select Object** commands that [build selections based on object attributes](02-selecting-objects-by-attribute.md), such as object type, fill color, or stroke width.

## Auto-select

By default, the **Auto-select** option is checked on the context toolbar. As expected, it automatically selects the object and its layer when you click to select it on the page. The option can be disabled if preferred.

You can select single or multiple objects using a variety of methods. If you already have an object selected, you can quickly select the next or previous object in the z-order (stack).

When shapes are created, a base box will be established on creation to accommodate the range of different potential shape sizes when creating variants of that shape. For tighter snapping, you can manually swap to a tight bounding box using the **Cycle Selection Box** option on the **Select** Menu.

## Edit All Layers and Select All

The behavior of the Select All command depends on the **Edit All Layers** setting on the **Layers** panel:

- When enabled, the command will select all objects across all layers and sub-layers.
- If this option is off, only objects on the current layer are selected. Objects within sub-layers are not selected.

> **Note:** Edit All Layers is enabled by default but can be disabled at any time.

## Selection box types

For some shapes (e.g. star shapes), a *Base box* type will be established on shape creation to accommodate the range of different potential shape sizes when creating variants of that shape. However, you can temporarily swap to a 'tighter' bounding box called *Regular bounds* if needed. The latter is useful for accurately resizing a shape by its corner/edge handles to another object or page element.

![Base box and regular bounds](../../assets/shared/selectionbox_shape.png)
*Selection box types: Base box (A) and Regular bounds (B)*

For rotated multiple selections of objects or pixel layers, you can temporarily reorient the selection's selection box to vertical using the same Regular bounds type. Otherwise, the selection box will stay transformed with the transformed items (using the Base Box type).

![Rotated multiple selection with reoriented selection box](../../assets/shared/selectionbox_multiselection.png)
*Rotated multiple selection before (A) and after (B) reorienting the selection box to Regular bounds*

> **Tip:** Try targeting an independently rotated key object in a multiple selection using `Alt`-click. The overall Base Box will adopt the same rotation as that key object.

It's possible to permanently set the object's selection box to orient to the page's horizontal and vertical edges. The object is unaffected. When reselecting the items again, the selection box will remain unrotated.

If you're using axonometric grids, the additional selection box type *Planar bounds*, which matches the current grid, can also be swapped to and be made permanent if needed.

**To toggle Edit All Layers:**

- On the **Layers** panel, click **Edit All Layers**.

**To select an object:**

Do one of the following:

- With the **Move Tool** selected, click an object or group on the page to select it.
- On the **Layers** panel, click an object entry.

**To select multiple objects:**

Do one of the following:

- With the **Move Tool** selected, `Shift`-click each object on the page in turn to select them.
- With the **Move Tool** selected, drag to draw a marquee around the object(s).*

**To select all objects in a layer:**

- From the **Select** menu, choose **Select All on Current Layer**.

**To select all objects on the active page/spread:**

- From the **Select** menu, select **Select All**.

**To select other objects in a selected object's z-order:**

Do one of the following:

- With the object selected, on the **Select** menu, choose:
  - **Select Next** / **Select Previous**—selects an object adjacent to the selected object in z-order sequence, within the same layer, group or entire layer stack. The option will cycle selection from bottom to top and vice versa.
  - **Select Top** / **Select Bottom**—as above but selection is made of the top or bottom object in the layer, group or entire layer stack in z-order.
  - **Select Parent**—selects the parent clipping object, layer or group in which the selected object is placed.
- `Click`-click the object, then choose the same options as above from the pop-up menu.

**To control automatic selection behavior:**

- On the Move Tool's context toolbar, choose one of the following options. These let you optionally select only objects or groups on the page, or just from the Layers panel (on-page selection is prevented).
  - **Default**—objects and groups can be selected on the page or Layers panel.
  - **Objects**—only objects can be selected on the page, while grouped items will be selected as if ungrouped; both groups and layers can be selected from Layers panel.
  - **Groups**—only groups can be selected on the page; both groups and layers can be selected from Layers panel.

**To cycle between selection box types:**

- On the **Select** Menu, choose **Cycle Selection Box**.

**To set the selection box permanently:**

1. Cycle to the selection box you want using **Cycle Selection Box** on the **Select** Menu.
2. On the same menu, choose **Set Selection Box**.

> **Note — Modifier keys:** When using the **Move Tool**, the following modifier keys can be used to aid layer selection:
>
> - With the **Auto-select** option disabled:
>   - `Cmd`-click an object on the page to temporarily override the option and enable the selection.
> - With the **Auto-select** option enabled:
>   - On the **Layers** panel, holding the `Shift`  and clicking selects multiple objects. The same is achieved by clicking objects on the page while holding the key.
>   - **macOS:** Holding the `Cmd`+`Shift` keys while clicking on multiple objects on the page in turn, selects them.
>   - **Windows:** Holding the `Ctrl`+`Shift` keys while clicking on multiple objects on the page in turn, selects them.
>   - `Alt` -click a layer in the panel temporarily disables the whole composition preview leaving only the one (clicked on) selected—helpful in confirming selection of layers in complex compositions.
>   - The `.`  toggles a shape's bounding box between a Base box and a Regular bounds box. Alternatively, use **Cycle Selection Box** on the **Select** Menu. To permanently use a Regular bounds box on the object, use `Cmd`+`.`.
>   - **macOS:** As you drag a selection marquee, pressing the `Ctrl`  selects objects which are only partially covered by the selection marquee. This behavior can be made the default in Settings (Preferences)*.

> **Tip:** ![Lock/Unlock](../../assets/shared/ui/lock_layer.png) You can **Lock**/**Unlock** selected objects from the **Layers** panel or **Layer** menu.

**To find an object in the Layers panel manually:**

Do one of the following:.

- `Click`-click the layer content on the page and select **Find in Layers Panel**.
- From the **Layer** menu, select **Find in Layers Panel**.
- **macOS:** On your keyboard, press `Cmd` + `K`.
- **Windows:** On your keyboard, press `Cmd`+`K`.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../25-settings-preferences/01-settings-preferences.md):
>
> - **General>Prefer to keep selection after delete**
> - ***Tools>Select object when intersects with selection marquee**
> - **User Interface>Auto-scroll to show selection in Layers panel**

#### SEE ALSO:

- [Selecting objects by attribute](02-selecting-objects-by-attribute.md)
- [Move Tool](../20-tools/01-layout-tools/01-move-tool.md)
- [Grouping objects](03-grouping-objects.md)
- [Layers panel](../21-panels/14-layers-panel.md)
- [Selecting and editing layers](../08-layers/04-selecting-and-editing-layers.md)
- [Select and view pages](../05-pages-spreads-and-sections/07-select-and-view-pages.md)
