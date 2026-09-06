# Updating page, list and note numbers

The **Books** panel allows you to specify whether each chapter's page numbering continues from the preceding chapter or starts at a specific number.

Additionally, the panel allows you to update the numbering of lists and of endnotes positioned at the end of the book, so their numbering continues from one chapter to the next.

## About numbering

### Page numbering

When a chapter is added to a book, its page numbering continues from the preceding chapter by default.

Any chapter's numbering can be set to start at a number of your choice. For example, after a book's front matter, which may be numbered using lower-case Roman numerals, the first proper chapter would start at page 1.

### List numbering

When a list is configured (on the **Bullets and Numbering** section of the **Paragraph** panel) to be **Global** and with **Restart Numbering** set to **Manual Only**, the numbering of its items continues from other, earlier lists of their kind in the same document.

Updating list numbering from the Books panel makes such lists continue their numbering from other lists of their kind in earlier chapters, too.

### End-of-book endnote numbering

When endnotes are configured (on the **Positioning** section of the **Notes** panel) to appear at the end of their book, their numbering will continue across chapters if you also set **Restart every** to **Book** in the panel's **Numbering** section. For example, if the first chapter's endnote bodies are numbered from 1 to 4, the second chapter's would then continue at 5, and so on.

## Automatic and manual updating

Affinity automatically updates the numbering of pages, global lists and end-of-book endnotes when a book is output, i.e exported or printed. Numbering also automatically updates while you edit your book's contents—for example, when chapters or pages are added or removed. You can choose to repaginate manually if you prefer.

While editing a book, numbering of global lists and end-of-book endnotes occurs only when you manually request it.

**To choose between automatic and manual updating of page numbers while editing a book:**

1. On the **Books** panel, open the Panel Preferences menu.
2. From the **Update Numbers** submenu, check **Update Page Numbers Automatically** to update automatically, or uncheck it to only update manually as required.

**To choose between automatic and manual updating of all numbers upon output:**

1. On the **Books** panel, open the Panel Preferences menu.
2. From the **Update Numbers** submenu, select **Update Numbers Before Output** for automatic updating or deselect it to update manually as required.

**To manually update page, list, note or all numbers:**

1. On the **Books** panel, select the chapters whose numbering you want to update.
2. From the Panel Preferences menu's **Update Numbers** submenu, select **Page Numbers**, **List Numbers**, **Note Numbers** or **All Numbers**.

#### SEE ALSO:

- [About books](01-about-books.md)
- [Creating books](02-creating-books.md)
- [Synchronizing chapters](03-synchronizing-chapters.md)
- [Outputting books](05-outputting-books.md)
- [Books panel](../../21-panels/03-books-panel.md)
- [Fields](../04-fields.md)
- [Fields panel](../../21-panels/08-fields-panel.md)
- [Bullets and numbering](../../10-text/08-paragraph-level/04-bullets-and-numbering.md)
