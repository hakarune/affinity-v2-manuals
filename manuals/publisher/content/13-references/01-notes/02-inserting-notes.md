# Inserting notes

Footnotes, sidenotes and endnotes are inserted into documents using the **Notes** panel.

Upon inserting a note:

1. A reference is added at the insertion point.
2. Space for a note body is allocated at an appropriate position for the note's type.
3. The insertion point is moved to the note body's position so you can enter text.

## Note order and serialization

Affinity Publisher automatically determines which reference is used to label a note, based on its position relative to other notes of the same type.

The correct serialization is maintained when new notes are inserted, or existing notes are moved or deleted.

For example, inserting an endnote between endnotes labeled 3 and 4 will result in the references of endnotes 4 and higher to be incremented by 1, and the new endnote's reference will be 4.

**To insert a footnote, sidenote or endnote:**

1. Position the insertion point where you want the note's reference to be.
2. On the **Notes** panel, select the required type: **Footnotes**, **Sidenotes** or **Endnotes**.
3. Click **Insert Note**. The document view will refocus on the newly created note body.
4. Type the note body's text.

> **Tip:** Inserting a note when a range of text is selected causes the note's reference to be positioned after the selection's last character.

**To delete a footnote, sidenote or endnote:**

1. Do one of the following:
  - Position the insertion point after the note's reference in story text.
  - Select the note's reference.
2. Press the `Backspace`  to delete the reference and corresponding note body.

> **Tip:** Alternatively, for endnotes whose bodies are in a different text frame than their story text, delete the page(s) that contain the endnote bodies to delete them and their corresponding references.

## Navigating notes

The Notes panel allows you to instantly refocus the document view from a note's reference to its corresponding body, or vice versa.

**To move from a note's reference to its body:**

1. In the story text, position the insertion point next to the reference or make a text selection that includes the reference.
2. On the **Notes** panel, click **Go to Body**.

> **Note:** If a text selection encompasses multiple references, clicking **Go to Body** will refocus the document view on the first one's note body.

**To move from a note's body to its reference:**

1. Position the insertion point or make a text selection within the note body.
2. On the **Notes** panel, click **Go to Reference**.

#### SEE ALSO:

- [About notes](01-about-notes.md)
- [Styling notes](03-styling-notes.md)
- [Hyperlinking notes](04-hyperlinking-notes.md)
- [Notes panel](../../21-panels/16-notes-panel.md)
