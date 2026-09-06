# Grouping

Layers can be grouped together for easier management and for restricting adjustments or masks to particular layers within your project. Layer groups can be nested together within a 'parent' layer group.

Grouped layers remain together so they can be easily selected, moved and copied. Furthermore, once a layer group is established, adjustments and masks can be applied to the group and will affect all the layers within the group but not those outside the group.

Groups, and nested groups, can be broken apart at any time into their separate layers.

> **Note:** Layer groups display as a nested Group layer on the **Layers** panel.

**macOS:**

> **Tip:** To select nested content directly from the document view, select the **Move Tool**, then hold the  and  s and click an object in the view. From the contextual menu that appears, select any content contained in the same group as (or deeper than) the object you clicked.

**Windows:**

> **Tip:** To select nested content directly from the document view, select the **Move Tool**, then hold the   and right-click an object in the view. From the contextual menu that appears, select any content contained in the same group as (or deeper than) the object you clicked.

> **Note:** For a layer group, the default blend mode is 'Passthrough' (i.e. the group itself has no special blend properties of its own). Please see the [Layer blending](../06-layers/05-layer-blending.md) topic for more information on how this blend mode affects layer groups.

**To create a group:**

1. Select two or more layers. (On the **Layers** panel, `Cmd`-click each layer.)
2. Do one of the following:
  - On the **Layers** panel, click **Group Layers**.
  - From the **Arrange** menu, select **Group**.

**To create an empty group:**

1. With no content selected<sup>1</sup>, do one of the following:
  - From the **Layer** menu, select **New Group**.
  - On the **Layers** panel, click **Group Layers**.

Dragging layers onto the newly created group adds them to it.

<sup>1</sup> When a single existing object, layer or layer group is selected, it is not added to the new group.

> **Tip:** The empty group's initial position in the layer stack is determined by the Insertion options on the Toolbar and whether nothing or a single object/layer or layer group is selected.

**To name a group:**

1. Do one of the following:
  - On the **Layers** panel, double-click the existing group.
  - With the group selected, from the **Layer** menu, select **Rename Layer**.
2. Type a new name.
3. Press `Return`.

You can enable **Ask for name when creating Layers and Groups** setting to be prompted to name them upon creation. This is found in the **Settings (or Preferences)>User Interface** section.

**To ungroup layer content:**

1. On the **Layers** panel, select the layer group.
2. From the **Arrange** menu, select **Ungroup**.

> **Tip:**
>
> **macOS:** You can expand or collapse all nested layers in a group by pressing the `Alt`  and clicking the group layer's arrow.
>
> **Windows:** You can expand or collapse all nested layers in a group by pressing the `Alt`  and clicking the group layer's arrow.

**To release a layer from a layer group:**

Do one of the following:

- Drag the layer out of the group to another layer position.
- `Click`-click the layer, and from the menu, choose **Release**.

**To select a specific layer within a layer group:**

1. On the **Layers** panel, expand the layer group to show its contents by clicking the layer's arrow.
2. Click to select a layer within the group.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../37-settings-preferences/01-settings-preferences.md):
>
> - **Miscellaneous>Reset Object Styles**

#### SEE ALSO:

- [Selecting](02-selecting.md)
- [Isolating](16-isolating.md)
- [Layers panel](../33-panels/13-layers-panel.md)
- [Targeting](15-targeting.md)
- [Keyboard shortcuts for layer operations](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
