# Lighting effects

The Lighting feature simulates lighting from one or more light sources.

![Before](../../assets/shared/filter_lighting_before.jpg)
![After](../../assets/shared/filter_lighting_after.jpg)

## About lighting

Lighting effects simulate ambient, point, directional, and spot lighting in your design. You can supplement the single light source with additional light sources for more advanced lighting control; different light source types can be used in combination, each being independently configured and positioned using on-screen handles.

Affinity Photo 2 also lets you create lighting effects from 3D bump maps made from texture inherent in any image.

### Source types

Different source types give dramatically different results. The types are best imagined with a few examples.

- Spot: Casts an elliptical beam of light focusing on a specific subject of interest, like a torch.
- Point: Casts omnidirectional light, like a light bulb.
- Directional. Casts light directionally from infinity, e.g. from the sun.

Lighting effects can be applied as a [non-destructive, live filter](../06-layers/08-using-live-filters.md), which can be accessed via the **Layer** menu, from the **New Live Filter Layer** category.

### Settings

The following settings can be adjusted in the dialog:

- **Diffuse**—sets the level of diffused 'scattered' light reflected from the surface. Higher values reflect more light.
- **Specular**—sets the level of light reflected from the surface that reflects in a single outgoing direction (rather than being diffused), to form a highlight (hotspot).
- **Shininess**—controls the spread of the specular reflection above. Set the value lower for larger and more widespread highlights; higher for smaller, sharper highlights.
- **Specular color**—sets the color for specular reflection.
- **Ambient**—Sets the level of uniform 'background' lighting.
- **Ambient light color**—Sets a color for ambient light.
- **Light**—Click to select a point light source. You can **Add**, **Copy** or **Remove** additional light sources.
- **Type**—selects the light source type (see above).
- **Color**—selects the light source color.
- **Distance**—selects the light source distance from the page.
- **Texture**—Creates texture from the image itself.

For 3D Bump Maps:

- **Load bump map**—click to load an image that you want to convert to a 3D bump map. Use **Clear bump map** to remove any applied map.
- Uncheck **Scale Horizontally To Fit** to retain the imported image's native width. When checked, the image is stretched/shrunk to the main image.
- Uncheck **Scale Vertically To Fit** to retain native height.
- **Opacity**—alters the transparency of the texture. Type directly in the text box or drag the slider to set the value.

**To apply a spot light:**

1. From the **Filters** menu, select **Lighting**.
2. From the **Type** pop-up menu, select 'Spot'.
3. Drag the on-screen handle at the apex of the 'fan' shape to adjust the distance and direction of the light.
4. (Optional) Drag the Elevation handle situated along the center line to set the height of the spot light above the page.
5. (Optional) Drag the outer and inner handles at the end of the fan to set the outer and inner cone, respectively.

**To apply a point light:**

1. From the **Filters** menu, select **Lighting**.
2. From the **Type** pop-up menu, select 'Point'.
3. Reposition the default point light by dragging the center handle over a subject of interest.
4. Drag the circle's edge inwards or outwards to set the light's distance from the page.

**To apply a directional light:**

1. From the **Filters** menu, select **Lighting**.
2. From the **Type** pop-up menu, select 'Directional'.
3. **macOS:** Drag the crosshair within the **Direction** dial.
4. **Windows:** Drag the white spot within the **Direction** dial.

**To load a 3D bump map:**

1. On the Lighting panel, click **Load bump map**, navigate to, then select your image.
2. Click **Open**.
3. Adjust **Texture** to set the amount of texture displayed.

#### SEE ALSO:

- [Using live filters](../06-layers/08-using-live-filters.md)
- [Applying filters](01-applying-filters.md)
