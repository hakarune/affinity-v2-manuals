# Merging and flattening

Merging layers combines multiple layers together. Pixel, vector, mask, adjustment or image layers can be merged into a new merged layer or into the first available pixel layer beneath it in the layer stack.

The entire document can also be flattened to produce a single-layer document.

Once layers have been merged, they become a single layer and their previous contents are no longer separately editable. There are several ways of merging layers.

**To merge all visible layers:**

In the **Layers** panel:

1. Click **Toggle Visibility** to set the visibility of layers in the project.
2. `Click`-click a layer and select **Merge Visible**.

A new layer is added one step above the selected layer. This layer is a merged copy of all visible layers.

**To merge selected layers:**

1. On the **Layers** panel, select multiple layers using `Cmd`-click or `Shift`-click.
2. Do one of the following:
  - `Click`-click any selected layer and select **Merge Selected**.
  - From the **Layer** menu, select the same option.

The selected layers merge down into the lowest layer in the selection.

**To merge a layer with a pixel layer below:**

- On the **Layers** panel, `Click`-click a layer and select **Merge Down**.

The selected layer merges with the first available pixel layer beneath it.

> **Warning:** Any non-pixel layer existing between the layers to be merged will not be included in the merge.

**To create a copy of all visible layers merged:**

1. On the **Layers** panel, click **Toggle Visibility** to set the visibility of layers in the project.
2. From the **Edit** menu, select **Copy Merged**.

A flattened version of the visible layers is added to the Clipboard.

**To flatten all layers:**

- From the **Document** menu, select **Flatten**.

The document will then contain a single flattened layer.

#### SEE ALSO:

- [Create layers](../06-layers/02-creating-layers.md)
- [Keyboard shortcuts for layer operations](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
