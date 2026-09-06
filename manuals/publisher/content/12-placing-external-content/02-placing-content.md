# Placing content

Placing content allows you to add raster and vector images, as well as Affinity documents, PDFs, and PSDs, to your document's pages to enhance your publication.

![Placed content](../../assets/shared/placing_content.png)

> **Note:** You can also place the contents of existing textual documents, such as Microsoft Word and RTF files. See [Importing text](../10-text/07-text-frames/03-importing-text.md) for more information.

## About placing content

A file of a supported file format can be dragged and dropped onto the page to place it.

Alternatively, multiple items can be loaded onto the **Place** panel and then placed, one at a time, in their top-to-bottom order from the panel or in any order you choose.

The selected item on the panel can be placed at its native dimensions or arbitrary dimensions by clicking or dragging in the document view, respectively.

When the **Place** panel is shown, the following settings are available on the context toolbar:

- **Repeat**—Specify the number of times you wish the selected items to be repeated upon placement. Each repeated item is placed once per page, starting at the page on which you click or drag. New pages will be added to your document if necessary. If multiple items are selected, each is repeated before the next in sequence is placed.
- **Replace Existing**—When selected, autoflow is allowed to change the contents of populated picture frames that are unlocked, whereas it will ignore locked picture frames. When unselected, autoflow populates only picture frames that are currently unpopulated.

> **Note:** When a multi-page document or multiple items of any kind are loaded onto the **Place** panel, they can be [autoflowed](03-autoflowing-images-and-documents.md) into your Affinity document.

### Tips for placing content

- Placed images are added as image layers rather than pixel layers. This allows their original image data (e.g., the native resolution, color space and color profile) to be kept. On export to PDF, this data is re-embedded into the PDF file.
- Placed documents offer a **Page Box** option on the context toolbar to choose how the page displays (e.g., with/without bleed, objects only).
- Use the context toolbar's scaling controls to ensure correct sizing of CAD-derived PDFs or PDF/PSD adverts on placement.
- The added content can be rasterized at any time via the **Layer** menu (or via -click).
- A file's embedded color profile will always be converted to the Affinity document's current working space.
- For unprofiled placed images, the color space is assumed to be RGB.

Once placed in your document, you have the option to replace the content, retaining its position, as well as edit placed content.

### Supported file formats for placement

Many industry-standard file formats can be placed.

- Documents
  - Affinity Photo 2/Designer 2/Publisher 2
  - Adobe Illustrator (AI)
  - Adobe Freehand (10 and MX)<sup>1</sup>
  - Adobe Photoshop (PSD)
  - Adobe InDesign (IDML)
  - Microsoft Excel (XLSX)
  - Microsoft Word (DOCX)<sup>5</sup>
  - PDF
  - DWG/DXF
  - RTF<sup>5</sup>
  - Plain text<sup>5</sup>
- Images
  - BMP
  - EPS
  - GIF
  - HEIF/HEIC/HIF<sup>4</sup>
  - JPEG
  - J2K,JP2
  - JPEG-XR/JXR (WDP/HDP)
  - PNG
  - RAW<sup>2</sup>
  - SVG
  - TGA<sup>3</sup>
  - TIFF
  - WEBP
  - OpenEXR
  - Radiance HDR

<sup>1</sup> Multi-page Freehand files open with each page concatenated onto a single page. Add file extension .fh10 or .fh11 to import. Text import is not supported.

<sup>2</sup> Raw images are processed automatically.

<sup>3</sup> Supports transparency.

<sup>4</sup> For iPhone images, the HEIC file may include an upsampled depth map, loaded as an editable second layer. For Canon EOS models (1 DX MkIII, R5 and R6), HIF files (HDR 10-bit PQ-encoded) are supported.

<sup>5</sup> See [Importing text](../10-text/07-text-frames/03-importing-text.md) for information about placing textual documents.

> **Note:** Upon placing a RAW image, Affinity Publisher 2 offers raw image development available via the **Place Tool** and **Move Tool**'s context toolbar. Click **Develop Image** to be taken to a dedicated develop area, where any edits made will reflect live on the placed image. You can re-develop the image too, as required.

### Tips for specific file formats and content

