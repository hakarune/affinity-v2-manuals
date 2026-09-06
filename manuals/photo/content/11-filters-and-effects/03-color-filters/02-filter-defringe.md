# Defringe

Purple fringing, or bichrominance as it's more correctly termed, is a form of chromatic aberration caused by the over-excitation of the pixels on the sensor in the camera. The effect can occur anywhere within an image but it's most common at the edges of high contrast areas, especially when a dark element is strongly backlit, such as branches silhouetted against a blue sky. The Defringe filter selectively adjusts these areas to remove the color fringing.

![Before](../../../assets/shared/filter_defringe_before.jpg)
![After](../../../assets/shared/filter_defringe_after.jpg)
*Using the Defringe filter to remove purple fringing from the window edges.*

## About the Defringe filter

This filter can be applied as a [non-destructive, live filter](../../06-layers/08-using-live-filters.md). It can be accessed via the **Layer** menu, from the **New Live Filter Layer** category.

On selecting the Defringe filter, it will default to settings which remove the purple fringing, as this is the most common type. This can be manually adjusted as necessary in the dialog, or by sampling the fringe color on the page to remove it.

### Settings

The following settings can be adjusted in the filter dialog:

- **Fringe Color**—defines the color of the fringe to be desaturated. Drag the slider or click on the image to define the hue.
- **Also Remove Complementary Hue**—also removes fringing matching the chosen hue's complementary color (e.g., choosing purple would also remove yellow fringing).
- **Tolerance**—defines how close the fringe color must be to the defined color before it is affected. Type directly in the text box or drag the slider to set the value.
- **Radius**—defines the radius of the pixels affected around the fringed areas. Type directly in the text box or drag the slider to set the value.
- **Edge Brightness Threshold**—defines the amount of contrast needed between the fringed areas before affecting the pixels. Type directly in the text box or drag the slider to set the value.

#### SEE ALSO:

- [Using live filters](../../06-layers/08-using-live-filters.md)
- [Applying filters](../01-applying-filters.md)
- [Chromatic Aberration](01-filter-chromaticaberration.md)
