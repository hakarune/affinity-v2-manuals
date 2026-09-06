# Color panel

The **Color** panel is used to choose color for various tools and selected objects.

> **Note:** A pop-up version of the Color panel may appear when choosing color from within other dialogs.

## About the Color panel

The **Color** panel can operate in several color modes—HSL, RGB, RGB Hex, CMYK and LAB—and has various ways of defining color—color wheel (HSL only), color boxes and color sliders. Color tints can also be applied from within the panel.

![Color panel](../../assets/images/panel_clr_wheel.png)
*Color panel (CMYK sliders): (A) Set Stroke/Set Fill color selectors with color 'none' swatch and 'swap' arrow, (B) Switch to opacity/noise, (C) Panel Preferences (D) Color Picker and picked color swatch, (E) Color sliders, (F) Opacity controls, (G) Noise controls.*

Like the **Swatches** panel, the Color panel takes on different appearances depending on the active Persona and on the selected tool. The large color selectors indicate the currently selected colors.

- In Publisher and Designer Personas, objects have fill and stroke color properties. The stroke color is represented by the cutout (donut) color selector. The fill is represented by the solid color selector.
- In Photo Persona, the two solid color selectors indicate interchangeable Foreground and Background colors.

The active color selector is shown at the front of the two color selectors. Choosing a new color will apply it to the active color selector.

> **Note:** ![Gradient Tool](../../assets/shared/ui/fill_tool.png) The **Gradient Tool** only shows a single color selector swatch which represents the color of the currently selected stop on the gradient.

## Using the Color panel

With the **Color** panel, colors can be applied to an object or for use by a tool in just a few clicks. Opacity and noise are further color attributes which can be applied.

**To set the color of a selector:**

1. Click the selector you want to apply the color to. It will show at the front of the two color selectors.
2. Do one of the following:
  - Choose a color from the color model's **Wheel** (HSL only), **Sliders**, or **Boxes**.
  - Click the picked color swatch.
  - Click the **None** swatch to make the color completely transparent (for the tool, fill or stroke).

**To switch colors between the selectors:**

- Click the double-headed arrow. The colors switch (but the active swatch selector remains the same.)

**To adjust opacity or noise setting:**

1. Select the toggle button to the bottom-left of the panel.
2. Drag the slider to set the value.

## Color selection preferences and color models

![Panel Preferences](../../assets/shared/ui/moremenuicon.png) When choosing colors in the Color panel, you can choose from various selection preferences and color model values. The color selection preferences are changed in the Panel Preferences menu.

Depending on the color model selected, you can also choose to work in **8 bit**, **16 bit** or **Percentage** mode.

Some of the selection methods allow you to set color using values other than RGB. This doesn't change the working color profile of the document, but changes the input values for the colors.

> **Note:** You can specify color values for RGB, RGB Hex, HSL, CMYK and Grayscale depending on the pop-up menu in the Color panel. This is not the same as the working color profile. For example, if your working profile is an RGB profile, choosing 100% K (black) from the CMYK color model doesn't convert your document to CMYK. Instead the color applied will be an RGB approximation of 100% K (black). However, if you convert or export the document to a CMYK profile, the 100% K (black) will be honored.

![Panel Preferences](../../assets/shared/ui/moremenuicon.png) The following color selection preferences are available from the Panel Preferences menu.

- **Wheel**—HSL Color Wheel
  - Drag on the outer ring to set the hue, and drag in the triangle to set saturation and lightness.
  - Click a swatch to the right of the wheel to select a recently used color.
  - Enter an RGB Hex value into the **#** setting.
- **Sliders**—RGB, RGB Hex, HSL, CMYK, LAB, Grayscale
  1. Select the color mode from the pop-up menu.
  2. (Optional) From the Panel Preferences menu, select **8 bit**, **16 bit** or **Percentage**.
  3. Drag sliders or type directly into the value boxes to set the color values.
- **Boxes**—Hue, Saturation, Lightness only
  - **Hue**—Drag on the hue slider to set the hue, drag in the box to set the saturation and lightness.
  - **Saturation**—Drag on the saturation slider to set the saturation, drag in the box to set the hue and lightness.
  - **Lightness**—Drag on the lightness slider to set the lightness, drag in the box to set the saturation and hue.
- **Tint**
  - Drag the slider to control the color tint. The further to the left the slider is positioned, the less ink is applied to the page.

The HSL color wheel's Saturation/Lightness control can be changed from **Triangle** to **Square** via the Panel Preferences menu.

![Lock/Unlock](../../assets/shared/ui/lock_layer.png) By default, the color space is locked when using **Sliders** (e.g., CMYK sliders) to prevent it from changing. This avoids inadvertently swapping to another mode after using swatches or selecting a different object created with a different color mode. When unlocked, the Color panel will remember the color mode that the selected object was created in.

> **Tip:** On the **HSL Color Wheel**, -dragging the outer Hue ring will snap to 45° intervals.

> **Tip:** -dragging a **Color** panel slider will move all of the sliders at once (for RGB and CMYK color space only). This can be useful for deciding on a lighter or darker shade of the color in place.

## Using the Color Picker

The picker lets you sample colors within or outside Affinity Publisher, then use them in your design.

**To use the Color Picker:**

1. (Optional) Select an object to adopt the picked color on picking.
2. Click the selector you want to apply the color to.
3. Drag the **Color Picker** to the color you want to sample.

## Saving chosen colors for later use

Once your color has been chosen and applied to a tool or object, there are several ways to preserve this color for later use.

![Panel Preferences](../../assets/shared/ui/moremenuicon.png) The following options are available from the Panel Preferences menu.

- **Copy Color to Clipboard as Hex**—this calculates the current color's Hex value and adds it to the clipboard. This is useful for web developers, to standardize on colors between graphics and HTML coding in a web environment.
- **Add Color to Swatch**—adds the current color to the currently loaded palette in the Swatches panel.
- **Add Chord to Swatch** pop-up menu—adds a chord of the current color to the currently loaded palette in the Swatches panel.

#### SEE ALSO:

- [Selecting colors](../07-color/06-selecting-colors.md)
- [Sampling (or picking) colors](../07-color/07-sampling-colors.md)
- [Color Chords](../07-color/11-color-chords.md)
- [Customizing the workspace](../19-workspace/04-customize/02-workspace.md)