| Content type | Comments |
| --- | --- |
| Affinity Designer files with multiple artboards | You'll be provided with an **Artboard** option on the document's context toolbar so you can choose which artboard is displayed. |
| Affinity documents, PDFs and PSD files | The file will be listed in the Layers panel as either an **Embedded document** or **Linked document** depending on the **Image placement** policy set during initial Document Setup. |
| PSD files | A bitmap representation of the file will be displayed; the file content will not be interpreted. This will generally give better results on output and also negates the requirement to have correct fonts installed. You can still edit the layers of the placed PSD, although if edits are made the file will be interpreted again and its appearance may change (for example, if a font is missing). |
| PDFs, SVGs, PSD and EPS files | If these are placed as embedded documents, you can edit them within Affinity. If edits are made, these files will be converted to Affinity documents and the original data will not be retained; you will not be able to write the embedded file out to its native file format and make it linked. Other features such as using PDF Passthrough will also then be lost. Please note that the Resource Manager will always display the original file's source filename and location should you need to refer back to it. |
| Affinity documents, PDFs, SVGs, PSD and EPS files | If these are placed as linked documents, you will not be able to edit them directly within Affinity. However, any edits made to the files will be picked up by Affinity and will be reported as **Modified** in the Resource Manager. You can then use the Resource Manager's **Update** button to update the files to match the external changes that were made. |
| Multi-page Affinity documents, InDesign (IDML) documents or PDFs | When placing a multi-page document, from its entry on the **Place** panel, you can: use the pop-up menu below the thumbnail to select the single page/spread you wish to place. click the filename to reveal all the document's pages/spreads, then select all that you wish to place, either one at a time or using autoflow. Once placed, you can choose which page or spread you want to display by using **Spread** on the context toolbar. For PDF, only one page can ever be displayed, although you can simulate a spread by duplicating the placed object and choosing a different page to view. |
| Placed PDFs | These offer a **PDF Passthrough** option on the context toolbar, which defaults to Passthrough for exact reproduction within your own PDFs. If that's not possible, the Interpret option is selected and the [Preflight panel](../21-panels/20-preflight-panel.md) lists the [reason(s)](../14-publishing-and-sharing/05-preflight.md). A bitmap preview of the PDF’s contents is displayed while editing your document in Affinity Publisher. |
| Password-protected PDFs | Placing a password-protected PDF will prompt you to enter the file's password. The password is then requested whenever you open the parent document. When the parent document is exported, the resulting PDF does not have to be password-protected. If you wish to protect the exported PDF, ensure you set the required password(s) and restrictions on Affinity's **Export** dialog. |
| Placed PDF, DWG or DXF files containing layers | These offer a **Layers** option on the context toolbar, from which you can choose which of the placed file's layers are visible or hidden in your Affinity document. For example, a layer of a DWG or DXF file might contain notes or more technical information, such as component labeling, that you want to omit for a less technical audience. For PDFs, changing layer visibility will automatically set **PDF Passthrough** to Interpret. |
| Microsoft Excel Workbook spreadsheets (XLSX) | These can be placed directly in Publisher as tables. When placing, click on the page (instead of dragging) to preserve the original appearance of the file. |

**To place a single piece of content:**

1. Do one of the following:
  - Select the **Place Tool**.
  - From the **File** menu, select **Place**.
2. In the pop-up dialog, navigate to and select a file, and click **Open**.
3. (Optional) If the file is a multi-page document, the **Place** panel appears. Select the page/spread you wish to place from the entry on the panel.
4. Do one of the following:
  - Click to place the file at its default, displayed size.
  - Drag on the page to set the size and position of the content.
  - Click on a picture frame to place the item in it.

> **Note:** Alternatively, you can drag and drop a file onto a page. It will be added as a new layer. The current image placement policy (embedded or linked) will be honored.

**To place multiple pieces of content:**

1. Do one of the following:
  - Select the **Place Tool**.
  - From the **File** menu, select **Place**.
2. On the pop-up dialog:The **Place** panel will appear, displaying the items you selected.
  1. Navigate to the file(s) you wish to place.
  2. Select the file(s). Hold the  or   to select adjacent or non-adjacent files, respectively.
  3. Click **Open**.
3. The topmost item on the **Place** panel is automatically selected to be placed next.
4. (Optional) Select a different item.
5. Do one of the following:The selected item is removed from the panel<sup>1</sup>.
  - Click to place the file at its default, displayed size.
  - Drag on the page to set the size and position of the content.
  - Click on a picture frame to place the selected item in it.
6. If the panel contains no more items, it will close automatically. Otherwise:
  - repeat from step 3.
  - press the `Esc`  to cancel further placement and close the panel.

**macOS:**

> **Note:** Alternatively, `Alt`-dragging multiple files from Finder onto a page in the document view will add them directly to the **Place** panel.

**Windows:**

> **Note:** Alternatively, `Alt`-dragging multiple files from Explorer onto a page in the document view will add them directly to the **Place** panel.

**To scale a placed image/document by DPI, percentage scale or to original size:**

1. Select the image or document.
2. From the context toolbar, select the Image/document Info section and choose an **Image DPI** or **Scale** percentage value from the pop-up menu. Alternatively, click **Original Size** to scale to 100% (native dimensions) and reset aspect ratio.

  ![Image scaling](../../assets/images/tbr_context_imagescaling.png)

**To return squashed content to its original aspect ratio:**

- With the content selected, double-click on one of its edge handles to reset its aspect ratio.

**To convert placed content into a picture frame:**

- Right-click on the content and select **Convert to Picture Frame**.
- Alternatively, with the content selected, go to the **Layer** menu and select **Convert to Picture Frame**.

**To edit an embedded document:**

- Do one of the following:
  - In the document view, double-click the placed document.
  - From the context toolbar, select **Edit Document**.

> **Note:** The editability of the embedded document may be affected by how the original document was saved in its native app.

> **Note:** Changes are saved within the main document without affecting the original.

**To replace content:**

1. Select placed content.
2. From the context toolbar, select **Replace Image** or **Replace Document** depending on what you've placed.
3. Select a replacement file from the file browser window and click **Open**.

#### SEE ALSO:

- [Autoflowing images and documents](03-autoflowing-images-and-documents.md)
- [Placing images from the Web](04-placing-images-from-the-web.md)
- [Place Tool](../20-tools/01-layout-tools/06-place-tool.md)
- [Embedding vs linking](01-embedding-vs-linking.md)
- [Resource Manager](06-resource-manager.md)
- [Linked Services](07-linked-services.md)
- [Color management](../07-color/04-color-management.md)
- [Importing text](../10-text/07-text-frames/03-importing-text.md)
