# Style Picker Tool

The **Style Picker Tool** allows you to sample style attributes from an object or text and quickly apply them to other objects and text. The tool is located on the **Color Picker Tool** flyout.

## Using the Style Picker Tool

Style attributes are sampled by clicking an object or a character in text. Sampling loads the clicked item's attributes onto the tool.

Sampling from text loads the paragraph style, character style and any local formatting applied at the precise character that is clicked.

Settings on the context toolbar allow you to select which of the loaded style attributes will be applied to other objects and text ranges. Select **All** or **None**. You can also choose any combination of:

- **Stroke**
- **Fill**
- **Layer Opacity**
- **Layer Effects**
- **Character Settings**—character style and any local formatting from the sampled character.
- **Paragraph Settings**—paragraph style and any local formatting from the sampled character.
- **Object Settings**—miscellaneous style attributes not encompassed by the others, such as contours, text frame settings and picture frame settings.

Your selection of attributes on the context toolbar can be modified at any time. For example, you might want to apply all attributes to a shape object but only the fill to artistic text.

The selected attributes are applied by clicking an object or selecting a text range.

> **Tip:** Alternatively, you can firstly select multiple objects and secondly sample style attributes to apply to the selection. This can be advantageous in complex layered documents because the selection can be made using either or both the document view and the **Layers** panel.

With styling loaded onto the tool, you can drag a selection marquee around objects to apply it to them.

### Unloading style attributes

To sample new style attributes, you must unload any currently loaded attributes from the tool. This can be done by clicking **Unload** on the context toolbar or pressing the  . The tool is then ready to sample from a new object or text.

Alternatively, hold down the   and immediately sample from a new object or text.

### Settings

The following settings can be adjusted from the context toolbar:

- **Unload**—when clicked, previously sampled style attributes are discarded, allowing you to sample from a new object or character in text.
- **All**—when clicked, all style attributes on the context toolbar are selected, allowing you to quickly apply all or a large subset of them.
- **None**—when clicked, all style attributes on the context toolbar are deselected, allowing you to quickly choose a small subset of them to be applied.
- **Stroke**—when selected, the loaded stroke style and stroke color will be applied to objects and text ranges you interact with. When deselected, these attributes will not be applied.
- **Fill**—when selected, the loaded fill color will be applied to objects and text ranges you interact with. When deselected, this attribute will not be applied.
- **Layer Opacity**—when selected, the loaded layer opacity will be applied to objects and text ranges you interact with. When deselected, this attribute will not be applied.
- **Layer Effects**—when selected, the currently loaded layer effects will be applied to objects and text ranges you interact with. When deselected, layer effects will not be applied.
- **Character Settings**—when selected, the currently loaded character styles and local formatting will be applied to text ranges you interact with. When deselected, these attributes will not be applied.
- **Paragraph Settings**—when selected, the currently loaded paragraph styles will be applied to text ranges you interact with. When deselected, these attributes will not be applied.
- **Object Settings**—when selected, currently loaded miscellaneous style attributes will be applied (where suitable) to objects and text ranges you interact with. When deselected, these attributes will not be applied.

> **Note — Modifier keys:** When using the Style Picker Tool, the following modifier keys can be used to speed up the workflow:
>
> - The `Alt`  discards the currently loaded style and samples from the clicked object or character.
> - The `Cmd`  applies the currently loaded style to the whole text frame instead of the clicked word or selected text range.

#### SEE ALSO:

- [Selecting colors](../../07-color/06-selecting-colors.md)
- [Layer opacity](../../08-layers/07-layer-opacity.md)
- [Using layer effects](../../17-layer-effects/01-using-layer-effects.md)
- [Styles](../../09-object-control/18-styles.md)
- [Using text styles](../../10-text/10-text-styles/01-using-text-styles.md)
- [Keyboard shortcuts for tools](../../24-keyboard-shortcuts/01-keyboard-shortcuts.md)
- [Settings (or Preferences)](../../25-settings-preferences/01-settings-preferences.md)
