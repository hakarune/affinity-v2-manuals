# Selecting colors

There are several ways of choosing colors for your design.

## About selecting colors

An essential requirement for efficient design is the ability to access colors easily and intuitively. Users may have a preferred method for color selection, so Affinity apps provides a choice:

- Context toolbar—for selection of Fill and/or Stroke colors from the context toolbar that displays when a vector object is selected.
- Color panel—for selection from sliders or boxes using different color models, or via an HSL color wheel. Opacity and noise are further color attributes which can be applied.
- Swatches panel—for selection by swatch from different preset or custom categories, including PANTONE® Colors. Colors can be saved to a palette.
- [Color Picker Tool](../20-tools/01-layout-tools/11-color-picker-tool.md)—for [sampling colors](07-sampling-colors.md) anywhere on your screen; great for complementary color work.
- Gradient Tool—apply or edit a color gradient across your object. Choose a gradient type from the tool's context toolbar.

**To apply a fill or stroke color from the context toolbar:**

1. Select the object.
2. From the context toolbar, click either the **Fill** or **Stroke** swatch.
3. From the pop-up menu, choose color from a **Swatches**, **Color** or **Gradient** tab.

> **Note:** Using the Color tab, you have the option of selecting color using an HSL Color Wheel by default; RGB, RGB Hex, HSL, CMYK, Lab, Grayscale sliders can also be used.

**To select a stroke/fill color via the Color panel:**

1. Click the Stroke or Fill color selector at the top left of the panel.
2. Adjust the sliders to set the color.

The relevant swatch updates to the selected color.

> **Note:** Click the **None** swatch to make the color completely transparent.

> **Note:** Click ![Panel Preferences](../../assets/shared/ui/moremenuicon.png) Panel Preferences menu on the Color panel to select color via RGB, RGB Hex, HSL, CMYK, LAB, or Grayscale sliders; in 8 bit, 16 bit or percentage modes where applicable; or use Hue, Saturation, or Lightness boxes.

**To switch colors between the swatch selectors:**

- Click the double-headed arrow. The colors switch (but the active swatch selector remains the same.)

**To adjust opacity or noise setting:**

1. Select the **Switch** toggle button at the bottom-left of the panel.
2. Drag the slider to set the value.

**To use a different color model:**

1. Click the Panel Preferences menu, and select **Sliders** from the menu.
2. At the top right of the panel, click the current color mode displayed, e.g. RGB, to reveal a pop-up menu.
3. Select a different color model from the menu.

**To apply a color tint:**

1. Click the Panel Preferences menu, and select **Tint** from the menu.
2. Drag the slider to the left or right to increase or decrease the color tint, respectively.

**To use a different color mode:**

- Click the Panel Preferences menu, and select **8 bit**, **16 bit** or **Percentage** from the menu.

**To save colors to Swatches panel:**

- Click the Panel Preferences menu, and select one of the following:
  - **Add Color to Swatch**—adds the current color to the currently loaded palette in the Swatches panel.
  - Select a chord type from the **Add Chord to Swatch** pop-up menu—adds a chord of the current color to the currently loaded palette in the Swatches panel.

## Using the Swatches panel

The Swatches panel provides color swatch presets that are selectable from various categories. You can easily apply grays, solid colors, or gradient colors as presets.

**To use a color swatch:**

Do one of the following:

- Choose a palette category from the category pop-up menu and click a color swatch in the palette.
- Click a swatch from the **Recently used** swatches.
- Click a **None** swatch to make the color completely transparent.

## Using the Gradient Tool

Use the Gradient Tool to apply your own gradient paths to an object's stroke or fill; you can also apply solid and bitmap fills. The tool's context toolbar lets you change a linear gradient fill to be radial, elliptical, or conical.

**To use the Gradient Tool:**

1. Select an object.
2. Select the **Gradient Tool** from the Tools panel.
3. From the context toolbar, select either 'Stroke' or 'Fill' from the **Context** pop-up menu.
4. From the context toolbar, select a fill type from the **Type** pop-up menu.
5. Drag the cursor across the object's stroke or fill depending on what you selected previously. Hold down the `Shift`  to constrain the angle of the gradient path to 45°.

> **Tip:** Select and drag an end stop on the path to change the length and direction of the path. End stops can be recolored and be given reduced opacity from the Color panel. Use the `Cmd`  to reposition the gradient without affecting its length or direction.

> **Tip:** Create your own gradient fills by clicking the color swatch, adjacent to the Type pop-up menu, on the context toolbar.

## Accessing PANTONE® Colors

PANTONE® Color palettes are available from the main Swatches panel, and will automatically become a global spot color in the document palette when applied. They are also available from the pop-up Swatches panel on the context toolbar when a shape, line, or stroke is selected.

**To access PANTONE® Colors:**

1. On the **Swatches** panel (or pop-up Swatches panel), from the category pop-up menu, select your preferred PANTONE palette.
2. To display the PANTONE® Color name and number, click on the **Swatches** panel's **Panel Preferences** menu and select **Appearance** > **Show as List**. Alternatively, you can select a category from the **Swatches** panel (for example, PANTONE® Formula Guide Solid Coated V4) and use the search window to locate a specific color (e.g., 129) within that category.

## Registration color

Printing to PDF will allow you to include printer marks, including registration marks assigned with registration black (100%C:100%M:100%Y:100%K). However, you can add this registration color as a swatch that can be assigned to an object on the page, creating an on-page registration mark.

**To add a registration color as a swatch:**

- From the Swatches panel, click **Panel Preferences**, then select **Add Registration Color**.

You can then apply the swatch to an object on the page.

## Recoloring/tinting images

There are a number of ways to recolor or add a tint to an image, for example, for rebranding purposes, or to help it blend in with the rest of your page.

**To recolor a placed image:**

With the image selected, do one of the following:

- Apply a color directly to the image from the context toolbar or **Color** panel.
- For press-ready CMYK documents only, enable **K Only** on the context toolbar to apply a tint of the color chosen from the context toolbar or **Color** panel. If the color is a Spot color, then, on PDF export, the image will print using a single color palette.
- From the **Quick FX** panel, check the **Color Overlay** effect and adjust the image to your preferred color and opacity using the opacity slider and color swatch.
- Apply a **Recolor** adjustment via the **Layers** panel.

#### SEE ALSO:

- [Sampling colors](07-sampling-colors.md)
- [Color chords](11-color-chords.md)
- [Color models](02-color-models.md)
- [Gradient editing](12-gradient-and-bitmap-fills.md)
- [Swatches panel](../21-panels/27-swatches-panel.md)
- [Color Picker Tool](../20-tools/01-layout-tools/11-color-picker-tool.md)
- [Applying adjustments](../18-adjustments/01-applying-adjustments.md)
- [Using layer effects](../17-layer-effects/01-using-layer-effects.md)
