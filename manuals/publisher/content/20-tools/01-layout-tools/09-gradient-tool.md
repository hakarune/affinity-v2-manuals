# Gradient Tool

The **Gradient Tool** allows you to adjust the fill and line colors applied to vector and text objects.

Although you can use the Gradient Tool to apply solid colors to an object's fill or stroke, its true power lies in its ability to apply and modify gradients.

> **Note:** You can also apply a gradient to pixel layers, adjustment layers and layer masks using the Gradient Tool.

> **Note:** You can also apply bitmap fills to objects, allowing you to add a bitmap image from an external source (like a pattern or texture) which can then be transformed on the object.

### Settings

The following settings can be adjusted from the context toolbar:

- **Context**—allows the adjustment of either the **Fill** or **Stroke** color of the selected object.
- **Text** or **Frame**—assigns the fill to either the frame **Text** or the **Frame** itself. For text frames only.
- **Type**—converts the object's color type. For example, from **None** to **Linear**. From here, you can also apply a **Solid** or **Bitmap** fill.
- Select, pick, and modify the object's solid or gradient color—click the color swatch to display a pop-up panel. See the [Color panel](../../21-panels/05-color-panel.md), [Swatches panel](../../21-panels/27-swatches-panel.md), and [Gradient and bitmap fills](../../07-color/12-gradient-and-bitmap-fills.md) topics for more information on the settings available.
- ![Rotate Gradient](../../../assets/shared/ui/fill_-_rotate_gradient.png) **Rotate gradient**—rotates the applied gradient by 90°.
- ![Reverse Gradient](../../../assets/shared/ui/fill_-_reverse_gradient.png) **Reverse gradient**—the end stops swap places. (All intermediate stops are also repositioned accordingly.)
- ![Maintain fill aspect ratio](../../../assets/shared/ui/fill_-_maintain_aspect_ratio.png) **Maintain fill aspect ratio**—if this option is off (default), the end stops can be resized separately which changes aspect ratio. When selected, the end stops are locked to keep the aspect ratio (i.e. changing one will automatically update the other). This setting affects only elliptical and bitmap fills.
- **Extend**—for bitmap fills only, these settings control how to present the bitmap fill's tile:
  - **Wrap**—repeats the bitmap outwards from a centrally set node; when it is smaller than the shape it is filling, it is tiled over to fill it.
  - **Mirror**—repeats the bitmap outwards from a centrally set node; the option aids smooth transition and seamless presentation of the bitmap fill while resizing, however this can be easily moved by dragging to a new position.
  - **Repeat**—used to achieve symmetrical and seamless patterns, which can be stacked infinitely.
  - **Zero**—places the bitmap centrally without it repeating. This option is helpful for positioning the image within a shape or a frame, i.e. to establish its starting point, before deciding on a repeating Extend method.
- **Quality**—for bitmap fills only, these settings control the quality of the fill when scaling the object:
  - **Nearest**—the quickest method to use while picture scaling at a cost of some image quality loss, however improved speed. This variant does not employ pixel interpolation, and so results in a sharper yet more jagged image.
  - **Bilinear**—similar to **Nearest**, however using a sophisticated interpolation technique while filling in empty pixels. Here, rather than copying the nearest pixel, the process uses adjacent pixels and this results in a considerably smoother scaling.
  - **Lanczos3**—may be used to seamlessly interpolate the value of samples or as a low-pass filter, which should result in an even smoother transition of pixels. It is also approximately similar to the bicubic method of interpolation.
- **Scale with object**—for bitmap fills only, when checked, the bitmap fill will scale in proportion to its object being rescaled; when unchecked, you'll avoid any unwanted shrinking or stretching of your bitmap fill during object rescaling.

#### SEE ALSO:

- [Transparency Tool](10-transparency-tool.md)
- [Selecting colors](../../07-color/06-selecting-colors.md)
- [Gradient and bitmap fills](../../07-color/12-gradient-and-bitmap-fills.md)
- [Keyboard shortcuts for tools](../../24-keyboard-shortcuts/01-keyboard-shortcuts.md)
