# Selecting objects

Before you can move or modify vector objects, you must first select them.

![Selecting objects](../../assets/shared/selecting_objects.png)

> **Note:** The fundamental methods of selecting objects described here are complemented by advanced **Select Same** and **Select Object** commands that [build selections based on object attributes](02-selecting-objects-by-attribute.md), such as object type, fill colour, or stroke width.

## Auto-select

By default, the **Auto-select** option is checked on the context toolbar. As expected, it automatically selects the object and its layer when you click to select it on the page. The option can be disabled if preferred.

You can select single or multiple objects using a variety of methods. If you already have an object selected, you can quickly select the next or previous object in the z-order (stack).

When shapes are created, a base box will be established on creation to accommodate the range of different potential shape sizes when creating variants of that shape. For tighter snapping, you can manually swap to a tight bounding box using the **Cycle Selection Box** option on the **Select** Menu.

## Edit All Layers and Select All

The behaviour of the Select All command depends on the **Edit All Layers** setting on the **Layers** panel:

- When enabled, the command will select all objects across all layers and sub-layers.
- If this option is off, only objects on the current layer are selected. Objects within sub-layers are not selected.

> **Note:** Edit All Layers is enabled by default but can be disabled at any time.

**![Edit All Layers](../../assets/shared/ui/edit_all_layers.png)

 To toggle Edit All Layers:**

- On the **Layers** panel, click **Edit All Layers**.

**![Move Tool](../../assets/shared/ui/move_tool.png)

 To select an object:**

Do one of the following:

- With the **Move Tool** selected, click an object or group on the page to select it.
- On the **Layers** panel, click an object entry.

**![Move Tool](../../assets/shared/ui/move_tool.png)

 To select multiple objects:**

Do one of the following:

- With the **Move Tool** selected, `Shift`-click each object on the page in turn to select them.
- With the **Move Tool** selected, drag to draw a marquee around the object(s).*

**To select all objects in a layer:**

- On the **Layers** panel, click a layer or sub-layer.

**To select all objects on a page:**

- From the **Select** menu, select **Select All**.

**To select other objects in a selected object's z-order:**

Do one of the following:

- With the object selected, on the **Select** menu, choose:
   - **Select Next** / **Select Previous**—selects an object adjacent to the selected object in z-order sequence, within the same layer, group or entire layer stack. The option will cycle selection from bottom to top and vice versa.
  - **Select Top** / **Select Bottom**—as above but selection is made of the top or bottom object in the layer, group or entire layer stack in z-order.
  - **Select Parent**—selects the parent clipping object, layer or group in which the selected object is placed.
- `Click`-click the object, then choose the same options as above from the pop-up menu.

**To control automatic selection behaviour:**

- On the Move Tool's context toolbar, choose one of the following options. These let you optionally select only objects or groups on the page, or just from the Layers panel (on-page selection is prevented).
   - **On (default)**—objects and groups can be selected on the page or Layers panel.
  - **Off**—objects and groups can be selected from the Layers panel only.
  - **Objects**—only objects can be selected on the page, while grouped items will be selected as if ungrouped; layers, groups and objects can be selected from the Layers panel.
  - **Groups**—only groups can be selected on the page; layers, groups and objects can be selected from the Layers panel.

> **Note:** ### Modifier keys
>
>
> When using the **Move Tool**, the following modifier keys can be used to aid layer selection:
>
>
> - With the **Auto-select** option disabled:
>    - `Cmd`-click an object on the page to to temporarily override the option and enable the selection.
> - With the **Auto-select** option enabled:
>    - On the layers panel, holding the `Shift`  and clicking selects multiple objects. The same is achieved by clicking objects on the page whilst holding the key.
>   - Holding the `Cmd`+`Shift` keys while clicking on multiple objects on the page in turn, selects them.
>   - Holding the `Ctrl`+`Shift` keys while clicking on multiple objects on the page in turn, selects them.
>   - `Alt` -click a layer in the panel temporarily disables the whole composition preview leaving only the one (clicked on) selected—helpful in confirming selection of layers in complex compositions.
>   - The `.`  toggles a shape's bounding box between a default Base box and a Regular bounds box; the former accommodates the range of different potential shape sizes when creating variants of that shape; the latter lets you manually swap to a tighter regular bounding box, for tighter snapping control. Alternatively, use **Cycle Selection Box** on the **Select** Menu.
>   - As you drag a selection marquee, pressing the `Ctrl`  selects objects which are only partially covered by the selection marquee. This behaviour can be made the default in Settings (Preferences)*.

> **Tip:** ![Lock/Unlock](../../assets/shared/ui/lock_layer.png)
>
>  You can **Lock**/**Unlock** selected objects from the **Layers** panel or **Layer** menu.

> **Tip:** Locate a layer in the Layers panel, by `Click`-clicking on an object on the page and selecting **Find in Layers Panel**.

> **Preferences:** ### Settings (or Preferences)
>
>
> Related behaviours can be adjusted from [the app's settings](../27-settings-preferences/01-settings-preferences.md):
>
>
> - **General>Prefer to keep selection after delete**
> - ***Tools>Select object when intersects with selection marquee**
> - **User Interface>Auto-scroll to show selection in Layers panel**

#### SEE ALSO:

- [Selecting objects by attribute](02-selecting-objects-by-attribute.md)
- [Move Tool](../22-tools/design-tools/01-move-tool.md)
- [Grouping objects](03-grouping-objects.md)
- [Layers panel](../23-panels/11-layers-panel.md)
- [Selecting and editing layers](../07-layers/04-selecting-and-editing-layers.md)
