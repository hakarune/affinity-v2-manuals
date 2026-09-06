# Export

The Export dialog provides a streamlined approach to exporting your document or current selection to a common image file format. You can make use of inbuilt presets, or modify advanced export settings and (optionally) create your own presets from them.

The dialog displays a preview of what will be exported, which you can zoom and pan to inspect the effect of your choices. Resize the dialog to preview a larger area of your document at once.

> **Note:** For a more comprehensive set of export options, use [Export Persona](../28-export-persona/01-exporting-using-export-persona.md).

## Password-protected PDFs

When exporting a PDF, you can choose to give it either or both of two types of password: an open password and a permissions password. Exporting with a password encrypts the resulting PDF.

PDF password options are available when the **Compatibility** option is set to *PDF 2.0 (ISO 32000-2)*, *PDF 1.7 (Acrobat 8)* or *PDF 1.6 (Acrobat 7)*. All PDF presets provided with Affinity *except* those for PDF/X output use PDF 1.7 or 1.6 compatibility.

### About open passwords

The content of a PDF with an open password can be viewed only by providing the open password or, if one has *additionally* been set, the PDF's permissions password.

When a PDF has only an open password, there are no restrictions on what people can do with its content. The PDF can be printed or placed in an Affinity document, its content can be modified and selectively copied, and pages can be extracted to create new PDFs.

### About permissions passwords

Setting a permissions password limits what people can do with the PDF unless they are able to provide the permissions password.

Optionally, you can choose to allow specific actions to be performed without providing the permissions password. So, you might choose to allow people to freely open and print your PDF, but not modify or selectively copy its content.

> **Note:** Exporting a PDF with a permissions password *always* disallows page extraction, which could be used to extract content as is from your PDF. This is independent of the **Allow copying of content** setting, which determines whether smaller amounts of content, such as images and text, are copiable.

## Settings

Your choice of file format determines which other settings are presented on the dialog.

Commonly used settings are available in the dialog's **File Settings** section.

The **Advanced** section contains detailed settings for the currently selected format. When these settings are modified, your choices can be saved as a preset.

For descriptions of the complete range of settings and their availability by format, see [Export settings](02-export-settings.md).

> **Tip:** The Export dialog displays an **Estimated File Size** for the exported file(s).

**To export:**

1. From the **File** menu, select **Export**.
2. At the top of the Export dialog, select a file format.
3. Adjust settings in the dialog's **File Settings**<sup>1</sup> section and (optionally) in the **Advanced** section. (All settings are explained in the [Export Settings](02-export-settings.md) topic.)
4. Click **Export**.
5. Enter a filename, choose where to save the file, then click **Save**.

> **Note:** When re-exporting to the same location, clicking **Export** overwrites the existing files.

<sup>1</sup> If one or more layers is selected, the exported file can be trimmed to their boundary by setting **Area** to **Selection Area** or **Selection Only**, which include or exclude all other layers from the output, respectively.

**To create a custom preset:**

1. From the **File** menu, select **Export**.
2. At the top of the Export dialog, select a file format.
3. (Optional) Select a **Preset** as the starting point for your custom preset.
4. Adjust settings in the dialog's **Advanced** section.
5. From the Preset section's options menu, select **Create preset**.
6. Enter a name for your custom preset, then click **OK**.

Consequently, when the corresponding file format is selected on the dialog, the custom preset is available from the **Preset** pop-up menu.

**To rename or delete a custom preset:**

1. From the **File** menu, select **Export**.
2. At the top of the Export dialog, select the preset's corresponding file format.
3. Select the **Preset** you want to rename/delete.
4. From the Preset section's options menu, do one of the following:
  - Select **Rename preset**, enter a new name, then click **OK**.
  - Select **Delete preset**, then click **Delete preset** to confirm.

> **Note — Modifier keys:** When previewing your export, the following modifier keys can be used to zoom in to areas of interest and view the results of different settings applied in the dialog:
>
> - **macOS:** Hold the `Alt`  while scrolling (using a scroll wheel, if available) to zoom in and out of the preview.
> - **Windows:** Hold the `Alt`  while scrolling (using a scroll wheel, if available) to move up and down of the zoomed-in preview.
> - **Windows:** Hold the `Cmd`  while scrolling (using a scroll wheel, if available) to zoom in and out of the preview.
> - Hold the `Shift`  while scrolling (using a scroll wheel, if available) to scroll left or right.
> - Press `Cmd`+ to zoom in by 10% increments.
> - Press `Cmd`- to zoom out by 10% increments.
> - Press `Cmd`+`1` to zoom to 100%, `Cmd`+`2` to zoom to 200%, etc.
> - **macOS:** With the File Settings section collapsed, press `Cmd`+`0` to zoom to fit.
> - **Windows:** Press `Cmd`+`0` (or double-click the image preview) to zoom to fit.
>
> Observe that the modifiers for zooming in/out and panning listed above only work while previewing raster image export formats.

#### SEE ALSO:

- [Export Persona](../28-export-persona/01-exporting-using-export-persona.md)
- [Export Options panel](../28-export-persona/02-export-options-panel.md)
- [Export settings](02-export-settings.md)
- **macOS:** [Share](04-share.md)
- [File formats](../34-appendix/01-supported-file-formats.md)
- [Keyboard shortcuts for file/document management](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
