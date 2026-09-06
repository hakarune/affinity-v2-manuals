# Reading Order panel

The **Reading Order** panel allows you to specify the order in which assistive technologies, such as screen readers, will present your document's contents to the reader.

> **Note:** This panel is hidden by default. It can be switched on via the **Window** menu.

![Books](../../assets/images/panel_readingOrder.png)
*The Reading Order panel.*

The panel automatically lists text objects from all pages of your document, and any other objects for which you have set alt text using the **Tags** panel.

Items can be reordered by dragging them up or down the list. They can be grouped into articles to help you more easily manage the reading order.

## Reading order item names

Items are named according to the following rules:

- If the corresponding object's layer has a custom name, that name is also the item name.
- Otherwise:
  - For text objects, the start of the text is used as the item name.
  - For non-text objects which have alt text, the alt text is used for both the item name and the layer name.
  - For non-text objects which don't have alt text, the object's default layer name is used as the item name<sup>1</sup>.
  - For articles, which can be used to group other items, *Article* is used as the default name<sup>2</sup>.

<sup>1</sup> This occurs when an object is manually added to the reading order. You'll need to add alt text for the item to be included in an exported PDF's reading order.

<sup>2</sup> To rename an article, select it, then click it again.

## Settings

The following items are available on the panel:

- **Reading Order**—lists all qualifying objects from your document in the order they will be presented by assistive technologies.
- **Go to Article**—selects the object in the document that corresponds to the selected item in the list. The document view focuses on the object, if it is not already in view.
- **Add Article**—creates a new article. If two or more reading order items are selected, they are added to the article.
- **Add selected object(s)**—adds to the list any objects which are selected but not already in the list.
- **Remove Article**—removes the selected article(s) from the list. If items within an article are selected, they are also removed, otherwise, they are moved to the top level of the list.

#### SEE ALSO:

- [Accessible PDFs](../14-publishing-and-sharing/06-pdf-publishing/03-accessible-pdfs.md)
- [Publishing PDF files](../14-publishing-and-sharing/06-pdf-publishing/01-publishing-pdf-files.md)
