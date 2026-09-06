# Color spaces

Your color space dictates the range of colors that are available to your screen or other output device.

## About color space

**macOS:**

Each output device, for example, your display or printer, is only capable of producing a certain range of colors. A color space is a specific implementation of the color model used to define the color gamut (i.e., the range of available color). For example, Adobe RGB, sRGB, Apple RGB, and so on, are all unique color spaces for the RGB color model. Different color spaces are also available for CMYK and Lab color models.

**Windows:**

Each output device, for example, your display or printer, is only capable of producing a certain range of colors. A color space is a specific implementation of the color model used to define the color gamut (i.e., the range of available color). For example, sRGB, Apple RGB, and so on, are all unique color spaces for the RGB color model. Different color spaces are also available for CMYK and Lab color models.

In order for a device to know which color space to use, it looks at the assigned color profile. You can choose your color space by assigning a [color profile](04-color-management.md) to your document.

### Which color space should I use?

Which color space you choose depends on what you're doing and the color model you're choosing to operate in.

If you're unsure of what color space to operate, it's advisable to stick with the default sRGB IEC61966-2.1 profile if using the RGB color model.

> **Note:** If you need to use a color space that is not available in Affinity Photo 2, it will have to be installed on your system. Devices can install color profiles for you. Consult your system's color management documentation for instructions.

#### SEE ALSO:

- [About color models](02-color-models.md)
- [Color management](04-color-management.md)
