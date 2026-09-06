# Synchronizing chapters

Affinity can synchronize swatches, text styles, table formats and master pages between a book's chapters to ensure consistent presentation throughout a publication.

## About synchronizable data

Each of a book's chapters contains an independent copy of swatches, text styles, table formats and master pages.

Editing this data in one chapter means that other chapters are out of sync. This may be intentional as part of your design but commonly you'll want to propagate changes to other chapters, e.g. when changing the font size of headings.

The **Books** panel allows you to do this easily when required. The process must be manually invoked but it is the most efficient way to reproduce changes across some or all of a book's chapters.

## About the Style Source Chapter

The first chapter that is added to a book becomes the book's Style Source Chapter, indicated by a key icon to its left. This status means the chapter contains what you consider to be up-to-date swatches, text styles, table formats and master pages.

The designated Style Source Chapter can be changed at any time, providing flexibility in the editing and propagation of data to your selected chapters (target chapters).

When the data in one or more chapters is outdated or incomplete, they can be synchronized with the Style Source Chapter.

## About synchronizing

Synchronization is unidirectional from the Style Source Chapter to target chapters, i.e. it does not alter data in the Style Source Chapter.

Data that exists in a target chapter but not the Style Source Chapter is unaffected by synchronization.

When you synchronize a target chapter with the Style Source Chapter, Affinity considers the following to determine what needs to be copied or updated:

- If a document palette category, text style, table format or master page exists in the Style Source Chapter but not in the target chapter, it is copied from the Style Source Chapter to the target chapter.
- If a named swatch, text style or table format exists in both chapters but has different settings, the target chapter's version is overwritten with the Style Source Chapter's version.
- If a master page of the same name exists in both chapters, the Style Source Chapter's version is copied to the target chapter without affecting the target chapter's version or any applications of it to pages. Both versions' names are unaltered, so consider renaming either or both to help distinguish them.
- If a document palette category exists in both chapters but the target chapter is missing some swatches, those swatches are copied to the target chapter. Swatches that exist only in the target chapter's category are unaffected.

**To set the Style Source Chapter:**

1. On the **Books** panel, select a chapter.
2. From the Panel Preferences menu, select **Set Style Source Chapter**.

**To synchronize data to target chapters:**

1. On the **Books** panel, select one or more chapters that aren't the Style Source Chapter.
2. From the Panel Preferences menu, do one of the following:
  - If you know synchronization settings are as needed, select **Synchronize**.
  - Otherwise, set which data types to synchronize:
    1. Select **Synchronize Settings**.
    2. Check **Swatches**, **Text Styles**, **Table Formats** and **Master Pages** as required.
    3. Click **Synchronize Now**.
    4. Click **Close**.

> **Note:** ![Synchronize Chapters](../../../assets/shared/ui/sync_chapters.png) Alternatively, after selecting chapters, click **Synchronize Chapters** on the panel.

#### SEE ALSO:

- [About books](01-about-books.md)
- [Creating books](02-creating-books.md)
- [Updating page, list and note numbers](04-updating-page-list-and-note-numbers.md)
- [Outputting books](05-outputting-books.md)
- [Books panel](../../21-panels/03-books-panel.md)
- [Swatches panel](../../21-panels/27-swatches-panel.md)
- [Table Formats panel](../../21-panels/29-table-formats-panel.md)
- [Text Styles panel](../../21-panels/33-text-styles-panel.md)
- [Pages panel](../../21-panels/17-pages-panel.md)
