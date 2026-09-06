# Importing PDF documents

PDF documents can be imported and edited depending on how the PDF was originally exported.

The importing of PDF documents is a one-way process. You cannot overwrite the original file once it has been imported, instead saving it as an Affinity document. However, you can edit the PDF content if page objects remain editable from the original export; you can then export the file as another PDF.

If the PDF document has stored Document Properties (metadata) such as Title, Author, Subject and Keywords (tags) these will be retained on import.

**To import Adobe PDF documents:**

1. Do one of the following:
   - From the **File** menu, click **Open**.
  - Double-click anywhere in the empty view. (Only available when no other documents are open.)
2. Select the file you want and click **Open**.
3. From the PDF Options dialog, you can choose:
   - **Load all pages/Load pages**—All pages or specific pages (by page number) can be imported.
  - **DPI**—sets the resolution for the document. The Estimate option reads and uses the resolution of the PDF file.
  - **Colour space**—sets the document colour space (e.g., RGB or CMYK) that PDF contents will use. The Estimate option senses the PDF file's colour space and uses that.
  - **Favour editable text over fidelity**—if text is to remain more editable at the expense of accurate design reproduction.
  - **Group lines of text into text frames**—If separate text lines can be treated as a single text frame to aid text flow.
  - **Replace missing fonts**—when checked, missing fonts are substituted with the suggested replacement font family/style or a font family/style of your choosing.

> **Note:** For multi-page PDF files, each page is placed on its own artboard.

> **Note:** On importing a PDF that has fonts that are unavailable on your computer, if you choose to check **Replace missing fonts** at this stage, you won't be able to swap the fonts at a later date via **Font Manager**. To replace missing fonts later, ensure you uncheck the option.

> **Note:** Adobe PDF files can be easily placed into an existing document using **File>Place**. When placing multi-page PDFs, you can choose which page you wish to display using the context toolbar.

**macOS:**

**To import Adobe PDF documents (via Finder):**

- Open Finder and drag the PDF file to an off page area of your workspace.

**Windows:**

**To import Adobe PDF documents (via Explorer):**

- Open Explorer and drag the PDF file to an off page area of your workspace.

> **Note:** **macOS:**
>
> On opening, a file's colour space is preserved by default, but you can convert it to the default working colour space via **Affinity Designer>Settings** (or **>Preferences**) (Colour option) using **Convert opened files...**. The document's current colour profile is displayed at the top left of your workspace.
>
>
> **Windows:**
>
> On opening, a file's colour space is preserved by default, but you can convert it to the default working colour space via **Edit>Settings** (Colour option) using **Convert opened files...**. The document's current colour profile is displayed at the top left of your workspace.

#### SEE ALSO:

- [Open documents and images](04-open-documents-and-images.md)
- [Importing Adobe documents](07-importing-cad-documents.md)
- [Importing CAD documents](07-importing-cad-documents.md)
- [Colour management](../06-colour/04-colour-management.md)
- [Supported file formats](../24-appendix/01-import-and-export-file-formats.md)
