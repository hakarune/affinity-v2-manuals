# White Balance adjustment

Remove unwanted color casts or give an image a warmer or cooler feel.

![Before](../../../assets/shared/adjustment_whitebalance_before.jpg)
![After](../../../assets/shared/adjustment_whitebalance_after.jpg)
*Before and after adjustment applied.*

The adjustment lets you control white balance using:

- the dialog's sliders
- a white point picker (Photo Persona only)
- a White Point Tool ([Develop Persona](../../04-develop-persona-raw/01-developing-raw-images.md) only)

> **Note:** Typically, white balance is available as an adjustment layer. In Develop Persona, it appears on the **Basic** panel and also as a dedicated White Balance Tool.

### Settings

The following settings can be adjusted:

- **White Balance**—controls the 'temperature' of the image. In the **Develop Persona** this is measured in Kelvin (K). Drag the slider to the left to cool the image, or drag the slider to the right to warm the image.
- **Tint**—tints the image either towards magenta or green. This is useful for removing color casts, especially if the image was taken under artificial lighting (e.g., tungsten or fluorescent).
- **Picker**—allows you to sample the image to set the white point on which the white balance will be calculated. You can sample using one of the following methods:
  - Click to sample a pixel under the cursor.
  - Drag the cursor across the image to sample all pixels under the cursor. The averaged color from those pixels is used.
  - Press the `Alt`  and drag to sample under a rectangular marquee, again using the averaged color of those pixels.

> **Note:** In Develop Persona, a dedicated **White Point Tool** is used instead of the **Picker**. It offers the same sampling functionality as the Picker.

> **Note:** In Develop Persona, the image uses the camera's "As Shot" White Balance values by default. Checking the adjustment's checkbox displays those values, which can be reverted to at any time by unchecking the adjustment's checkbox.

#### SEE ALSO:

- [Applying adjustments](../01-applying-adjustments.md)
