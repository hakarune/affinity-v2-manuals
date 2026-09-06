# Preflight

Affinity Publisher's preflight check feature can be used to ensure that your document exports or prints as intended. The preflight check can be run on demand—e.g. prior to output—or 'live' on a continual basis.

> **Note:** When an .afpub file is opened or created, preflight checking will be set to **Live** by default. When a PDF, .afdesign or .afphoto file is opened, preflight checking will be set to **Never** by default but you can adjust this manually via the **Preflight** panel.

![Preflight](../../assets/images/panel_preflight.png)
*The Preflight panel.*

Preflight checks the contents of your file for errors, ensuring the file is ready for print or export.

## Preflight notifications

With preflight enabled, the bell-shaped preflight indicator in the status bar will change color to indicate whether warnings or errors have been detected in the document.

- ![Preflight indicator disabled](../../assets/shared/ui/preflightIndicatorDisabled.png) Grey indicates that preflight is not enabled, i.e. live checks are not being performed.
- ![Preflight indicator OK](../../assets/shared/ui/preflightIndicatorOk.png) Green indicates that preflight is active and no errors or warnings have been found.
- ![Preflight indicator Error](../../assets/shared/ui/preflightIndicatorErrors.png) Red indicates that preflight is active and errors that will interrupt export have been found.
- ![Preflight indicator Warning](../../assets/shared/ui/preflightIndicatorWarning.png) Yellow indicates that preflight is active and issues that will not affect export have been found.

Hovering over the preflight indicator when it is red will reveal the number of errors preflight has found. Clicking on the indicator takes you directly to the **Preflight** panel.

## Editing the Preflight profile

The **Preflight** panel uses a default set of checks, but these can be customized. The **Preflight** panel's ![Options menu](../../assets/shared/ui/moremenuicon.png) **Edit profile** function allows you to tailor preflight checking to your needs. You can control the severity level for preflight issues, set values and thresholds that trigger preflight warnings and errors, and control how placed documents work with preflight.

## Errors and warnings

The **Preflight** panel displays a full list of warnings and errors it has found, allowing you to pinpoint and correct certain errors where they appear in your document.

The types of items that are listed are determined by the active preflight profile's settings. Two different icons may be shown to indicate severity:

- ![Preflight warning](../../assets/shared/ui/preflightWarning.png) A yellow icon to the left of an entry is a warning of an issue that will not affect export.
- ![Preflight error](../../assets/shared/ui/preflightError.png) A red icon to the left of an entry indicates an error in the file that will interrupt export.

The full list of preflight warnings and errors is as follows:

- **Bleed Hazard**—appears when an object is positioned outside of the bleed zone. You can adjust the safe zone edge via the panel, which will change what preflight checking will identify as a bleed hazard.
- **Check copy**—appears if a preflight user comment has been attached to an object. Can be used as a reminder to, for example, check final text copy or to check image copyright.
- **Cross-reference out of date**—appears after making certain changes to your document that require a cross-reference's value to be manually updated. Click **Fix** to update the cross-reference.
- **Cross-reference target is missing**—appears if the target of a cross-reference has been deleted from the document, e.g. an anchor has been removed.
- **Cross-reference book target is missing**—appears if the target is in a book chapter that is not open for editing, and so nothing more about the target is known.
- **Cross-reference target is not a list**—a cross-reference contains a **List Number** subfield but its target is not an item in a numbered or bulleted list.
- **Cross-reference target is not a note**—a cross-reference contains a **Note Number** subfield but its target is not a footnote, sidenote or endnote.
- **Cross-reference target is not in a book**—a cross-reference contains a **Chapter Name** subfield but its target is not a book chapter.
- **Cross-reference expansion includes itself**—a cross-reference contains a **Paragraph Body** or **Numbered Paragraph** subfield whose value includes the cross-reference's text.
- **Cross-reference target is not in text**—a cross-reference contains a text-based subfield, such as **Paragraph Body**, but its target is not text. For example, the cross-reference is linked to an anchor on a shape or image.
- **Cross-reference has no string for language**—a cross-reference contains an **Above/Below** subfield but translations have not been set for the text's language. Translations can be set via **Edit Strings** on the **Cross-References** panel's Preferences menu.
- **Cross-reference value is empty**—a cross-reference contains a subfield for which its target provides no value, e.g. a **Paragraph Body** subfield when the cross-reference's target is an empty paragraph. This check is optional and can be disabled by editing the preflight profile, selecting **Cross-References**, and then unchecking **Check for empty values**.
- **Data merge sources need updating**—appears when a data record(s) in the external data source has been edited. Click **Fix** to update to the latest records.
- **The document index needs updating**—can be resolved by using the **Index** panel to update the index.
- **Field (field name) not found in source (data source file name)**—appears when a row or column in the external data source has either been renamed or deleted.
- **Fill ink density too high (Percentage)** / **Stroke ink density too high (Percentage)** / **Text ink density too high (Percentage)**—appears when an object uses a color with an ink density over a specified threshold.
- **Fill uses too rich black (Percentage)** / **Stroke uses too rich black (Percentage)** / **Text uses too rich black (Percentage)**—appears when an object uses a rich black ink density over a specified threshold.
- **Fill uses CMY** / **Stroke uses CMY** / **Text uses CMY**—appears when an object's Cyan, Magenta or Yellow levels do not conform to the document's expectation of only gray and spot colors.
- **Frames in flow have mismatched scales**—appears when one or more of a story's text frames has been scaled. Double-click the warning to go to the first frame in the linked sequence, then follow the text flow to locate any frames on which the lower-right handle is solid. Double-click the handle to reset the frame's scale.
- **Hidden Object**
- **Hyperlink to Invalid Anchor (anchor name)**—appears where a hyperlink's anchor is missing or has been deleted.
- **Hyperlink to Invalid Page**—appears where a hyperlink's target page is missing or has been deleted.
- **Linked resource is missing/Linked resource is out of date**
- **Mismatched color space (RGB)**
- **Missing characters (character)**—appears when text uses a glyph that is not present in the currently applied font.
- **Missing Font**—appears if the document is opened on a device that does not have the used fonts available.
- **Non-Proportional Scaling**—appears when an object is not proportionally scaled, e.g. when an image has been accidentally squashed.
- **Object missing Alt Text**—appears when alt text has not been specified for an object and the object has not been marked as decoration. The issue can be resolved using the **Tags** panel.
- **One or more table of contents entries need updating**—appears when the TOC is out of date because referenced text in the document has been added to, modified or deleted. Click **Fix** to update the TOC and resolve.
- **Overflowing path text**—appears where there is overset text on a path.
- **Overflowing text frame**—appears where there is overset text within a text frame.
- **PDF passthrough**—a series of different preflight checks for PDF passthrough. These will report as:
  - **Placed PDF has image adjustments applied. The PDF will be rasterized on export.**
  - **Placed PDF has effects applied. The PDF will be rasterized on export.**
  - **Placed PDF has transparency applied. The PDF will be rasterized on export.**
  - **Placed PDF Version (version) is not compatible with the PDF export version. The PDF will be rasterized on export.**
  - **Placed PDF has objects of a color not compatible with the PDF export version. The PDF will be rasterized on export.**
  - **Placed PDF is missing or broken.**
  - **Placed PDF has unsupported page box. The PDF will be rasterized on export.**
  - **Placed PDF has objects of a color different to the document color space. The PDF will still pass through.**
