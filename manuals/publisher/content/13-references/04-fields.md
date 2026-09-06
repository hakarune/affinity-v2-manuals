# Fields

Fields allow various pieces of information or metadata within your document to be automatically inserted into the document text. Fields will automatically update as data—for example, a date—changes.

## About fields

Fields can be used to insert relevant section information. For example, adding a **Name** or **Page Number** field from the **Fields** panel's **Document Sections** to a master page's footer will automatically display the correct section name or page number, respectively, wherever the master page is applied.

## Inserting fields

Items that may be inserted as fields can be found on the **Fields** panel (accessed by opening the **Window** menu, then selecting **References>Fields**).

Available fields include:

- **Document Information**—displays the **Author**, **Tags**, **Comments**, **Title**, **Subject**, and **Revision**.
- **Document Statistics**—displays key statistics for the document: **Last edited by**, **Created**, **Saved**, **Printed**, **Save Count**, **Filename**, **Path**, and **Total Pages**.
- **Document Sections**—displays the following for each section of the document: **Name**, **Running Header**, **Page Number**, **Last Page** and **Run Last Page**.
- **Continuation**—displays the page number of the **Previous Frame** and **Next Frame** in a sequence of linked text frames, so you can add jump lines to publications.
- **General Information**—displays the current **Date & Time**.
- **Data Merge (*data source file name*)**—dynamically displays fields from a currently connected external data source.
- **Custom**—allows you to create your own fields, whose values can be any text you wish.

> **Note:** The **Author** field is filled in with your user account short name by default. If you do not want this name visible in documents you upload or share, this field can be edited by clicking its value. Editing the **Author** field's value with no document open will make the name you enter the new default.

> **Note:** A number of these fields are also available from the **Text** menu's **Insert** options.

### Converting regular text to fields

Text in a document can be converted to a field, directly from a text selection or via the **Find and Replace** panel.

A text selection can be converted only if it does not:

- include any hard breaks, such as paragraph breaks and section breaks.
- include filler text.
- consist of multiple text ranges.
- produce a blank string of text.

Using the **Find and Replace** panel is useful in a document containing multiple instances of the same text—or similar text, which can be found using regular expressions—that you wish to convert

## Formatting fields

Fields with editable formatting include **Date & Time**, **Created**, **Saved**, **Printed/Exported**, and **Running Header**.

Field formatting can be edited, via the **Fields** panel or the document view.

### Formatting dates and times

Fields that display the date and time can be customized to display any of a wide variety of details. When editing their formatting, select **Custom** and enter the required details in the **Pattern** setting.

The table below lists items supported by the setting. Patterns can be combined as you wish, including with regular text to form longer phrases.

The **Language** setting affects the values shown by each pattern. For example, *MMMM* displays *July* when an English language is selected, *julio* for Spanish, and *Temmuz* for Turkish.

### Dates

| Symbol | Meaning | Pattern | Example value | Notes |
| --- | --- | --- | --- | --- |
| `G` | Era designator | `G`    `GGGG`    `GGGGG` | AD    Anno Domini    A |  |
| `y` | Year | `y`    `yy` | 2023    23 |  |
| `Q` | Quarter | `Q`    `QQ`    `QQQ`    `QQQQ` | 2    02    Q2    2nd quarter |  |
| `M` | Month in year | `M`    `MM`    `MMM`    `MMMM`    `MMMMM` | 9    09    Sep    September    S |  |
| `L` | Standalone month in year | `L`    `LL`    `LLL`    `LLLL`    `LLLLL` | 9    09    Sep    September    S | Some languages use a different spelling of the month in certain contexts, e.g. when a month is mentioned without a date and year. These spellings can be accessed using these patterns. For example, in Polish `MMMM` displays *lipca* for July, whereas `LLLL` displays *lipiec*. |
| `w` | Week of year | `w` | 27 | Consecutive instances of the symbol add a leading zero to the resulting value. |
| `W` | Week of month | `W` | 2 | Consecutive instances of the symbol add a leading zero to the resulting value. |
| `d` | Day in month | `d`    `dd` | 2    02 |  |
| `D` | Day of year | `D`    `DD`    `DDD` | 1    01    001 | Example is 1st of January. |
| `F` | Day of week in month | `F` | 2 | Example is second Wednesday in July.    Consecutive instances of the symbol add a leading zero to the resulting value. |
| `E` | Day of week | `E`    `EEEE`    `EEEEE`    `EEEEEE` | Tue    Tuesday    T    Tu |  |
| `e` | Local day of week | `e`    `eee`    `eeee`    `eeeee`    `eeeeee` | 2    Tue    Tuesday    T    Tu | When the field's language is set to US English, Monday is day 2 as the week starts on Sunday, whereas for UK English it is day 1 as the week starts on Monday. |

### Times

