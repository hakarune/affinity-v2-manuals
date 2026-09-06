# Denoise

The Denoise filter is a powerful form of noise reduction. At higher settings, it also creates a really pleasing, posterizing effect.

## About the Denoise filter

This filter can be applied as a [non-destructive live filter](../../06-layers/08-using-live-filters.md). It can be accessed via the **Layer** menu, from the **New Live Filter Layer** category.

![Before](../../../assets/shared/filter_denoise_before.jpg)
![After](../../../assets/shared/filter_denoise_after.jpg)

### Settings

The following settings can be adjusted:

- **Luminance**—controls the intensity of noise removal from the luminance channel. Drag the slider to set the value.
- **Luminance Detail**—adjusts the detail edge smoothing threshold. Higher values will allow more fine detail through, whereas lower values will smooth fine detail and provide stronger noise reduction.
- **Luminance Contribution**—controls how much of the overall luminance noise reduction is added to the image.
- **Colors**—controls the intensity of noise removal from the chrominance channels. Drag the slider to set the value.
- **Colors Contribution**—controls how much of the overall chrominance noise reduction is added to the image.

#### SEE ALSO:

- [Using live filters](../../06-layers/08-using-live-filters.md)
- [Applying filters](../01-applying-filters.md)
- [Add Noise](01-filter-addnoise.md)
- [Diffuse](04-filter-diffuse.md)
- [Perlin Noise](07-filter-perlinnoise.md)
