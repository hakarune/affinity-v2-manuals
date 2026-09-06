# Applying filters

Filters can be applied to layers within your document for corrective or creative purposes.

## About filters

In Affinity Photo 2, filters are available in both non-destructive and destructive forms. A variety of filters are available as [live filters](../06-layers/08-using-live-filters.md) which are non-destructive.

As well as to pixel layers, you can apply destructive filters to mask layers, adjustment layers, live filter layers and masked fill layers; spare channels can also take destructive filters too.

For destructive filters, it's a great idea to make a duplicate layer of the layer you planned to work on. By applying a filter to the duplicated layer, you preserve the original layer's contents, with the option to hide the 'filter' layer as needed.

> **Note:** If a selection is in place before the filter is applied, the filter will only affect pixels within the selection.

## Available filters

Filters are organized into the following categories.

- [Blur](02-blur-filters.md)
- [Sharpen](07-sharpen-filters.md)
- [Distort](04-distortion-filters.md)
- [Noise](06-noise-filters.md)
- [Detect](05-edge-detection-filters.md)
- [Colors](03-color-filters.md)
- [Astrophotography](01-applying-filters/01-astrofilters.md)
- [Lighting/Tonal](01-applying-filters/02-tonalfilters.md)

### Settings

The following general settings are available from all filter dialogs:

- **Before/After**—when selected, a dividing line is displayed over the document to show a before and after preview. Drag the dividing line to reposition it. Available on destructive filters.
- **Cancel**—exits the dialog without applying the changes to the filter.
- **Apply**—exits the dialog and applies the filter settings to the layer.

**Live** filters have these additional settings:

- **Delete**—closes the dialog and deletes the filter layer, removing the filter from the image.
- **Merge**—merges the current filter layer with the layer immediately below it in the layer order.
- **Add Preset**—adds the current settings as a preset for use with later images and projects.
- **Reset**—reverts all dialog settings to default.
- **Opacity**—how see-through the filter layer is.
- **Blend mode**—changes how the applied pixels interact with existing pixels on the layer below. Choose mode type from a pop-up menu.

**To apply a filter:**

1. On the **Layers** panel, select a layer (we recommend that this is a duplicate layer).
2. Select the filter from the **Filters** menu.
3. If a dialog appears for the filter, follow the steps below:
  1. Adjust the settings in the dialog. (The strength of some filters, including most of the Blur category, can be set higher than their dialog allows. To do so, drag right on the canvas.)
  2. Click **Apply**.

> **Note:** Not all filters have a dedicated dialog or customizable settings.

**To fade a filter's results:**

The **Fade** command becomes available when the most recent edit to the selected layer was made using a destructive filter or tool. The command blends the result of that edit with the layer's previous appearance. The result replaces the layer's current contents.

1. On the **Layers** panel, select a suitable layer.
2. Select the **Fade** command from the **Layer** menu.
3. In the dialog that appears, use the **Fade** slider to control the blend between the layer's current and previous appearances.
  - Set a value closer to 0% to make the layer's previous contents more visible than its current contents.
  - Set a value closer to 100% to make the layer's current contents more visible than its previous contents.
4. (Optional) Select an alternative **Blend Mode** to alter how the pixels of the layer's previous and current contents interact.
5. Click **Apply**.

**To apply a live filter from the Layers panel:**

1. On the **Layers** panel, select a layer.
2. Click **Live Filters** and select a filter from the pop-up menu.
3. If a dialog appears for the filter, follow the steps below:
  1. Adjust the settings in the dialog. (The strength of some filters, including most of the Blur category, can be set higher than their dialog allows. To do so, drag right on the canvas.)
  2. Close the dialog to apply.

The filter is clipped to the selected layer, restricting its effect to just that layer.

#### SEE ALSO:

- [Blur filters](02-blur-filters.md)
- [Sharpen filters](07-sharpen-filters.md)
- [Distortion filters](04-distortion-filters.md)
- [Noise filters](06-noise-filters.md)
- [Edge detection filters](05-edge-detection-filters.md)
- [Color filters](03-color-filters.md)
- [Lighting/Tonal filters](01-applying-filters/02-tonalfilters.md)
- [Blend modes](../06-layers/05-layer-blending.md)
- [Keyboard shortcuts for adjustments and filters](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
