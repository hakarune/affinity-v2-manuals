# Importing add-ons

Add-ons stored as files must be manually imported into Affinity. There are two ways to import them:

- Using the panel or part of the app's interface that corresponds to the add-on's type.
- For files whose extension begins with *.af*, by selecting **Import Content** on the **File** menu.

> **Tip:** As well as Affinity's own file formats, various industry standard file formats can be imported.

> **Note:**
>
> **macOS:** Some content may be provided as one of several add-on types. For example, overlays may be provided as assets that can be dragged from the Assets panel as needed, or as image files that can be dragged and dropped from Finder into your documents.
>
> **Windows:** Some content may be provided as one of several add-on types. For example, overlays may be provided as assets that can be dragged from the Assets panel as needed, or as image files that can be dragged and dropped from Explorer into your documents.

## Add-ons supplied in an archive

Add-ons may be supplied in the ZIP file format or similar and must be extracted before they can be imported.

**macOS:** In Finder, double-click the archive to extract its contents to the same folder as it.

**Windows:** In File Explorer, right-click the archive and select **Extract All**, then follow the on-screen instructions to extract the archive's contents to your required location.

## To import add-ons

For any type of add-on listed in the table below, follow the corresponding steps, then (except for fonts) browse to and select the add-on file to be imported and click **Open**.

| Add-on type | Importable file extensions | Multiple at once? | To import… |
| --- | --- | --- | --- |
| Assets | .afassets |  | On the **Assets** panel, select **Import Assets** from the Panel Preferences menu. |
| Brushes | .afbrushes, .abr | ![check](../../assets/shared/check.png) | On the **Brushes** panel, select **Import Brushes** from the Panel Preferences menu. |
| Document templates | .aftemplate | ![check](../../assets/shared/check.png) | Use your operating system to move the document template files to a folder for long-term storage, then add the folder to the **Templates** section of the **New Document** dialog. |
| Fonts | .affont | ![check](../../assets/shared/check.png) | Drag one or more files from your file manager and drop them onto an Affinity 2 app's window. |
| Fonts | As supported by your operating system, e.g. .otf, .ttf | ![check](../../assets/shared/check.png) | Install using your operating system or third-party font manager. If fonts are unavailable in Affinity, confirm in your font manager that they are enabled, then quit and reopen Affinity. |
| LUTs (Look-up tables) | .cube, .csp, .3dl, .look (one LUT per file) .afluts (one LUT category per file) | ![check](../../assets/shared/check.png) <sup>1</sup> | On the **Adjustment** panel, click the **LUT** adjustment, click **Options**, then do one of the following: For a file that contains one LUT, select **Import LUTs**. For a file that contains a LUT category, select **Import LUT Category**. |
| Macros | .afmacro (one macro per file) .afmacros (one category per file) |  | Do one of the following: For a file that contains one macro, click **Import** on the **Macro** panel. For a file that contains a macro category, select **Import Macros** from the **Library** panel's Panel Preferences menu. |
| Styles | .afstyles |  | On the **Styles** panel, select **Import Styles** from the Panel Preferences menu. |
| Swatches palettes | .afpalette, .ase (Adobe Swatch Exchange), .clr | .afpalette, .ase (Adobe Swatch Exchange) |  |

<sup>1</sup> Either multiple LUT files or multiple LUT category files can be imported simultaneously.

## After importing

When most types of add-on are imported, one or more new categories are created. One of these categories is automatically displayed on the corresponding panel, with the following exceptions:

- An individual LUT file—the LUT is added to the currently selected category on the LUT adjustment.
- An individual macro file—the macro's operations are presented on the Macro panel, from which you can play them or add the macro to the Library panel for later playback.
- A macro category—the category is added to the Library panel and you may need to scroll to see it.

#### SEE ALSO

- [About Affinity add-ons](01-about-add-ons.md)
- [Linking custom content across apps](02-linking-custom-content-across-apps.md)
- [Exporting add-ons](03-exporting-add-ons.md)
- [Creating new documents](../03-get-started/03-create-new-documents.md)
