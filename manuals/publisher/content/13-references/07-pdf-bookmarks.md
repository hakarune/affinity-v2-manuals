# PDF bookmarks

When exporting a PDF, you can choose to include bookmarks that help the reader jump quickly to important parts of it without having to scroll or search. For example, the start of every chapter of a book, major articles in a magazine, or important text or figures in a report.

## Making PDF bookmarks

There are two methods for creating PDF bookmarks:

- Manually wherever the **Anchors** panel lets you create an anchor in your document, e.g. within text or attached to an object such as a picture frame, table or shape.
- Automatically from tables of contents created using the **Table of Contents** panel.

The two methods can be used together in the same document.

## Managing PDF bookmarks

PDF bookmarks are a special kind of anchor and so they are primarily managed on the Anchors panel.

Any anchor can be given this special treatment, by checking **Export as PDF Bookmark** when adding a new anchor or clicking the bookmark icon to its right side.

When creating PDF bookmarks from a table of contents, one will be created for every item in the table. Use the panel's bookmark icons to exclude the auto-created PDF bookmarks for any levels you do not want in your PDF. For example, if you want PDF bookmarks only for table of contents items created from Heading 1 and Heading 2 text styles.

> **Tip — Using PDF bookmarks in a reader:** When a PDF is viewed using a compatible reader, its bookmarks are often accessed in a sidebar. In Acrobat Reader, they're in the Bookmarks pane (**View>Show/Hide>Navigation Panes>Bookmarks**).
>
> Other PDF readers might call bookmarks by another name. In Apple's Preview app, for example, select **View>Table of Contents**.

**To manually create a PDF bookmark:**

1. Select the text or object to which you want to attach an anchor.
2. Select **Window>References>Anchors**.
3. Select **New Anchor**.
4. Ensure **Export as PDF Bookmark** is checked and (optionally) rename the anchor.
5. Select **OK**.

**To create PDF bookmarks from a table of contents:**

1. Select the text frame that contains your table of contents.
2. Select **Window>References>Table of Contents**.
3. Check **Include as PDF bookmarks**.

> **Tip — Deleting a table of contents' PDF bookmarks:** If you change your mind about including PDF bookmarks from a table of contents, uncheck **Include as PDF bookmarks** to instantly remove all associated items from the **Anchors** panel.

**To export a PDF that includes bookmarks:**

Affinity Publisher's PDF (digital - small size), PDF (digital - high quality) and PDF (flatten) presets are configured to include bookmarks by default.

1. Select **File>Export**.
2. Select **PDF**.
3. In **File Settings**, set **Preset** as required or manually choose your PDF settings from either section.
4. In **Advanced**, if **Include bookmarks** is not checked, make it so.
5. Select **Export**, and then name and choose where to save the PDF.

#### SEE ALSO:

- [Anchors panel](../21-panels/01-anchors-panel.md)
- [Table of Contents panel](../21-panels/30-table-of-contents-panel.md)
- [Publishing PDF files](../14-publishing-and-sharing/06-pdf-publishing/01-publishing-pdf-files.md)
