# Lens Correction

The Lens Correction filter fixes various types of lens distortion by straightening and aligning lines in an image, based on a lens profile

It is an simplified alternative to the [Lens Correction features available in the Develop Persona](../../04-develop-persona-raw/06-lens-panel/03-adjustment-lenscorrection.md) and most commonly used to quickly apply corrections to JPEG images.

![Before](../../../assets/shared/filter_lenscorrection_before.jpg)
![After](../../../assets/shared/filter_lenscorrection_after.jpg)

> **Tip:** Whether editing a JPEG or RAW image, Develop Persona's equivalent and additional lens correction settings are available at any time. You might choose the Lens Correction filter when only a lens profile needs to be applied.

## Automatic and manual lens identification

When an image contains EXIF data that identifies a camera and lens for which Affinity Photo 2 has a matching lens profile, that profile is automatically selected in the filter's window.

A camera and lens profile may need to be selected manually when using:

- A manual lens, the identity of which a camera cannot write to images' EXIF data.
- A lens adaptor, which may amend the lens description that's written to images' EXIF data.

## About the Lens Correction filter

This filter can be accessed via the **Filter** menu, from the **Distort** category.

### Settings

The following settings can be adjusted in the filter dialog. Settings will be automatically selected if the current image contains the EXIF data necessary to identify the camera hardware and its settings.

- **Camera**—select the camera you want to correct for.
- **Lens**—choose a lens profile to manually apply the lens correction. The list will change depending on the lenses supported by the selected camera.
- **Focal length**—specify the focal length for the correction, e.g. 50 mm.

#### SEE ALSO:

- [Applying filters](../01-applying-filters.md)
- [Lens Distortion](06-filter-lensdistortion.md)
- [Lens Correction (Develop Persona)](../../04-develop-persona-raw/06-lens-panel/03-adjustment-lenscorrection.md)
