# Triangle Tool

Create all types of triangles including true isosceles and right-angle triangles easily with the Triangle Tool.

![Triangle default](../../../assets/shared/shapes_triangle1.png)
*Default shape and handle position (in red) before customization.*

## Customization

The **Triangle Tool** offers a handle on the shape and options on the context toolbar to enable the triangle to be modified.

![Triangle alternatives](../../../assets/shared/shapes_triangle2.png)
*Two possible outcomes when the option is customized.*

### Settings

The following settings can be adjusted from the context toolbar:

- **Fill**—click the color swatch to display a pop-up panel to update fill color.
- **Stroke**—click the color swatch to display a pop-up panel to update stroke color.
- **Stroke properties**—set the stroke style, width, joins, cap ends, order and arrowhead settings via a pop-up panel.
- ![Presets Icon](../../../assets/shared/ui/cogicon.png) **Presets**—click to display a pop-up panel from which you may select an existing preset (if any are available) or create a new preset.
- **Top point**—controls the position of the top point of the triangle from left (0%) to right (100%), with 50% representing a central point.
- **Mirror**—updates the above settings to give a reversed (flipped) version of the current shape.
- ![Enable Transform Origin](../../../assets/shared/ui/rotationcntr.png) **Enable Transform Origin**—displays a movable transform origin about which the shape can be rotated.
- ![Hide Selection while Dragging](../../../assets/shared/ui/hide_selection_while_dragging.png) **Hide Selection while Dragging**—when selected, the object's selection box is temporarily hidden when transforming the object. If this option is off, the selection box remains visible during transformation. The selected behavior persists across all objects unless it is manually switched.
- ![Show Alignment Handles](../../../assets/shared/ui/alignment_mode.png) **Show Alignment Handles**—when selected, displays alignment handles at the center and edges of the selected object. Hovering over these handles displays a floating guideline across the page. You can drag the handles to position the center or edges of the selected object in line with this guide.
- ![Transform Objects Separately](../../../assets/shared/ui/multiple_transform.png) **Transform Objects Separately**—when selected, where multiple objects are selected, they can be be resized, rotated and sheared independently of each other instead of transforming the bounding box.
- ![Convert to Curves](../../../assets/shared/ui/converttocurves.png) **Convert to Curves**—converts the selected object into a series of connected lines and nodes.
- **Keep selected**—when enabled (default), the new shape layer will be selected on creation. When disabled, the new object is deselected which prevents it from adopting the next object’s stroke/fill properties.

> **Tip — Isosceles, right-angled and equilateral triangles:** - To create an isosceles triangle, set the top point to 50%.
> - To create a right-angled triangle, set the top point to either 0% or 100%.
> - To create a true equilateral triangle (where all three sides are the same length), use the **[Polygon Tool](07-polygon-tool.md)**. Ensure that you constrain the shape with the `Shift`  as you draw, and then set the number of sides to 3 on the context toolbar.

> **Note:** To reset any red handle to its default position, simply double-click the handle.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../../37-settings-preferences/01-settings-preferences.md):
>
> - **Tools>Tool Handle Size**

#### SEE ALSO:

- [About geometric shapes](../../25-lines-and-shapes/06-about-geometric-shapes.md)
- [Draw and edit shapes](../../25-lines-and-shapes/07-draw-and-edit-shapes.md)
- [Polygon Tool](07-polygon-tool.md)
