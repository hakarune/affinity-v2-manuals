# Copying and pasting objects

The **Edit** menu provides multiple ways to copy and paste objects. Pasted objects can include/exclude specific copied object properties.

![Paste options](../../assets/shared/pasteOptions.png)
*(A) Paste, (B) Paste Inside, (C) Paste Style (Stroke, Fill and Outer Shadow), (D) Paste FX (Outer Shadow layer effect only), (E) Paste without Format (retains target formatting), (F) Paste Special (Windows only); pastes as a choice of clipboard formats such as SVG, Device Independent Bitmap, etc.*

## About copying

You can copy content throughout the app or externally to third-party apps. Both need a reciprocal pasting operation to add the content to the target page.

## About pasting

As well as the commonly used Paste command, other paste commands can be used to selectively control which object's properties are included/excluded in the paste operation.

| Paste option | Description |
| --- | --- |
| Paste | Pastes objects, preserving the copied object's look and formatting. |
| Paste Inside<sup>1</sup> | Pastes an object inside another object. |
| Paste Style<sup>2</sup> | Pastes copied stroke, fill, layer effects and text formatting/styles<sup>3, 4</sup> to another object/text. |
| Paste FX | Pastes only layer effect(s) to another object. |
| Paste without Format | Pastes unformatted text by stripping the formatting from the copied text. When pasted, the target text will retain its text formatting. |
| Paste Special | Pastes copied content into and out of your Affinity app using a choice of clipboard formats that show dynamically by the type of content copied externally or within Affinity. |

<sup>1</sup> If pasting a single image inside a picture frame, it is positioned within the frame's bounding box and the frame's scaling behavior (Scale to Max Fit, Scale to Min Fit, Stretch to Fit, or None) is applied to it. If pasting multiple images at once, they are clipped by the picture frame and may be positioned outside of its bounding box.

<sup>2</sup> Use the **Style Picker Tool** instead if you want to paste only some of the copied style attributes, e.g. paragraph settings but not character settings and other object styles.

<sup>3</sup> If the copied text contains text ranges with different formatting, the formatting of its first character will be pasted.

<sup>4</sup> If copied text's formatting includes settings that are incompatible with the target text, the incompatible settings will not be pasted. For example, horizontal centering is ignored when pasting onto a range *within* a left-aligned paragraph.

**Windows:**

## About Paste Special

When using **Paste Special** you will be offered a choice of clipboard formats to use for pasting. These options are dependent on the type of content copied and will dynamically change accordingly.

For example, for copied curves and shapes your formats are:

- image/x-inkscape-svg <sup>1</sup>
- SVG <sup>1</sup>
- Portable Document Format
- PNG
- Device Independent Bitmap
- Serif Persona Nodes <sup>2</sup>

For text, the available choices will be different, and may include:

- Unicode text
- Rich Text Format
- Serif Persona Story <sup>2</sup>

<sup>1</sup> These clipboard formats are available when **Copy items as SVG** is enabled via **Settings** (or **Preferences**) (**General** section.

<sup>2</sup> These are proprietary Affinity formats that retain the highest level of fidelity to the original copied object. This format is used by default when copying and pasting between Affinity apps.

**To copy objects:**

1. Select one or more objects.
2. From the **Edit** menu, select **Copy**.

**To paste objects:**

1. Select one or more objects.
2. From the **Edit** menu, select one of the paste options.

> **Note:** *Alternatively, you can cut (rather than copy) the object. From the **Edit** menu, select **Cut**.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../25-settings-preferences/01-settings-preferences.md):
>
> - The **Copy items as SVG** preference [via **Settings** (or **Preferences**) (**General** section)] copies objects in SVG format in readiness for pasting to external apps.
> - The **Preserve Unicode breaks when copying plain text** preference [via **Settings** (or **Preferences**) (**General** section)] preserves paragraph markers, preventing the conversion of line breaks to line feeds in copied text that is pasted to external apps.

#### SEE ALSO:

- [Targeting objects](10-targeting-objects.md)
- [Layer clipping](../08-layers/11-layer-clipping.md)
- [Style Picker Tool](../20-tools/01-layout-tools/12-style-picker-tool.md)
