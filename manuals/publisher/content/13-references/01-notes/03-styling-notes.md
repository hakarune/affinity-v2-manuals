# Styling notes

The **Notes** panel allows you to control various attributes of how footnotes, sidenotes and endnotes are presented.

## Controlling the scope of styling

At the top of the Notes panel, specify how extensively the panel's settings will affect notes of the selected type:

- **Document-wide**—settings affect all notes of the selected type in your document.
- **Custom**—settings affect only notes of the selected type and encompassed by your selection or at the insertion point's position. They are also applied when you insert a note.

### Custom styling

The Custom option allows a subset of notes to deviate from a document's default settings wherever needed. For example, you might use a different number format for a specific story, or apply a different rule color, character style, or paragraph style that does not clash with a specific page's background.

| Text selection/insertion point | Scope (selected note type only) |
| --- | --- |
| A text frame is selected | All references currently within the frame and their note bodies. (Notes in unselected linked frames are not affected.) |
| All of a story's text is selected | All the story's references, and the corresponding note bodies. (Notes in other stories are not affected.) |
| Some of a story's text is selected | Only references encompassed by the selection, and the corresponding note bodies. |
| Insertion point is at a reference in story text | Only the individual reference and its corresponding note body. |
| Selection or insertion point is within a note body | Only that note body and its corresponding reference (prefixed and in the story text). |

## Styling references and note bodies

The availability of Notes panel sections depends primarily on the type of note that is selected at the top of the panel. Some sections are available only when you select certain secondary settings on the panel, as described in the following table’s *Available for* column.

| Section | Available for… | Purpose |
| --- | --- | --- |
| Numbering | Footnotes, sidenotes and endnotes | Note serialization settings, including characters used for references. |
| Format | Footnotes, sidenotes and endnotes | Advanced reference formatting, and character and paragraph styles for references and note bodies. |
| Positioning | Footnotes, sidenotes, and endnotes at **End of Story** | Distances of note bodies from story text and each other. |
| Rules | Footnotes, and endnotes at **End of Story** | Style settings for lines that separate note bodies from story text. |
| Title | Endnotes in **Separate Frame**, **Shared Section Frame**, **Shared Document Frame** or **End of Book** | Words and paragraph style for the heading that precedes endnote bodies. |

> **Note — About notes and Microsoft Word DOCX files:** When a DOCX file that contains footnotes or endnotes is placed, the imported notes are styled using the corresponding document-wide note formatting settings of your Affinity Publisher document.

**To style references:**

1. On the **Notes** panel, select the type and scope of notes you want to style.
2. In story text, position the insertion point/make a selection that encompasses references of the selected note type.
3. On the panel's **Format** section, next to **In main text** and/or **In note body**, set **Number text**, **Number style**, and **Superscript** as required.

> **Note:** If the number field is accidentally removed from **Number text**, it can be reinserted by selecting **Note** from the setting's menu.

**To style note bodies:**

1. On the **Notes** panel, select the type and scope of notes to be styled.
2. Position the insertion point within a note body of the selected note type.
3. On the panel's **Format** section, set **Note body style** to your required paragraph style.

## Visually separating footnote bodies and story text

The Notes panel's **Rules** section allows you to clearly distinguish footnote bodies from the preceding story text by drawing a separating line between them.

Use **Rule before** to choose which of two scenarios the section's other settings will affect:

- **First Note**—rules drawn above groups of note bodies where the first line is a new note.
- **Continued Note**—rules drawn above groups of note bodies where the first line is a continuation of a note body from an earlier page. (A note's reference is not repeated where it continues.)

For each scenario, you can specify whether a rule should be drawn at all, and how it should be styled, sized, and positioned.

## Endnote bodies

When endnote bodies are positioned in a separate text frame after their story text, section, document or book, each is enclosed in zero-width, non-printing note marks (brackets).

The marks are visible by default. To change their visibility, select **Text>Notes>Show Note Marks**.

#### SEE ALSO:

- [About notes](01-about-notes.md)
- [Inserting notes](02-inserting-notes.md)
- [Hyperlinking notes](04-hyperlinking-notes.md)
- [Notes panel](../../21-panels/16-notes-panel.md)
- [Adding sections](../../05-pages-spreads-and-sections/09-adding-sections.md)
