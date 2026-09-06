# Expressions for field input

Instead of adding absolute values into input fields, you can add expressions. These allow you create new values based on percentages, mathematical symbols, and another field's value.

> **Note:** You can mix units of measurement in an expression. Affinity handles conversion automatically.

> **Note:** The expression or variable presented after the comma can be used as alternative, often shortform, versions of the expression or variable.

When adding an expression into a field, the following colours may appear, providing feedback on the validity of the expression:

- Red—this denotes an error (examples include unrecognised units, unexpected character, unexpected token, unknown keyword, incomplete argument)
- Green—the variable has been recognised
- Orange—valid input awaiting Return key

## Sizing expression examples

Use throughout the user interface but typically:

- When resizing a document via **File > Document Setup**.
- Transforming one or more selected objects via the **Transform** panel<sup>*</sup>.
- Increasing stroke width on one or more selected objects via the **Stroke** panel<sup>*</sup>.

<sup>*</sup>Individual objects in multiple selections will be sized based on their own values, not those of other objects.| Input | Result |
| --- | --- |
| +=20 | Increase value by 20. |
| -=20 | Decrease value by 20. |
| *2 | Double size. |
| /2 | Divide in half. |
| 50%, *0.5 | Decrease by half. |
| 120%, *1.2 | 20% bigger. |

## Relational expression examples

Use when resizing a document or transforming an object via the **Transform** panel.

| Input | Result |
| --- | --- |
| w+20 | Scales based on addition of other input value. *Example entered into Height box to set height as width plus 20 pixels.* |
| w-20 | Scales based on subtraction of other input value. *Example entered into Height box to set height as width minus 20 pixels.* |
| 2*w | Scaling based on a multiple of other input value. *Example is entered into Height box to set height to double the width.* |
| w/2 | Scaling based on a division of other input value. *Example entered into Height box to set height to half the width.* |
| w^3 | Scales based on a power of other input value. *Example entered into Height box to set height as the width to the power of three.* |
| 12pt / x | Sets the text's x-height to 12pt. |

## Mathematical constants

For general use throughout the user interface.

| Input | Constant |
| --- | --- |
| pi, π | For Pi |
| phi, gr, φ | For golden ratio |
| root2, rad, rt | For Pythagoras’s constant |
| e | Euler’s constant |

## Transform variables

Use when moving, scaling, rotating or shearing objects via the **Transform** panel.

| Input | Variable |
| --- | --- |
| xposition, x | X position |
| yposition, y | Y position |
| width, w | Width |
| height, h | Height |
| rotation, r | Rotation |
| shear, s | Shear |

## Document variables

Use when setting dimensions using the New Document or Document Setup dialogs.

| Input | Variable |
| --- | --- |
| spreadwidth, w | Document width |
| spreadheight, h | Document height |
| marginleft, l | Left document margin |
| marginright, r | Right document margin |
| margintop, t | Top document margin |
| margin, b | Bottom document margin |

## Typographical variables

Use when setting the size of text.

| Input | Variable |
| --- | --- |
| xheight, x | X-height |
| ascent, a | Ascent |
| capheight, c | Cap height |

## Transform panel variables

Use when sizing and positioning content using the **Transform** panel in relation to the document (i.e. page spread).

| spreadwidth, sprw, sw | The width of the current spread |
| --- | --- |
| spreadheight, sprh, sh | The height of the current spread |
| spreadleft, sprl, sl | The position of the left edge of the current spread |
| spreadright, sprr, sr | The position of the right edge of the current spread |
| spreadtop, sprt, st | The position of the top edge of the current spread |
| spreadbottom, sprb, sb | The position of the bottom edge of the current spread |
| marginsizeleft, mgnszl, msl | The size of the left margin on the current spread |
| marginsizeright, mgnszr, msr | The size of the right margin on the current spread |
| marginsizetop, mgnszt, mst | The size of the top margin on the current spread |
| marginsizebottom, mgnszb, msb | The size of the bottom margin on the current spread |
| marginleft, mgnl, ml | The position of the left margin on the current spread |
| marginright, mgnr, mr | The position of the right margin on the current spread |
| margintop, mgnt, mt | The position of the top margin on the current spread |
| marginbottom, mgnb, mb | The position of the bottom margin on the current spread |
| designareawidth, areawidth, aw | The space between the left and right margins on the current spread |
| designareaheight, areaheight, ah | The space between the top and bottom margins on the current spread |

## Advanced mathematical expressions

For general use throughout the user interface.

| Function/Usage | Notes |
| --- | --- |
| abs(x) | Absolute value |
| idiv(x,y) | Results in the integer (whole number) of *x* divided by *y* (no rounding is applied) |
| irem(x,y) | Results in the remainder of *x* divided by *y* |
| sin(a) | Sine |
| asin(a) | Inverse Sine |
| cos(a) | Cosine |
| acos(a) | Inverse Cosine |
| tan(a) | Tangent |
| atan(a) | Inverse Tangent |
| atan2(a, b) | Arctangent |
| average(a, b, ...) | Average of arguments |
| clamp(a, lo, hi) | a if it is between lo and hi, otherwise lo or hi |
| clampmin(n, min) | clamp values below minimum |
| clampmax(n, max) | clamp values above maximum |
| copysign(t, t sign) |  |
| dim(t x, t y) |  |
| fma(t a, t b, t c) | Computes (a*b) + c |
| fmod(t, t) |  |
| fraction(t) |  |
| lerp(a, b, f) | Linear interpolation (a + (b - a) f) |
| min(a, b, ...) | Smaller of values |
| max(a, b, ...) | Larger of values |
| mid(a, b) | Average of a and b |
| noise(seed / x, y) | Generate 1D noise either from a seed or based on X/Y input. |
| round(n) | Round to integer |
| roundup(b), ceil(n) | Round up to integer |
| rounddown(b), floor(n) | Round down to integer |
| trunc(t) | Shorthand for **truncate** |
| truncate(n) | Truncate **n** places after decimal point. |
| whole(t) |  |

#### SEE ALSO:

- [Document setup](../03-get-started/10-document-setup.md)
- [Transform panel](../23-panels/22-transform-panel.md)
- [Draw and edit shapes](../05-drawing-curves-and-shapes/06-draw-and-edit-shapes.md)
