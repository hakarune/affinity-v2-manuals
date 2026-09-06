# Importing Adobe documents

You can import Adobe Illustrator and Adobe Photoshop files into your Affinity app.

Importing of Adobe documents is a one-way process. You cannot overwrite the original file once it has been imported, instead it is possible to save it as an Affinity document. For Photoshop files, you can 'roundtrip' PSD files by exporting your edited file as a PSD file.

When importing Adobe Illustrator files, Affinity uses the embedded PDF in the file rather than the raw Illustrator data.

Files are imported with layers intact and ready for editing.

**To import Adobe files:**

1. Do one of the following:
   - From the **File** menu, click **Open**.
  - Double-click anywhere in the empty view. (Only available when no other documents are open.) Next, navigate to your file, select it and click **Open**.
  - Open the file containing folder and drag the Adobe file to an off page area of your workspace.
2. Select the file you want and click **Open**.
3. For Illustrator files, from the PDF Options dialog, you can control page import choice, resolution, colour space, text editability and missing font. See [Importing PDF documents](05-importing-pdf-documents.md).

> **Note:** Photoshop and Illustrator files can be easily placed into an existing document via the **Document** menu (**Place**). For multi-page files, each page is placed on its own artboard.

> **Note:** **macOS:**
>
> On opening, a file's colour space is preserved by default, but you can convert it to the default working colour space via **Affinity Designer>Settings** (or **>Preferences**) (Colour option) using **Convert opened files...**. The document's current colour profile is displayed at the top left of your workspace.
>
>
> **Windows:**
>
> On opening, a file's colour space is preserved by default, but you can convert it to the default working colour space via **Edit>Settings** (Colour option) using **Convert opened files...**. The document's current colour profile is displayed at the top left of your workspace.

## About Smart Objects

Smart objects reside on layers with similar pixel information as typical layers, however, they may be edited as stand-alone objects which aids non-destructive workflows. Adjustments, filters, transformations and more can be performed on smart objects in Affinity Apps. When importing Adobe Photoshop files containing smart objects, you can choose to import them and retain their editable functionality. This is instead of them being rasterised on import.

**macOS:**

**To enable Smart Objects import:**

1. On the top menu, click **Affinity Designer 2** to access the app's **Settings** (or **Preferences**).
2. In the **General** section, enable **Import PSD smart objects where possible**.

> **Note:** In Mac OS 13 (Ventura) and later, **Settings** (or **Preferences**) have been renamed to **Settings**.

**Windows:**

**To enable Smart Objects import:**

1. On the top menu, click **Edit** to access the app's **Settings** (or **Preferences**).
2. In the **General** section, enable **Import PSD smart objects where possible**

**To edit a Smart Object:**

1. Select the **Move Tool**, then do one of the following:
   - On the Layers panel, double-click the layer containing the smart object.
  - On the context toolbar, select **Edit Document** or **Replace Document**.

> **Note:** It is possible to save Affinity files as a PSD document type via **File**>**Export** command on the top menu.

> **Preferences:** ### Settings (or Preferences)
>
>
> Related behaviours can be adjusted from [the app's settings](../27-settings-preferences/01-settings-preferences.md):
>
>
> - **General>Import PSD text as text rather than bitmap**
> - **General>Import PSD smart objects where possible**
> - **General>Enable "save" over imported PSD files**

#### SEE ALSO:

- [Open documents and images](04-open-documents-and-images.md)
- [Importing PDF documents](05-importing-pdf-documents.md)
- [Importing CAD documents](07-importing-cad-documents.md)
- [Colour management](../06-colour/04-colour-management.md)
- [Supported file formats](../24-appendix/01-import-and-export-file-formats.md)
