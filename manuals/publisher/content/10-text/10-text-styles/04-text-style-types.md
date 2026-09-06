# Text style types

There are three types of text style in Affinity Publisher which are used for differing purposes.

## About text style types

There are no restrictions on what text attributes and properties can be applied to a text style, regardless of its type. Instead, the type determines the predominant purpose of that text style.

There are three types of text style:

- **Paragraph**—used to define the properties of paragraphs.
- **Character**—used to define the properties of individual glyphs (or words, lines and sentences inside a paragraph).
- **Group**—used to define the properties for a group of text styles. Group styles are not applied directly to text. They are listed in the **Text Styles** panel, separately from the other styles, and clicking on them does nothing. Other styles can be based on group styles, which should be used to share formatting between the other styles, and/or as a way of organizing the Hierarchical view in the **Text Styles** panel.

### Paragraph and Character text styles

Although text styles are assigned a type, Affinity Publisher gives you the option of applying paragraph and character text styles flexibly. For example, you can set paragraph styles to selected glyphs as if they are character styles, without affecting the style applied to the paragraph. To activate this feature, you must set the text style to **Show in both panels**.

> **Note:** If a keyboard shortcut is attached to a text style, that shortcut will apply the style using its predominant nature. For example, if you select a portion of text and use a shortcut to apply a paragraph text style, the selected text's paragraph will be modified, not just the selected text.

### Group text styles

A **Group** text style cannot be applied directly to text on the page. Instead it defines the foundations on which other text styles are built and allows you to quickly create a text style hierarchy.

![Options menu](../../../assets/shared/ui/moremenuicon.png) Group text styles only display in the [Text Styles panel](../../21-panels/33-text-styles-panel.md) and are best understood when **Show hierarchical** is set on the panel's Panel Preferences.

The Group style can be considered as the group's parent or master text style. All other styles which are based on a Group style are considered to be child or subordinate styles.

You can create subordinate text styles within a group by selecting the Group text style as the **Based on** style.

![Panel Preferences](../../../assets/shared/ui/moremenuicon.png) You can display text styles in hierarchical groupings by checking **Show Hierarchical** from the **Text Styles** panel's Preferences.

> **Note:** The complexity of your hierarchy is entirely in your hands—subordinate styles can also be master styles with their own subordinates and group styles can be introduced as subordinates to a master group style.

**To edit a text style's type:**

1. On the **Text Styles** panel, click on a listed style's options menu and select **Edit**.
2. In the dialog's **Style** section, select an option from the **Type** list, e.g. Character, Paragraph or Group.
3. Click **OK**.

**To allow flexible use of a text style:**

1. On the **Text Styles** panel, click on a listed style's options menu and select **Edit**.
2. In the dialog's **Style** section, select the **Show in both panels** option.
3. Click **OK**.

The style is available for selection from the Style pop-up menu on the Character and Paragraph panel as well as on the Text context toolbar.

**To create a text style hierarchy:**

1. On the **Text Styles** panel, select **Create Group Style**.
2. Adjust the settings in the dialog.
3. Click **OK**.
4. On the **Text Styles** panel, click on the newly created group style's options menu and select **Create Style Based on**.
5. Adjust the settings in the dialog.
6. Click **OK**.

By default, you'll create another group style within the group, but you can create a Character or Paragraph style type using the settings instead.

#### SEE ALSO:

- [Using text styles](01-using-text-styles.md)
- [Creating and managing text styles](02-creating-and-managing-text-styles.md)
- [Removing text styles](03-removing-text-styles.md)
- [Text Styles panel](../../21-panels/33-text-styles-panel.md)
