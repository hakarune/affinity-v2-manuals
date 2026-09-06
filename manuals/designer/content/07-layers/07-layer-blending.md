# Layer blending

A layer's blend mode determines how the layer or object's pixels blend with the pixels on the layer beneath.

![Blend Modes](../../assets/shared/layer_blending.png)
*Common blend modes: (A) Normal, (B) Multiply, (C) Screen, (D) Overlay, (E) Divide (F) Colour Burn.*

## Blend mode types

Affinity Designer supports an impressive selection of different blend modes. The most commonly used blend modes are as follows:

- **Normal**—The default blend mode. The top pixels display over underlying pixels according to the level of top layer opacity.
- **Multiply**—The blending result is a combination of the top and bottom colour at each pixel position, always producing a darker value.
- **Screen**—The opposite of Multiply, where the blending result is a combination of the inverse of the top and bottom colour at each pixel position, always producing a lighter value.
- **Overlay**—Applies either Multiply or Screen blend mode, depending on the bottom colour at each pixel position. If the bottom layer pixels are <50% grey, it multiplies; if >50% it screens.
- **Divide<sup>1</sup>**—Lower layers are lightened by luminance on the upper layer. White has no effect. Lightness is increased progressively by grey through to black.
- **Colour Burn<sup>1</sup>**—Darkens the bottom colour pixels relative to the values of the top colour pixels.

Other available blend modes include Darken, Darker Colour, Linear Burn, Lighten, Lighter Colour, Colour Dodge<sup>1</sup>, Add, Soft Light, Hard Light, Vivid Light, Pin Light, Linear Light, Hard Mix, Difference<sup>1</sup>, Exclusion<sup>1</sup>, Subtract, Hue<sup>2</sup>, Saturation<sup>2</sup>, Luminosity, Colour<sup>2</sup>, Average<sup>1</sup>, Negation<sup>1</sup>, Reflect<sup>1</sup>, Glow<sup>1</sup>, Contrast Negate, Erase and Passthrough.

<sup>1</sup> Not available in Lab16 mode.

<sup>2</sup> Not available in Greyscale mode.

> **Note:** Any layer or object can have a blend mode assigned, including mask and adjustment layers. The default blend mode is 'Normal'—no special compositing is applied. For a group, the default is 'Passthrough'. When set, the group itself has no special blend properties of its own, and passes on the blend mode of its parent layer.

> **Note:** Layer blend modes applied to child layers produce isolated blending which will not affect the parent layer or any other layers in the layer stack.

> **Note:** The same blend modes can be utilised on layer effects and pixel brushes.

**To change the blend mode of a layer (or object):**

1. In the **Layers** panel, select a layer (or object).
2. Choose a blend mode from the pop-up menu on the panel.

#### SEE ALSO:

- [Layer blend ranges](08-layer-blend-ranges.md)
- [Layer effects](../18-layer-effects/01-using-layer-effects.md)
- [Painting brush strokes](../10-vector-painting/01-painting-vector-brush-strokes.md)
