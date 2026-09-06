# Modifying vector brush strokes

A vector brush stroke applied to the page remains fully editable and can be modified, while the stroke is selected. On the context toolbar, you can change its stroke width or colour; on the Stroke panel you can change its profile, while the Brushes panel lets you swap the brush for another.

![Modifying brush strokes](../../assets/shared/modifing_brush_strokes.png)

For more advanced brush settings you can also use the **Edit** button on the Brushes panel, with the option to save your brush stroke setting as a new brush preset.

### Settings

The following settings are available in the Brush dialog's **Stroke** section:

- **Brush Width**—sets the size of the stroke.
- **Size Variance**—sets the amount of brush width deviation allowed as a stroke is painted.
- **Opacity Variance**—sets the amount of transparency deviation allowed as a stroke is painted.
- The controller pop-up menu varies the brush size and opacity according to a particular input: 'Pressure' for pen tablets and Force Touch-enabled devices, and 'Velocity' or 'Velocity Inversed' for mice/Trackpads.
- The controller pop-up menu varies the brush size and opacity according to a particular input: 'Pressure' for pen tablets, and 'Velocity' or 'Velocity Inversed' for mice. The last two options simulate pressure relative to the speed of mouse movement. Click the adjacent Ramp profile icon to select a standard profile from lower thumbnails or create your own using the ramp chart. Move circular nodes to reshape the ramp, add nodes to the ramp by clicking on the line, or select a node to delete a node with the `Backspace`  (simplifying the ramp). Check **Linear** for straight lines between all nodes; If unchecked (non-linear), nodes are connected using smooth curves.
- The profile pop-up menu sets the behaviour of the controller.
- **Body**—determines the method with which the central section is drawn along the length of the stroke.
- **Corners**—determines the method used to control how corners are drawn within the stroke.
- **Head Offset**—sets the transition point at which the head section becomes the body section.
- **Tail Offset**—sets the transition point at which the body section becomes the tail section.
- Drag the red dotted lines on the lower preview to set the length of the brush body. As the lines are repositioned the Head and Tail Offset values will update.
- **Reset**—returns all stroke settings to those of the saved brush preset.
- **Duplicate**—saves the current stroke settings as a preset brush.
- **Close**—exits the dialog and applies stroke settings to the selected object.

**To modify vector brush strokes:**

1. Select the Vector Brush Tool, unless already selected.
2. `Cmd`-click on the brush stroke.
3. On the context toolbar, click **More**.
4. Adjust the settings in the **Stroke** section.
5. Click **Close**.

> **Tip:** You can paint on the page while the Brush dialog is open. The stroke will adopt the current settings in the dialog. This allows you to adjust the full brush settings as you paint for increased efficiency.

> **Note:** For more information on saving your settings as a preset, see the [Creating custom brushes](03-creating-custom-vector-brushes.md) topic.

#### SEE ALSO:

- [Painting brush strokes](01-painting-vector-brush-strokes.md)
- [Create custom vector brushes](03-creating-custom-vector-brushes.md)
- [Vector Brush Tool](../22-tools/design-tools/09-vector-brush-tool.md)
- [Brushes panel](../23-panels/04-brushes-panel.md)
