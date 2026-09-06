# Importing InDesign documents

You can import Adobe InDesign documents (IDML) into Affinity Publisher.

## About importing InDesign documents

The importing of documents in Affinity Publisher is a one-way process. You cannot overwrite the original file once it has been imported. Imported documents must be saved as an .afpub file.

Affinity Publisher can import InDesign files that have been saved in IDML (InDesign Markup Language) format, which is available in InDesign CS4 and later. With earlier versions of InDesign, you can export documents to PDF and then import that format directly into Affinity Publisher.

The dpi (dots per inch) setting of the resulting Affinity Publisher document is decided as follows:

- If the imported IDML file does not contain linked or embedded raster resources with their own dpi settings, the document is set to 300 dpi if it's a CMYK document or 72 dpi if it's an RGB document.
- If the imported IDML file contains linked or embedded raster resources, the document is set to whichever of 72, 96, 144, 192, 300, 400 and 600 dpi is closest to the highest dpi setting of all those resources.

A document's dpi setting can be changed at any time in **File>Document Setup**.

> **Note:** You can merge multiple IDML files by going to **Document>Add Pages from File**. See [Merge documents](../13-references/10-merge-documents.md) for more information.

**To import an Adobe InDesign (IDML) file:**

1. From the **File** menu, select **Open**.
2. Select an IDML file and click **Open**.
3. If linked resources are not found, Publisher will ask whether you want to locate them. You can click:
  - **Yes** to locate missing resources one at a time.
  - **Resource Manager** to review missing resources and locate only those required at this time.
  - **No** to open the document without locating anything. Items can be located later by selecting **Window>Resource Manager**.
4. If the document uses fonts that are unavailable, Publisher will warn you and provide a shortcut to [Font Manager](../10-text/06-editing/05-font-manager.md), where you can make substitutions.

> **Note:** Adobe InDesign files can be easily placed via **File>Place**. When placing multi-page documents, you can choose which page you wish to display using the context toolbar.

#### SEE ALSO:

- [Opening documents](02-open-documents.md)
- [Font Manager](../10-text/06-editing/05-font-manager.md)
- [Embedding vs linking](../12-placing-external-content/01-embedding-vs-linking.md)
- [Placing content](../12-placing-external-content/02-placing-content.md)
