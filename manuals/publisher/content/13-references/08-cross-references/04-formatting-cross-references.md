# Formatting cross-references

A cross-reference's text adopts the formatting applied at its position in document text. The formatting can be overridden with your choice of character style, e.g. to add emphasis that distinguishes the cross-reference from other text. Additionally, you can limit the amount of text and which punctuation is displayed by a cross-reference's subfields.

![Formatting options on the Insert Cross-Reference dialog](../../../assets/images/crossrefsInsert.png)
*Formatting and other options on the Insert Cross-Reference dialog.*

The following formatting options are available when inserting or editing cross-references:

- **Style override**—Select an existing character style to override formatting at the cross-reference's position in document text, or apply no override style. From this option, you can also create a new character style or edit the currently selected one.
- **For**—Select whether the **Style override** is applied to *Everything* (all of the cross-reference's text), *All Fields* within the text, or only *Text Fields* or *Number Fields*.
- **Limit subfields**—Check to use the following options to control the length and punctuation of subfield values. Uncheck to display subfield values in full.
  - **Max word count**—Enter the maximum number of words that each subfield will display, if an end character is not encountered sooner.
  - **Add ellipsis**—Check to display an ellipsis (…) at the end of a subfield's text if it has been truncated because the maximum word count was reached. Uncheck to omit the ellipsis.
  - **End characters**—Enter characters that, if any is encountered, will cause the subfield's text to be truncated, even if the maximum word count has not been reached.
  - **Include end character**—Check to include an encountered end character at the end of the text. Uncheck to omit the character.

> **Note:** The **Generate hyperlinks** option specifies whether a cross-reference's field, when the document is exported to an interactive file format such as PDF, can be clicked or tapped to take the reader to the cross-reference's target. It does not affect the formatting of cross-references.

> **Tip:** Commonly used special characters can be added to **End characters** by clicking the downward-pointing arrow on this option.

> **Tip:** To display text in full or until an end character is reached, set **Max word count** to 0.

**To limit text displayed by arbitrary-length subfields:**

1. Check **Limit subfields**.
2. Set **Max word count**, **Add ellipsis**, **End characters** and **Include end character** as required.

> **Note:**
>
> **Limit subfields** is available only when a cross-reference's text contains a subfield whose value is of arbitrary length, i.e. **Section Name**, **Chapter Name**, **Object Description**, **Anchor Name**, or **Numbered Paragraph**.

#### SEE ALSO:

- [About cross-references](01-about-cross-references.md)
- [Setting a cross-reference's target](02-setting-a-cross-reference-s-target.md)
- [Setting a cross-reference's text](03-setting-a-cross-reference-s-text.md)
- [Updating cross-references](05-updating-cross-references.md)
- [Cross-References panel](../../21-panels/07-cross-references-panel.md)
- [About books](../09-books/01-about-books.md)
- [Anchors](../06-anchors.md)
- [Text styles](../../10-text/10-text-styles/01-using-text-styles.md)
- [Preflight](../../14-publishing-and-sharing/05-preflight.md)
