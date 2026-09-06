# Table of contents

Affinity Publisher provides the ability to easily insert and manage a table of contents (TOC) for your document.

A table of contents searches the document for text in specified text styles (typically headings) and reproduces that text in a list, normally annotated with page numbers. The document can have as many TOCs as required, but typically a single TOC at the start of your publication is used.

## Planning your TOC position

If you create a document with sufficient pages containing TOC-qualifying headings, you will need to plan out the number of TOC pages to accommodate the automatically generated TOC:

- If the number of headings necessitates a two-page spread, you will need to make room for this at the start of the publication.
- If the number of TOC entries may overflow the frame, link the text frames between page 1 and 2 of your TOC, otherwise manually flow the overflowing text to the second page's frame.

## Using multiple TOCs

When a TOC has been inserted for the document, secondary, section-specific TOCs can be created (for example, TOCs for each chapter of a book). You can generate and present a secondary TOC within a selected section, including all subsequent qualifying headings, or just those within the section.

## Text styles

TOC text styles only show in the **Text Styles** panel when a text frame containing a generated TOC is selected. By default, new TOCs should have their own styles.

Leader tabs can be added as tab stops as part of the style used by the table of contents. The default TOC style can be found in the **Text Styles** panel. Clicking on the style and selecting **Edit** will display the **Edit Text Style** dialog, from which you can adjust the tab stops in the **Tab Stops** section. By default, there will be a single tab stop at position 0 (measured from the right edge). The third menu along sets the leader, and by default there is none. Click on the menu and select **Tab stop leader character** or click the "..." at the end of the row to display a pop-up panel that allows you to pick which character is used for the leader.

﻿﻿

**To generate a table of contents**

1. From the **Text** menu, select **Table of Contents** and then **Insert Table of Contents** to insert a table of contents at the caret.
2. The **Table of Contents** panel (usually accessed via **Window>References>Table of Contents**) will open automatically, allowing you to adjust the format of your TOC.
3. Alternatively, a table of contents can be inserted directly from the **Table of Contents** panel. To do this, open the **Table of Contents** panel, select a table of contents from the **TOC:** pop-up menu and adjust additional panel settings accordingly, then click **Insert** from the top of the panel.

> **Note:** Your TOC is populated with text that has the **Style Name** assigned to it in your document; you can check or uncheck these Style Name entries at the bottom of the panel to include or exclude that style's text, respectively. Don't confuse this with the **TOC Style** setting above these entries which simply creates an identifying prefix for your TOC text styles which format the TOC; these styles are controlled via the **Text Styles** panel. For example, text from the Style Name of 'Heading 1' would be styled with a text style of 'TOC: Heading 1' by default.

**To update your table of contents manually**

1. With a table of contents selected, from the **Table of Contents** panel, click **Update**. Click **Update All Tables of Contents** to update every table of contents in your document.

> **Note:** You will be prompted to update your table of contents on export even if all TOCs are up to date.

**To add leader lines between items and page numbers:**

1. Select a text frame that contains a table of contents.
2. On the **Table of Contents** panel (**Window>References>Table of Contents**), verify the name of the selected **TOC**.
3. On the **Text Styles** panel, double-click the Entry style that matches the TOC's name. For example, TOC 1: Entry.
4. Select **Tab Stops** on the left of the **Edit Text Style** dialog.
5. To the right, click the predefined tab stop's ‘**…**’ button.
6. Next to **Leader**, select the **Tab stop leader character**, **Tab stop leader underline**, or **Tab stop leader strikeout** setting.
7. (Optional) If you chose the leader character setting, type the glyph to repeat along the leader line in the **Character** field.
8. Click **OK**.

#### SEE ALSO:

- [Table of Contents panel](../21-panels/30-table-of-contents-panel.md)
- [Text Styles panel](../21-panels/33-text-styles-panel.md)
