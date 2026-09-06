# Creating and managing text styles

Text styles can be created in the Text Styles panel, ready for applying to text. They can also be managed and modified to improve your design and workflow.

There are several ways to create a new text style:

1. Build it from scratch—the new text style will have no initial connection to any other text style.
2. Duplicate it from another style—the new text style will initially be exactly the same as the selected text style but has no connection to that style.
3. Base it on an existing style—the new text style will use the selected text style as its base. A connection between the styles is retained and a hierarchy is established.

A text style can be modified in two ways:

- Editing the text style directly.
- Updating the text style to match some selected, locally formatted text.

> **Tip:** You can also set up your own keyboard shortcuts to apply individual text styles to text.

**To create a text style from scratch:**

1. (Optional) Select a portion of text or click inside a paragraph.
2. On the **Text Styles** panel, select:See [Text style types](04-text-style-types.md) for more information.
  - **Create Paragraph Style**—to create a new paragraph style.
  - **Create Character Style**—to create a new character style.
  - **Create Group Style**—to create a new group style.
3. Adjust the settings in the dialog.
4. (Optional) In the **Edit Text Style** dialog, select the **Apply style to selection** option to apply the style to the text selected in step 1.
5. Click **OK**.

**To create a text style from an existing style:**

1. On the **Text Styles** panel, click on a listed style's options menu and select:
  - **Duplicate**—to start with settings exactly the same as the selected style.
  - **Create Style Based on**—to automatically set the dialog's **Based on** option to the selected style.
2. Adjust the settings in the dialog.
3. Click **OK**.

**To edit an existing text style:**

1. On the **Text Styles** panel, click on a listed style's options menu and select **Edit**.
2. Adjust the settings in the dialog.
3. Click **OK**.

**To update a text style:**

1. Select text that is formatted with the text style.
2. Adjust local formatting via the context toolbar, **Character** panel or **Paragraph** panel.
3. On the context toolbar or the **Text Styles** panel, select **Update Paragraph Style** or **Update Character Style** as appropriate.

The text style is updated to match the local formatting.

**To assign a keyboard shortcut to a text style:**

1. On the **Text Styles** panel, click on a listed style's options menu and select **Edit**.
2. In the dialog, select the **Style** section and then click inside the **Keyboard shortcut** box.
3. Press your required key combination.
4. Click **OK**.

> **Note:** ![Already Assigned warning icon](../../../assets/shared/ui/excl.png) If a warning icon appears in the box, the shortcut is already assigned to another action or text style. Hover over the icon to see what that action or text style is.
>
> To remove a keyboard shortcut from a text style, click the cross icon inside the **Keyboard shortcut** box.

### Options

The following options are available in the **Style** section of the **Edit Text Style** dialog:

- **Based on**—sets the default settings for this style. In a hierarchical sense, the Base on text style is the master style to this subordinate style.
- **Next style**—for paragraph styles, this determines the text style automatically applied to the following paragraph (see note).
- **Keyboard shortcut**—sets the keyboard shortcut which will apply this text style.
- **Type**—determines the predominant nature of the text style.
- **Show in both panels**—if this option is off (default), the text style can only be applied in its predominant way (determined by the Type set above). When selected, a paragraph style can be applied as a character style and vice versa.
- **Reapply Text Styles**—removes all the settings applied in the Character, Typography and Paragraph sections of this dialog. The settings in this Style section remain unchanged.

> **Note:** The **Next style** feature is only activated when you press the `Return`  when typing text or when using the **Apply ... Then Next Styles** option in the **Text Styles** panel.

**Additional Edit Text Style dialog options:**

- **Style name**—defines the name the text style will use throughout the app.
- **Character**—assigns character-level attributes to the text style or overwrites those determined by the Based on style. See [Character panel](../../33-panels/07-character-panel.md) for details.
- **Typography**—activates OpenType features for the text style or overwrites those determined by the Based on style. See [OpenType font features](../10-opentype-font-features.md) for details.
- **Paragraph**—assigns paragraph-level attributes to the text style or overwrites those determined by the Based on style. See [Paragraph panel](../../33-panels/19-paragraph-panel.md) for details.
- **Style settings**—lists all the attributes applied to the current text style.
- **Apply style to selection**—applies the current text style to any selected text (if text was selected prior to entering the dialog).

> **Note:** Where **[no change]** is shown, an attribute remains unchanged from the **Based on** style.

#### SEE ALSO:

- [Using text styles](01-using-text-styles.md)
- [Removing text styles](03-removing-text-styles.md)
- [Text style types](04-text-style-types.md)
- [Text Styles panel](../../33-panels/28-text-styles-panel.md)
