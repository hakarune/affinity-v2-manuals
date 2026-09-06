# Colour spaces

Your colour space dictates the range of colours that are available to your screen or other output device.

## About colour space

Each output device, for example, your display or printer, is only capable of producing a certain range of colours. A colour space is a specific implementation of the colour model used to define the colour gamut (i.e., the range of available colour). For example, Adobe RGB, sRGB, etc, are all unique colour spaces for the RGB colour model. Different colour spaces are also available for CMYK and Lab colour models.

In order for a device to know which colour space to use, it looks at the assigned colour profile. You can choose your colour space by assigning a [colour profile](04-colour-management.md) to your document.

### Which colour space should I use?

Which colour space you choose depends on what you're doing and the colour model you're choosing to operate in.

If you're unsure of what colour space to operate, it's advisable to stick with the default sRGB IEC61966-2.1 profile if using the RGB colour model.

> **Note:** If you need to use a colour space that is not available in Affinity Designer, it will have to be installed on your system. Devices can install colour profiles for you. Consult your system's colour management documentation for instructions.

#### SEE ALSO:

- [About colour models](02-colour-models.md)
- [Colour management](04-colour-management.md)
