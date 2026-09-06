# Liquify Tools

The Liquify tools can be used in isolation or combination to allow you to warp an image as appropriate.

**The Liquify tools available include:**

#### Push Forward Tool

Shifts pixels in the direction of the stroke.

#### Push Left Tool*

Shifts pixels 90° to the left of the stroke direction. This spreads and compresses edges along the stroke.

#### Twirl Tool*

Applies a clockwise rotational distortion under the stroke (centered around the middle of the tool cursor). If the tool is used in one area multiple times, the strength of the distortion increases.

#### Pinch Tool*

Applies a concave spherical distortion under the stroke. If the tool is used in one area multiple times, the strength of the distortion increases.

#### Punch Tool*

Applies a convex spherical distortion under the stroke. If the tool is used in one area multiple times, the strength of the distortion increases.

#### Turbulence Tool

Applies a crumbling distortion under the stroke which compacts some mesh lines together while expanding others. If the tool is used in one area multiple times, the strength of the distortion increases.

#### Mesh Clone Tool

Paints samples from one part of the mesh onto another. Ideal for applying previously set mesh adjustments to another area of the image. (`Alt`-click sets the sample area.)

#### Reconstruct Tool

Reduces the warp effect applied to an image using the above tools. If the tool is used in one area multiple times, the strength of the underlying effect decreases. With the appropriate number of applications, the area will return to its original, unwarped state.

#### Freeze Tool

Protects areas of the image from any warp effects by applying a mask.

#### Thaw Tool

Allows areas of the image to be warped by removing the current mask.

> **Note — Modifier s:** When using the above tools the following modifier s can be used:
>
> - You can quickly decrease or increase the brush width using the [ or ] s, respectively.
> - The `Shift`  reduces the rate at which the warp effect is applied.
> - For tools marked with an asterisk (*), the `Alt`  switches modes to achieve the opposite warp effect.

### Settings

Tool settings can be adjusted using the [Brushes panel](../../22-liquify-persona/03-brush-panel.md).

#### SEE ALSO:

- [Warping using Liquify Persona](../../22-liquify-persona/01-warping-using-liquify-persona.md)
- [Masking in Liquify Persona](../../22-liquify-persona/02-masking-in-liquify-persona.md)
- [Mesh Warp Tool](../10-warp-tools/01-mesh-warp-tool.md)
- [Keyboard shortcuts for tools](../../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
