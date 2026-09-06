# Accessible PDFs

Affinity allows you to make exported PDF files accessible to users of assistive technologies, such as screen readers. The features allow you to ensure text and descriptions of images are presented in a logical order.

> **Tip:** When exporting to a PDF file, select **Tagged PDF** to include accessibility information—alt text, reading order, and export tags—in the file.

## Descriptions of non-text content

Objects in Affinity documents can be tagged with alt text (meaning alternative) so that assistive technology can describe them to the publication's reader.

You can provide your own alt text or you can use XMP metadata from your placed images. For example, the provider of an image may have embedded a title or description in it.

Objects that are not part of your main content can be marked as decorative so that they are not described by screen readers.

## Reading order

You can specify the order in which qualifying content from your document will be presented to the reader when exported to PDF.

Entries for the following types of objects are automatically included in the reading order:

- Text objects, meaning frame text, artistic text, shape text, and path text.
- Other objects for which you’ve specified alt text.

Initially, reading order is based on objects' positions on the page: from top to bottom, and from left to right when objects have the same vertical position.

The determined reading order may be undesirable. It can be changed by dragging listed items into the required order.

Objects can be grouped into articles to help you manage the reading order. Articles can be renamed, but their names are used only to assist you in Affinity; article names are not carried over to exported PDFs.

Any item can be excluded from the reading order. It'll still be listed in the reading order, but with a cross next to it to indicate its exclusion, and will included again if you change your mind.

## Document structure tags

The relative importance of each text fragment can be indicated to assistive technologies by assigning export tags to your paragraph styles.

Each paragraph style can be indicated as corresponding to a heading (up to level six) or a paragraph.

**To add alt text to an object:**

1. Select the object.
2. On the **Tags** panel, do one of the following:
  - To provide your own alt text, select *Custom*, then type your alt text in the box below.
  - To use metadata from the placed image as alt text, select the field to use: *XMP:Title*, *XMP:Description*, *XMP:Headline*, *XMP:Alt Text (Accessibility)* or *XMP:Extended Description (Accessibility)*.

**To set an object as decorative:**

1. Select the object.
2. On the **Tags** panel, select **Mark as Decoration**.

**To amend the reading order:**

On the **Reading Order** panel:

1. Drag an entry up or down the list.
2. Drop when a blue highlight appears in the required position. This can be a blue line displayed between items, or a blue highlight on an article’s entry.
3. If you dropped on an article and the item is in an incorrect position within it, repeat these steps.

**To exclude an item from the reading order:**

On the **Reading Order** panel:

- Click the check mark at the right of the item's entry. It will change to a cross to indicate exclusion.

**To create an article (group) in the reading order:**

On the **Reading Order** panel:

1. (Optional) Select the items you wish to group by `Cmd`-clicking each one.
2. Select **Add Article**.
3. (Optional) Give the article a more meaningful name, click it to select it, then click its name, type a new name, and press `Return`.

Items in an article can be reordered by dragging them up or down the list.

Items can be removed from an article by dragging to a position in the list that's outside of the article, or by deleting the article to move all its contents to the list's top level.

**To assign a document structure tag to a paragraph style:**

1. On the **Text Styles** panel, click on the required style's options menu and select **Edit "<style name>"**.
2. On the dialog that appears:
  1. Select **Export Tags**.
  2. Under **PDF**, set **Export Tag** to the required value: *P*, any of *H1* through to *H6*, or *[No change]* to inherit from the parent style, if this style has one.

**To include accessibility information when exporting to PDF:**

On the **Export** dialog:

1. Select **PDF**.
2. Ensure **Tagged PDF** is checked.
3. Set other PDF export settings as required.
4. Select **Export**.
5. Provide a filename for the PDF, navigate to where you wish to save the file, then select **Save**.

#### SEE ALSO:

- [Publishing PDF files](01-publishing-pdf-files.md)
- [Reading Order panel](../../21-panels/22-reading-order-panel.md)
- [Tags panel](../../21-panels/31-tags-panel.md)
- [Text Styles panel](../../21-panels/33-text-styles-panel.md)
-