- **Placed image DPI too low**—appears when an image's DPI is too low for the file, with the image's DPI listed in brackets beside the error.
- **Spelling Mistake**
- **Stroke too narrow (Stroke width)**—appears when the stroke width is too narrow.
- Text patterns—a series of different preflight checks for text patterns that are commonly found in edited or imported copy which may cause inconsistency. These will report as:
  - **Multiple spaces**.
  - **Space after Tab**.
  - **Space after break**.
  - **Consecutive breaks**.
  - **Straight quotes**.
  - **Ellipsis with full stops**.
  - **Double hyphen for dash**.
- **Unnamed Anchor**—An unnamed anchor has been generated, e.g. as a consequence of document content with a text style applied that is used to generate a table of contents.

Double-clicking on an issue in the panel will take you to its location in the file. A **Fix** button beside certain issue types allows you to fix them immediately.

> **Note:** Some preflight checks provide a **Look inside placed documents** option. Some warnings/errors about placed documents, such as PDF version compatibility, can be fixed from the parent document but others, such as missing fonts in a placed PDF, require you to have access to the placed document's source file.

If enabled, preflight will be re-run on print and export. If there are errors (not warnings) in the file, a dialog offers the chance to abort the export and go to the **Preflight** panel to review the errors.

## Preflight user comments

Preflight user comments can be added to objects in your publication, creating a custom check to be made prior to print or export. This has many uses, including the ability to:

- Check specific layers are hidden or visible at export.
- Check text and picture frames are populated.
- Check text frames with placeholder text that may need replacing.
- Check images that need copyright checking or creative approval.
- Check images using temporary colors.
- Check copy.
- Ensure copy is approved.

When a user comment is added, it will be listed in the **Preflight** panel to be checked later.

**To access the Preflight panel:**

Do one of the following:

- Click on the Preflight indicator in the status bar.
- On the **Window** menu, select **Preflight**.

**To configure preflight settings:**

- From the **Preflight** panel, click on the **Profile** options menu and select **Edit profile**.
- The **Preflight Profile** dialog will appear. From here, you can establish which issues you wish to check for in your file and how extensive you would like your checks to be.
- After you have finished editing your profile, close the dialog. The **Profile** setting will now display **Custom**.

**To save a preflight preset:**

- From the **Preflight** panel, click on the **Profile** options menu and select **Create preset**.
- Type in a name for your preset and click **OK**.

**To change the bleed hazard safe zone edge:**

- From the **Preflight** panel, click on the **Profile** options menu and select **Edit profile**.
- The **Preflight Profile** dialog will appear. From here, select the **Bleed Hazard** tab.
- Select one of the **Safe Zone Edge** options.

**To enable preflight to check for issues:**

- From the **Preflight** panel, select one of the **Check** options:
  - **Export** will check the file for issues just prior to export.
  - **Live** will actively check the file for issues as you update it.

**To disable error checking:**

- From the **Preflight** panel, go to the **Check** options and select **Never**.

**To check for issues immediately:**

- From the **Preflight** panel, select **Check Now**.

**To view further information on an issue:**

- Hover over the issue in the **Preflight** panel.

**To view an object marked with an issue in the file:**

- Double click on the issue in the **Preflight** panel.

**To automatically fix an issue in the file:**

- Where applicable, click the **Fix** button in the **Preflight** panel.

**To set preflight user comments:**

1. In the document view or on the **Layers** panel, `Click`-click on an object or a layer group and select **Preflight Comment>Set**.
2. Enter a comment into the **Comment** text box, then select **OK**.

**To clear preflight user comments:**

1. In the document view or on the **Layers** panel, `Click`-click on an object or a layer group and select **Preflight Comment>Clear**.

#### SEE ALSO:

- [Create new documents](../04-get-started/01-create-new-documents.md)
- [Publishing PDF files](06-pdf-publishing/01-publishing-pdf-files.md)
