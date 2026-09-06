# Using text styles

Text styles can be applied to text within your publication for efficiency and consistency.

## About text styles

A text style is a set of one or more text attributes which can be applied to text in bulk. An attribute could be a typeface, trait (bold, italic), font size, spacing, alignment to name only a few. Later, if you chose to modify a text style, any text which uses that style will update to conform to the attribute changes you've made.

Every new document comes with a default set of text styles but the [Text Styles panel](../../21-panels/33-text-styles-panel.md) provides you with the ability to [create and manage a document's text styles](02-creating-and-managing-text-styles.md) as well as [remove them](03-removing-text-styles.md).

Text styles can be applied to text using the Text Styles, Paragraph or Character panels, the context toolbar or a custom keyboard shortcut.

> **Note:** Text styles are assigned to one of three types (paragraph, character and group), but are flexible in how they can be used. For more information, see [Text style types](04-text-style-types.md).

## Understanding local formatting vs character and paragraph style formatting

Local formatting means that you apply a text attribute(s) directly to a character, word or paragraph. These settings are not stored so if you want to do the same to other text you'd have to do it all again. This is fine for smaller passages of text but for longer publications this might be laborious and also create inconsistency. Character formatting overcomes this by saving those attributes to a named character style that can be applied to any text just with one click. When working with paragraphs, you can adopt paragraph styles using the same principles as character styles.

Text styles can be copied and pasted between text by using the **Style Picker Tool**.

**To apply a text style to a paragraph:**

1. With the **Artistic Text Tool** or **Frame Text Tool** selected, click inside a paragraph or drag to select multiple paragraphs.
2. Do one of the following:
  - On the context toolbar, select a text style from the **Paragraph Style** pop-up menu.
  - On the **Paragraph** panel, select a text style from the **Paragraph Style** pop-up menu.
  - On the **Text Style** panel, select a paragraph text style.
  - Use a custom keyboard shortcut.

**To apply a text style to a sentence, word or character:**

1. With the **Artistic Text Tool** or **Frame Text Tool** selected, select a portion of text.
2. Do one of the following:
  - On the context toolbar, select a text style from the **Character Style** pop-up menu.
  - On the **Character** panel, select a text style from the **Character Style** pop-up menu.
  - On the **Text Style** panel, select a character text style.
  - Use a custom keyboard shortcut.

**To remove local formatting:**

1. With the **Artistic Text Tool** or **Frame Text Tool** selected, select a portion of text with local formatting.
2. On the **Text Style** panel, select **Reapply Text Styles**.

## Controlling local and character style overrides

If you have a mix of local and character formatting on a paragraph, and you apply a different paragraph style to that paragraph you can control the override behavior of local and character formatting, i.e whether it is removed or kept.

**To control local/character formatting override behavior:**

1. Select the paragraph.
2. On the **Text Styles** panel, `Click`-click on a chosen style's Options menu and select the behavior you want.
  - **Apply <style> to Paragraphs**—The style is applied; character styles are kept but local formatting (bold,italic, etc.) is removed; paragraph indents and alignment settings are overridden.
  - **Apply <style> to Paragraphs and Clear Character Styles**—The style is applied but local formatting (bold,italic, etc.) and character styles are removed.
  - **Apply <style> to Paragraphs and Preserve Character Formatting**—The style is applied and local formatting (bold,italic, etc.) and character styles are kept; paragraph indents and alignment settings are overridden.
  - **Apply <style> to Paragraphs and Preserve Local Formatting**—The style is applied and local formatting (bold,italic, etc.) and character styles are kept; paragraph indents and alignment settings are kept.

Two additional **Apply <style> to Characters** options let you apply a chosen paragraph style as a character style to selected text—either removing or retaining any local formatting on selected text.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../../25-settings-preferences/01-settings-preferences.md):
>
> - **Miscellaneous>Reset Text Styles**

#### SEE ALSO:

- [Creating and managing text styles](02-creating-and-managing-text-styles.md)
- [Removing text styles](03-removing-text-styles.md)
- [Text style types](04-text-style-types.md)
- [Text Styles panel](../../21-panels/33-text-styles-panel.md)
- [Style Picker Tool](../../20-tools/01-layout-tools/12-style-picker-tool.md)
