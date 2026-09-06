# ![Export Persona](../../assets/shared/ui/export_persona_on.png)

 Exporting using Export Persona

The Export Persona is a dedicated workspace for exporting artboards, layers, groups, and objects as export slices to different file formats and image sizes simultaneously. You'll also be able to export custom drawn slices.

## How it works

The Export Persona uses a combination of panels and tools to create slices. Slices are export areas which you choose to output from your document.

The Layers panel, Export Options panel and Slices panel are used in combination in Export Persona. The Slice Tool is unique to Export Persona and is used to create custom slices.

## Using the Layers panel

The **Layers** panel is different from the Layers panel in Designer Persona. It is used exclusively as a precursor for selecting artboards, layers, groups, or objects from which slices can be created, and added to the **Slices** panel.

When you export a Layers panel item as a slice, the slice will automatically size to what is considered to be the extent of the selected item. A circle symbol at the top right of the slice indicates that it is auto-sized. If you choose to resize the slice, the symbol changes to a square, indicating that the slice has been modified. A resized slice created from a Layers panel item can be reset to 'auto-sized' at any point.

When a slice created via the Layers panel is exported, only content on the layer from which it was created is included in the output.

## Using the Slice Tool

The Slice Tool gives you full freedom to create export areas of all sizes, over any part of your document.

When a slice created with the Slice Tool is exported, content from all visible layers within its area is included in the output.

## Using the Export Options panel

The **Export Options** panel lets you set up your default export settings, or settings for the currently selected item prior to slice creation.

## Using the Slices panel

The **Slices** panel stores all your slices (from the Layers panel or Slice Tool) ready for export directly from the panel. Each created slice has an initial export format (e.g., PNG, JPEG, or SVG) associated with it on creation, with additional export formats being added per slice if needed; each export format lets you export at different size scaling or absolute sizes.

You can use the filenames in the **Slices** panel to specify (or create) a folder hierarchy in which to place your exported files. This is achieved through the use of the forward slash, or oblique, character.

For example, a PNG hero image could be placed within an **img** folder within an **assets** folder using the following syntax: **assets/img/hero**

If any part of the folder structure does not exist, the folder hierarchy will be created when the appropriate slices are exported using **Export Slices (*n*)**.

> **Tip:** You can export the entire document's page using **File>Export** or by selecting the predefined spread area on the **Slices** panel.

## Exported slice dimensions and DPI

When exporting slices via the Export Persona, the slice export size (1x, 2x, 3x, etc.) is linked with your document's DPI. The table below shows how DPI and export size affect export dimensions, using a 64x64 px document as an example.

| DPI setting for a 64x64 document | Export dimensions (in pixels); Exported DPI |  |  |
| --- | --- | --- | --- |
|  | 1x | 2x | 3x |
| 72 | 64x64; 72 | 128x128; 144 | 192x192; 216 |
| 96 | 64x64; 96 | 128x128; 192 | 192x192; 288 |
| 144 | 32x32; 72 | 64x64; 144 | 96x96; 216 |
| 192 | 32x32; 96 | 64x64; 192 | 96x96; 288 |
| 216 | 21x21; 72 | 42x42; 144 | 64x64; 216 |
| 288 | 21x21; 96 | 42x42; 192 | 64x64; 288 |

**To set default export options:**

1. On the **Export Options** panel, select the **Defaults** tab.
2. Adjust settings as appropriate.
3. Jump back to the **Selection** tab when finished.

The settings will be used when your next slice is created.

**![Slice Tool](../../assets/shared/ui/slice_tool.png)

 ![Export](../../assets/shared/ui/export.png)

 To export an area of the document as an image:**

1. Do one of the following:
   - On the **Layers** panel, select an artboard, layer, group or object and click **Create Slice**.
  - With the **Slice Tool** selected, drag on your page to define your export area.
2. Do one of the following:
   - On the [Export Options panel](02-export-options-panel.md), adjust export settings as appropriate.
  - Jump to the [Slices panel](03-slices-panel.md), expand the slice entry and alter the export format or choose an **Export preset** from the pop-up menu (PNG, JPEG, and Apple icon design presets only).
3. (Optional) On the [Slices panel](03-slices-panel.md), click the + icon under the export format entry to add an additional graphic export format.
4. (Optional) On the [Slices panel](03-slices-panel.md), click the indented + icon under the export size entries to add increasing levels of resolution (2x, 3x, etc.) to the export format.
5. Do one of the following, to control what gets exported:
   - Select **Click to export all formats for this item**.
  - Select **Click to export this size**. This exports a specific export format for a slice at a specific size.
  - Click **Export Slices (*n*)** to export all formats and sizes for all checked slices in the Slices panel.
6. Navigate to and select the storage folder for the exported image(s) and then click **Export**.
7. (Optional) On the **Slices** panel, select **Continuous** if you want to automatically re-export export areas if the document is subsequently changed. This option is only available if **Export Slices (*n*)** was selected above.

> **Note:** ### Modifier keys
>
>
> When using the Slice Tool, the following modifier keys can be used:
>
>
> - The `Shift`  constrains the area's proportions to a square.
> - The `Cmd`  if pressed as you drag out a slice area, draws from the centre of the original drag position (can be combined with the `Shift` ).

**![Slice Tool](../../assets/shared/ui/slice_tool.png)

 To reset the dimensions of an manually resized export area created from a layer:**

1. With the **Slice Tool**, select a resized export area.
2. On the context toolbar, select **Revert to auto sized**.

#### SEE ALSO:

- [Layers panel (Export Persona)](04-layers-panel-export-persona.md)
- [Export Options panel](02-export-options-panel.md)
- [Slices panel](03-slices-panel.md)
- [Export](../14-saving-and-sharing/03-export.md)
- [Exporting artboards](../04-artboards/09-exporting.md)
