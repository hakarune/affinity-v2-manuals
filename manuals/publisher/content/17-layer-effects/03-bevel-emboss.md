# Bevel/Emboss

The Bevel/Emboss effect is used to add rounded edges and shadows to give a 3D impression.

![Before](../../assets/shared/layerfx_base.jpg)
![After](../../assets/shared/layerfx_bevelemboss_02.jpg)

Depending on the type of bevel or emboss set, the rounded-edge might be inside or outside an object, convex or concave, and may include a shadow.

For all bevel/emboss effects you can adopt a preset or custom profile that defines the bevel/emboss edge.

### Settings

The following settings are shown on the **Quick FX** panel:

- **Opacity**—controls the transparency of the effect.
- **Radius**—controls the extent of the effect.
- ![Layers Effects Icon](../../assets/shared/ui/cogicon.png) **Layer Effects**—provides access to the **Layer Effects** dialog for more advanced settings and controls.

> **Note:** By default, you'll apply a Pillow Emboss effect when using the Quick FX panel. For an inner/outer bevel and a basic emboss effect, use the Layer Effects dialog.

The following advanced settings can be adjusted in the **Layer Effects** dialog:

- **Type**—sets an Inner bevel, Outer bevel, Emboss or Pillow emboss effect. Select from the pop-up menu.
- **Radius**—controls the extent of the effect.
- **Depth**—sets the depth of the effect. This can be linked to Radius or set independently.
- **Soften**—blurs the shadows and highlights.
- **Profile**—defines how the light is applied and sculpts the ridges, valleys, and bumps that are shaded in the process.
- **Invert**—reverses the effect of the lighting profile.
- **Remove Profile**—returns the profile to the default setting where light is applied evenly.
- **Direction**—represents the position of the light source, shadow or gradient. Click or drag to adjust the direction (and set the **Azimuth** and **Elevation** automatically).
- **Azimuth**—defines the direction of the light source, shadow or gradient.
- **Elevation**—defines the 'height' of the light source.
- **Highlight**—sets the blend mode, color and opacity for the highlight. Blend mode defaults to screen.
- **Shadow**—sets the blend mode, color and opacity for the shadow. Blend mode defaults to multiply.
- **Scale with Object**—when selected, the effect scales in proportion to the object if the object is resized. If this option is off, the effect's scale remains unchanged when the object is resized.
- **Fill Opacity**—sets the opacity of the layer contents without affecting the applied effects.

**To apply a preset or custom profile:**

1. Click the Profile thumbnail.
2. In the pop-up panel, choose either:
  - One of the Standard profile thumbnails.
  - A custom profile: Click on the curve to add a node, drag a node or portion of the curve to shape it.
3. Select the Linear checkbox to create a sharp curve or deselect to create a smooth curve.
4. Click away from the pop-up panel to apply the profile.

#### SEE ALSO:

- [Using layer effects](01-using-layer-effects.md)
- [Quick FX panel](../21-panels/21-quick-fx-panel.md)
