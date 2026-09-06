# 3D Effect

The 3D effect is used to create the impression of a textured surface.

![Before](../../assets/shared/layerfx_base.jpg)
![After](../../assets/shared/layerfx_3deffect_02.jpg)

### Settings

The following settings are shown on the **Quick FX** panel:

- **Opacity**—controls the transparency of the effect.
- **Radius**—controls the extent of the effect.
- ![Layers Effects Icon](../../assets/shared/ui/cogicon.png) **Layer Effects**—provides access to the **Layer Effects** dialog for more advanced settings and controls.

The following advanced settings can be adjusted in the **Layer Effects** dialog:

- **Radius**—controls the extent of the effect.
- **Depth**—sets the depth of the effect. This can be linked to Radius or set independently.
- **Soften**—blurs the shadows and highlights.
- **Opacity**—sets the opacity of the effect.
- **Profile**—defines how the light is applied and sculpts the ridges, valleys, and bumps that are shaded in the process.
- **Remove Profile**—returns the profile to the default setting where light is applied evenly.
- **Diffuse**—sets the amount of diffuse color reflected from the object's surface when lit by the **Light source**. A high setting will give a matt appearance, while a low setting will give a gloss appearance.
- **Specular**—sets the intensity of specular color reflected from the object's surface when lit by the **Light source**. A high setting will give a gloss appearance, while a low setting will give a matt appearance.
- **Shininess**—sets the amount of specular color reflected from the object's surface when lit by the **Light source**. A high setting gives sharper highlights, while a low setting will give widespread highlights.
- **Specular color**—sets the specular color. Click the color box to choose the color from the pop-up panel.
- **Ambient**—sets the intensity of ambient light.
- **Ambient light color**—sets the color of the ambient light. Click the color box to choose the color from the pop-up panel.
- **Light source**—select a light source from the pop-up menu. You can then adjust the settings below for the selected light source.
- **Add**—applies an additional light source to the effect.
- **Remove**—deletes the selected light source. If there is only one light source it cannot be removed.
- **Direction**—represents the position of the light source, shadow or gradient. Click or drag to adjust the direction (and set the **Azimuth** and **Elevation** automatically).
- **Azimuth**—defines the direction of the light source, shadow or gradient.
- **Elevation**—defines the 'height' of the light source.
- **Color**—sets the color of the selected light source. Click the color box to choose the color from the pop-up panel.
- **Scale with Object**—when selected, the effect scales in proportion to the object if the object is resized. If this option is off, the effect's scale remains unchanged when the object is resized.
- **Fill Opacity**—sets the opacity of the layer contents without affecting the applied effects.

**To apply a (custom) profile:**

1. Click the Profile thumbnail.
2. In the pop-up panel, choose one of the Standard profiles.
3. (Optional) Click on the curve to add a node, drag to shape the curve.
4. Select the Linear checkbox to create a sharp curve or deselect to create a smooth curve.
5. Click away from the pop-up panel to apply the profile.

#### SEE ALSO:

- [Using layer effects](01-using-layer-effects.md)
- [Quick FX panel](../21-panels/21-quick-fx-panel.md)