| `a` | AM or PM | `a`    `aaaaa` | PM     p |  |
| --- | --- | --- | --- | --- |
| `B` | Flexible time periods | `B` | at night | Possible values are *in the morning*, *noon*, *in the afternoon*, *in the evening* and *at night*. |
| `h` | Hour in day (1–12) | `h`    `hh` | 7    07 |  |
| `H` | hour (0–23) | `H`    `HH` | 7    07 |  |
| `k` | Hour number in day (1–24) | `k`    `kk` | 4     04 |  |
| `K` | Hour in am/pm (0–11) | `K`    `KK` | 7    07 |  |
| `m` | Minute in hour (0–59) | `m`    `mm` | 8    08 |  |
| `s` | Second in minute (0–59) | `s`    `ss` | 3    03 |  |
| `z` | Short/Long Timezone | `z`    `zzzz` | BST    British Summer Time |  |
| `O` | Time Zone: short localized GMT    Time Zone: long localized GMT | `O`    `OOOO` | GMT-8    GMT-08:00 |  |
| `V` | Time Zone: short time zone ID    Time Zone: long time zone ID    Time Zone: time zone exemplar city    Time Zone: generic location | `V`    `VV`    `VVV`    `VVVV` | gblon    Europe/London    London    United Kingdom Time |  |
| `x` | Time Zone: ISO8601 basic hm    Time Zone: ISO8601 basic hm    Time Zone: ISO8601 extended hm | `x`    `xx`    `xxx` | +01, -0930    +0100, -0930    +01:00, -09:30 |  |

### Other

| `'` | Escape character to include literal text | `'Today is' EEEE` | Today is Tuesday | Surround literal text with apostrophes to display it alongside date and time values in a field. |
| --- | --- | --- | --- | --- |
| `' '` | Two single quotes produce one | `'Today''s date is' dd/MM/yyyy` | Today’s date is 03/07/2023 |  |

> **Tip:** The value of a **Date & Time** field (from the **General Information** fields category) is when the field was inserted into document text.

**To insert a field:**

1. In a text object, create an insertion point or select text that you want to replace.
2. On the **Fields** panel, expand the section that contains the required field.
3. Double-click the required field's name.

> **Note:** The **Text** menu's **Insert**>**Fields**>**Page Number** function will also insert a **Page Number** field into the document.

**To edit formatting of an existing instance of a field:**

1. Do one of the following:
  - -click the field in document text and select **Edit Field**.
  - ![Edit Format](../../assets/shared/ui/DefaultFormat.png) In document text, select the field or create an insertion point immediately before or after it. On the corresponding entry on the **Fields** panel, select **Edit Format** (or **Edit Running Header Defaults** for that field).
2. On the dialog that appears, select your preferred format.

Other instances of the field are unaffected.

**To set default formatting for future instances of a field:**

1. In the document view, ensure that:
  - an instance of the field is not selected.
  - the insertion point is not immediately before or after an instance of the field.
2. ![Edit Format Defaults](../../assets/shared/ui/DefaultFormat.png) On the required field's entry on the **Fields** panel, select **Edit Format Defaults**.
3. On the dialog that appears, select your preferred format.

Instances of the field that you insert afterwards will use your preferred format.

**To convert a field to regular text:**

- In document text, -click the field and select **Expand Field**.

**To convert a text selection to a field:**

1. Select the text range to be converted.
2. -click the selection and then select **Convert Text to Field**.
3. (Optional) Edit the proposed name and value for the field.
4. Select **OK**.

**To highlight fields in document text:**

- From the **Text** menu, select **Highlight Fields**.

**To create a custom field:**

1. On the **Fields** panel, expand the **Custom** section.
2. ![Create Custom Field](../../assets/shared/ui/createCustomField.png) Select **Create Custom Field** (the + button).
3. Type a name and a value for the field into the corresponding boxes.
4. Select **Close**.

**To edit a custom field's value:**

1. On the **Fields** panel, expand the **Custom** section.
2. To the right of the custom field's name, click the existing value (or the blank space if there is no value).
3. Type the new value.
4. Press the  .

> **Warning:** Instances of the field in your document automatically display the new value, and text may reflow accordingly.

**To rename or delete a custom field:**

1. On the **Fields** panel, expand the **Custom** section.
2. ![Edit Custom Field](../../assets/shared/ui/DefaultFormat.png) On the field's entry, select **Edit Custom Field**.
3. Do one of the following:
  - To rename the custom field, click its current name, edit the text, and then press the  .
  - ![Delete](../../assets/shared/ui/trash_can.png) To delete the custom field, select **Delete**.

#### SEE ALSO:

- [Fields panel](../21-panels/08-fields-panel.md)
- [Data merge](11-data-merge.md)
- [Find and replace](../10-text/11-checking-text/02-find-and-replace.md)
