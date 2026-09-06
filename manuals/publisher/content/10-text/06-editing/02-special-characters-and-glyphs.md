# Special characters and glyphs

Special characters and glyphs can be added to your text from any font installed on your computer.

Commonly used items, such as the non-breaking space, non-breaking hyphen and zero-width space, can be inserted via the **Text** menu.

Additional characters/glyphs can be inserted via the **Glyph Browser** panel, which allows you to insert glyphs, Unicode characters or Unicode characters with alternates.

Alternatively, you can type a character's Unicode character code or glyph ID (GID) and then tell Affinity to convert it to the actual character.

> **Warning:** Glyphs of the same hexadecimal character code or GID may be different between fonts. Applying a new font to text may cause some characters to be displayed as rectangles or not at all, which indicates no glyph is defined for the affected character codes within that font.

Commonly used characters available via **Text>Insert**, each with its Unicode character code where available:

| Category name | Character name | Displayed character | Unicode character code |
| --- | --- | --- | --- |
| Symbols | Bullet | • | U+2022 |
|  | Dagger | † | U+2020 |
|  | Double Dagger | ‡ | U+2021 |
|  | Ellipsis | … | U+2026 |
|  | Inverted Question Mark | ¿ | U+00BF |
|  | Inverted Exclamation Mark | ¡ | U+00A1 |
|  | Copyright | © | U+00A9 |
|  | Trademark | ™ | U+2122 |
|  | Registered Trademark | ® | U+00AE |
|  | Paragraph Marker | ¶ | U+00B6 |
|  | Section Marker | § | U+00A7 |
| Maths | Plus Minus | ± | U+00B1 |
|  | Multiply | × | U+00D7 |
|  | Divide | ÷ | U+00F7 |
|  | Approximately Equal | ≈ | U+2248 |
|  | Not Equal | ≠ | U+2260 |
|  | Less Than or Equal | ≤ | U+2264 |
|  | Greater Than or Equal | ≥ | U+2265 |
|  | Degree | ° | U+00B0 |
|  | Per Mille | ‰ | U+2030 |
|  | Pi | π | U+03C0 |
|  | Infinity | ∞ | U+221E |
| Quotation Marks | Double Left Quote | “ | U+201C |
|  | Double Right Quote | ” | U+201D |
|  | Single Left Quote | ‘ | U+2018 |
|  | Single Right Quote | ’ | U+2019 |
|  | Double Base Quote | „ | U+201E |
|  | Single Base Quote | ‚ | U+201A |
|  | Left Guillemet | « | U+00AB |
|  | Right Guillemet | » | U+00BB |
|  | Single Left Guillemet | ‹ | U+2039 |
|  | Single Right Guillemet | › | U+203A |
| Dashes and Hyphens | Em Dash | — | U+2014 |
|  | En Dash | – | U+2013 |
|  | Figure Dash | ‒ | U+2012 |
|  | Soft Hyphen | ‑ | U+00AD |
|  | Non-Breaking Hyphen | ‑ | U+2011 |
| Spaces and Tabs | Em Space |  | U+2003 |
|  | En Space |  | U+2002 |
|  | Non-Breaking Space |  | U+00A0 |
|  | Narrow Non-Breaking Space |  | U+202F |
|  | Zero Width Space |  | U+200B |
|  | Hair Space |  | U+200A |
|  | Sixth Space |  | U+2006 |
|  | Thin Space |  | U+2009 |
|  | Quarter Space |  | U+2005 |
|  | Third Space |  | U+2004 |
|  | Punctuation Space |  | U+2008 |
|  | Figure Space |  | U+2007 |
|  | Zero-Width Non-Joiner |  | U+200C |
|  | Tab |  | U+0009 |
|  | Right Indent Tab |  |  |
|  | Indent to Here |  |  |
| Breaks | Line Break |  | U+2028 |
|  | Column Break |  |  |
|  | Frame Break |  |  |
|  | Page Break |  | U+000C |
|  | Odd Page Break |  |  |
|  | Even Page Break |  |  |

> **Note:** For definitions and typical uses of marks available in **Text>Insert**, refer to [Unicode's General Punctuation character code chart](https://affin.co/unicode).

Other characters you may encounter while editing text:

| Character name | Unicode character code |
| --- | --- |
| Zero-Width Joiner | U+200D |
| Paragraph Break |  |
| End of Story |  |
| Pin position |  |
| Anchor |  |
| Index mark |  |

**To add commonly used special characters/glyphs:**

1. Create an insertion point in your text.
2. On the **Text** menu, select **Insert**, then select the required category and special character.

**To show special characters (paragraph marks, spaces and breaks) in text:**

- On the **Text** menu, select **Show Special Characters**.

**To insert characters using the Glyph Browser panel:**

1. Create an insertion point in your text.
2. On the **Window** menu, select **Text>Glyph Browser**.
3. Select a Font, Font style and Subset from the pop-up menu options.
4. Double-click a glyph to add it at the insertion point.

**macOS:**

> **Note:** Emoji (and other special characters) can be inserted via macOS's **Character Viewer**, which is accessed by selecting **Emoji & Symbols** on the **Edit** menu.

**Windows:**

> **Note:** Emoji can be inserted via Windows' **Emoji** panel, which is accessed by pressing Win+. (full stop).

**To insert a character using its glyph ID or Unicode character code:**

1. Create an insertion point in your text.
2. Do one of the following:
  - For a *glyph ID*: Type 'G+' then enter the required character's ID (in hex), e.g. '02F5' or '2F5'.
  - For a *Unicode character code*: Type 'U+' then the required character code (in hex), e.g. '0040', '040' or '40'.
3. Convert the typed code/ID to the required character by selecting **Text>Toggle Unicode**.

> **Tip:** You can toggle back to hex code by keeping the insertion point at the end of the character and using the same command—in case you've mistyped the code, for example.

> **Tip:** Hover over a character on the Glyph Browser panel to see its glyph ID and Unicode character code. By making a note of either, you can type the character more quickly in future using the above procedure.

#### SEE ALSO:

- [Working with text](../01-working-with-text.md)
- [Glyph Browser panel](../../21-panels/10-glyph-browser-panel.md)
- [Text marks](../11-checking-text/01-text-marks.md)
