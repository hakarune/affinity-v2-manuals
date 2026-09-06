# Transforming objects

Objects can be positioned, sized, rotated or sheared on the page either 'by eye' or with absolute precision. Flipping operations are also possible.

Transforming is a general term to describe the repositioning, sizing (scaling), rotation, shearing or flipping of objects. Several choices are available:

- "by eye": Using the **Move Tool** or by dragging control/rotation handles.
- Move data entry: For accurate repositioning, rotating, scaling and duplicating of objects by dialog.
- **Transform** panel: For accurate repositioning, resizing, rotating and shearing objects via panel.

You can also transform an object about a point on its own geometry, another object's geometry or a point on the page.

![Transform before](../../assets/shared/transform_before.jpg)
![Transform after](../../assets/shared/transform_after.jpg)

**To position objects accurately:**

1. Select one or more objects.
2. On the **Transform** panel, change **X** and/or **Y** values.

**To nudge objects:**

1. Select one or more objects.
2. Do one of the following:
  - For nudging by a single unit of measurement: Press an arrow key.
  - For 10x the single unit of measurement: Press an arrow key with the `Shift`  pressed.

> **Note:** As you nudge, dynamic measuring guides appear in the direction of travel.
>
> **macOS:**
>
> You can change nudge distances via **Affinity Publisher>Settings** (or **>Preferences**) (**Tools**).
>
> **Windows:**
>
> You can change nudge distances via **Edit>Settings** (**Tools**).

**To move, rotate or scale objects accurately (by Move data entry):**

1. Select one or more objects.
2. Press the `Return`  to display a **Move / Duplicate** dialog.  
Enter new settings that will offset the object from its original position, with optional **Angle**, **Rotation** and **Scale** settings. **Distance** is the measurement between the original and moved object's centers.

  ![Move data entry](../../assets/images/move_data_entry.png)

The dialog also lets you [duplicate](04-duplicating-objects.md) the original object by a set number of copies.

Check **Previous Settings** if you want to retain and use the last used transformation values entered into the dialog; uncheck to transform with new values.

> **Tip:** The **Rotation** field will accept equations, so it's easy to set the correct rotation amount—simply enter the equation as, e.g. *360/6* if you were setting up six positions, then set the **Number of copies** to be *≥5* (as you already have one object).

**To size objects accurately:**

1. Select one or more objects.
2. On the **Transform** panel, change **W** and/or **H** values.

> **Note:** You can scale objects from a custom transform origin (rather than an anchor point) that has been placed prior to transforming.

**To size objects to same:**

1. Select multiple objects, ensuring the object to be sized to is selected *first*. To do this, use `Shift`-click to target it first or a marquee selection that encompasses it first.
2. ![Match Width](../../assets/shared/ui/match-width.png) ![Match Height](../../assets/shared/ui/match-height.png) On the Toolbar, click **Alignment**, then set the **Make Same** option, choosing to size to **Width** or **Height**.
3. (Optional) Check **Maintain Aspect Ratio** to ensure the objects will resize using their original proportions.
4. Click **Apply**.

**To size objects to a targeted key object:**

1. Select multiple objects.
2. With the `Alt`  pressed, click the target object. The selected key object will possess a strong outline.
3. ![Match Width](../../assets/shared/ui/match-width.png) ![Match Height](../../assets/shared/ui/match-height.png) On the Toolbar, click **Alignment**, then set the **Make Same** option, choosing to size to **Width** or **Height**.

**To flip or rotate objects:**

1. Select one or more objects.
2. Do one of the following:
  - On the Toolbar, select a flip or rotate option.
  - From the **Layer** menu's **Transform** submenu, select a flip or rotate option.

> **Note:** You can also [rotate objects](14-rotating-and-shearing-objects.md) directly on the page by dragging the selection's rotate handle or by using the **Transform** panel.

**To transform selected objects separately:**

1. Select multiple objects.
2. With the **Move Tool** selected, select **Transform Objects Separately** from the context toolbar.
3. Transform any object.

**To transform selected objects separately:**

1. Select multiple objects.
2. With the **Move Tool** selected, select **Transform Objects Separately** from the context toolbar.
3. Transform any object.

**To size selected objects separately to absolute sizes**

1. Select multiple objects.
2. Ensure **Transform Objects Separately** is selected from the context toolbar.
3. On the **Transform** panel, resize by entering an absolute value into the **W** or **H** input boxes. For example enter *=100px* into the **W** box to make all objects 100px wide.

This absolute sizing is in contrast to scaling other objects in your selection proportionately to a targeted key object resized to, e.g. 100px. Note the importance of the "=" symbol to signify an expression being used.

## Scale override

When an object is resized, the stroke width, layer effect radii, corner radii and text frame contents can be forced to scale by using the **Transform** panel. If **Scale with object** settings are unchecked on the object itself (stroke, layer effect, etc.) then they will be ignored.

> **Tip:** For best results, use Scale override when resizing and maintaining the object's aspect ratio.

**To override scaling on objects:**

1. Select an object.
2. On the **Transform** panel, enable **Scale Override**.
3. Resize via the object's handles with the `Shift`  pressed.

**To override scaling on objects selectively:**

1. Select an object.
2. On the **Transform** panel, click the **Scale Override** down arrow to check/uncheck the following settings:
  - **Line weights**—useful when working on vector objects with a stroke. For example, you can either force or prevent scaling while resizing with the setting set to **Scale with object** or **Locked**, respectively.
  - **Shape corners**—to control the scaling of a shape's corners while resizing, you can either force (**Scale with object**) or prevent (**Locked** setting).
  - **Layer effect radii**—to control the scaling of the radius of a layer effect added to an object.
  - **Text frame contents**—to control the scaling of frame text while resizing; when set to **Locked** the container will scale while keeping text the same size. When set to **Scale with object** however, text will enlarge when resizing the container by its corner handles.
3. Ensure the **Scale Override** button is enabled.
4. Resize via the object's handles with the `Shift`  pressed.

#### SEE ALSO:

- [Rotating and shearing objects](14-rotating-and-shearing-objects.md)
- [Duplicating objects](04-duplicating-objects.md)
- [Transform panel](../21-panels/34-transform-panel.md)
- [Expressions for field input](../26-expressions-for-field-input/01-expressions-for-field-input.md)
- [Keyboard shortcuts for transforming operations](../24-keyboard-shortcuts/01-keyboard-shortcuts.md)
