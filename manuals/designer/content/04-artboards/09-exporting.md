# Exporting artboards

Artboards can be exported as individual images or all the artboards in a document can be exported together as a single image.

If you select an artboard before proceeding to export, the selected artboard will automatically be selected in the Export dialog. However, all artboards in the current document are available for exporting from the Export dialog at any time, regardless of selection.

If you choose to export the entire document, all artboards in the document will be included in the exported image. The resulting image dimensions will be based on the smallest possible size relative to each artboard's size and position on the pasteboard. In other words, the smaller the artboard sizes and the closer they are together, the smaller the overall image's dimensions. For this reason, we advise exporting artboards in separate documents for print, web, and apps.

For more information on exporting an entire document, see the [Export](../14-saving-and-sharing/03-export.md) topic.

## Export Persona

Slices (export areas) are automatically created for individual artboards, allowing you to access all the features available in [Export Persona](../15-exporting/01-exporting-using-export-persona.md).

**To export an individual artboard:**

1. (Optional) [Select an artboard](03-selecting-moving-and-resizing.md).
2. From the **File** menu, select **Export**.
3. Adjust the settings in the dialog.
4. From the **Area** pop-up menu, select a named artboard. (This step is not necessary if the above optional step was followed.)
5. Click **Export**.

**![Export](../../assets/shared/ui/exported.png)

 To export an artboard using Export Persona:**

1. (Optional) On the [**Export Options** panel](../15-exporting/02-export-options-panel.md), adjust export settings as appropriate for artboard slices selected in the Slices panel.
2. On the [**Slices** panel](../15-exporting/03-slices-panel.md), adjust settings as appropriate for each artboard slice by expanding the artboard slice entry. You can:
   - Add other file formats for export.
  - Add additional size scalings (e.g., x3) or absolute sizes (100w) for the slice's export format.
  - Rename files for export.
  - Export specific sizes and formats selectively.
3. Click **Export Slices (*n*)** at the bottom of the panel to export all checked items.
4. Navigate to and select the storage folder for the exported image(s) and then click **Export**.
5. (Optional) On the **Slices** panel, select **Continuous** if you want to automatically re-export export areas if the document is subsequently changed. This option is only available if **Export Slices (*n*)** was selected above.

#### SEE ALSO:

- [Artboards](01-about-artboards.md)
- [Export](../14-saving-and-sharing/03-export.md)
- [Exporting using Export Persona](../15-exporting/01-exporting-using-export-persona.md)
