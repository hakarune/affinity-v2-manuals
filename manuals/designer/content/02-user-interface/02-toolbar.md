# Toolbar

The Toolbar hosts commonly used tools and functions to keep them at your fingertips. Options are placed in logical groups to improve ease of use.

### Settings

The following options are available from the Toolbar.

#### Defaults:

- ![Synchronise defaults to current object](../../assets/shared/ui/synchronise_defaults.png)

   **Synchronise defaults from selection**—the default settings are updated to those of the currently selected object.
- ![Reset document defaults](../../assets/shared/ui/revert_defaults.png)

   **Revert defaults**—synchronised defaults are reverted to saved defaults. If an object is currently selected, its attributes revert to the default settings.

#### Viewing mode:

- ![Pixel view mode](../../assets/shared/ui/pixel_view_mode.png)

   **Pixel view mode**—activates Pixel mode to display vector designs as individual pixels.
- ![Retina pixel view mode](../../assets/shared/ui/retina_pixel_view.png)

   **Retina pixel view mode**—activates Pixel (Retina) mode to display vector designs as individual pixels, representing viewing on retina and high DPI displays.
- ![Outline view mode](../../assets/shared/ui/outline_view_mode.png)

   **Outline view mode**—activates Outline mode to display design as paths only. Use **View>View Mode>Wireframe** to choose an alternative 'Filled' wireframe option that displays both outlines and semi-transparent fills.

#### Order:

- ![Move to Back](../../assets/shared/ui/move_to_back.png)

   **Move to Back**—repositions the selected object(s) at the bottom of the layer. Alternatively, repositions the selected layer(s) at the bottom of the Layers panel.
- ![Back One](../../assets/shared/ui/back_one.png)

   **Back One**—moves the selected object(s) down one position in the layer. Alternatively, moves the selected layer(s) down one position in the Layers panel.
- ![Forward One](../../assets/shared/ui/forward_one.png)

   **Forward One**—moves the selected object(s) up one position in the layer. Alternatively, moves the selected layer(s) up one position in the Layers panel.
- ![Move to Front](../../assets/shared/ui/move_to_front.png)

   **Move to Front**—repositions the selected object(s) at the top of the layer. Alternatively, repositions the selected layer(s) at the top of the Layers panel.

> **Note:** The above options are also available from the **Layer** menu's **Arrange** submenu.

#### Transforms:

- ![Flip Horizontal](../../assets/shared/ui/flip_horizontal.png)

   **Flip Horizontal**—flips the selected object(s) left to right.
- ![Flip Vertical](../../assets/shared/ui/flip_vertical.png)

   **Flip Vertical**—flips the selected object(s) top to bottom.
- ![Rotate Anti-clockwise](../../assets/shared/ui/rotate_anti_clockwise.png)

   **Rotate Anti-clockwise**—rotates the selected object(s) to the left by one 90° increment.
- ![Rotate Clockwise](../../assets/shared/ui/rotate_clockwise.png)

   **Rotate Clockwise**—rotates the selected object(s) to the right by one 90° increment.

> **Note:** The above options are also available from the **Layer** menu's **Transform** submenu.

#### Align:

- ![Alignment](../../assets/shared/ui/arrange.png)

   **Alignment**—displays a pop-up dialog allowing you to align and distribute selected object(s). The **Align to** pop-up menu sets the alignment criteria for the operation. For example, you can align in relation to Selection Bounds, page Spread, page Margin or the first (or last) object selected during a multi-object selection (by marquee drag over or selection with `Shift` ). If margins are not set, alignment is to the page edge instead.

#### Snapping:

- ![Force Pixel Alignment](../../assets/shared/ui/force_pixel_alignment.png)

   **Force Pixel Alignment**—when selected (default), vector content will snap to full pixels when created, moved or modified. If this option is off, vector content can occupy partial pixels.
- ![Move By Whole Pixels](../../assets/shared/ui/move_by_whole_pixels.png)

   **Move by whole pixels**—allows you to constrain the movement of vector objects, nodes and handles to whole pixels.
- ![Snapping](../../assets/shared/ui/snapping.png)

   **Snapping**—when selected, selected objects will obey the snapping rules defined by the current snapping options. If this option is off (default), snapping is disabled.
- Snapping options—customise settings from the pop-up menu.

#### Operations:

- ![Add](../../assets/shared/ui/add.png)

   **Add**—creates a new object from the sum of the selected objects.
- ![Subtract](../../assets/shared/ui/subtract.png)

   **Subtract**—removes sections from the lowest object based on the overlap with objects higher up in the selection. All other selected objects are discarded.
- ![Intersect](../../assets/shared/ui/intersect.png)

   **Intersect**—creates a new object from the overlapping sections of selected objects.
- ![Xor](../../assets/shared/ui/combine.png)

   **Xor**—merges selected objects into a composite object with transparent area where filled regions overlap.
- ![Divide](../../assets/shared/ui/divide.png)

   **Divide**—splits object areas into separate objects; the object from the intersecting area retains the colour of the upper object.

> **Note:** New objects adopt the properties of the lowest object in the selection.

> **Note:** The above options are also available from the **Layer** menu's **Geometry** submenu.

#### Insert Target:

- ![Insert behind the selection](../../assets/shared/ui/insert_behind_selection.png)

   **Insert behind the selection**—when selected, new objects are added below the currently selected object(s).
- ![Insert at the top of the layer](../../assets/shared/ui/insert_top_of_layer.png)

   **Insert at the top of the layer**—when selected, new objects are added at the top of the layer.
- ![Insert inside the selection](../../assets/shared/ui/insert_inside_selection.png)

   **Insert inside the selection**—when selected, new objects are added inside the current selection.

#### Account:

- ![user account](../../assets/shared/ui/User_logged_out.png)

   ![Active user account](../../assets/shared/ui/User_logged_in.png)

   **Account**—registers your app, accesses your Affinity account and synchronises with purchased content. The icon will show green when signed into your account.

> **Note:** If all target options are off (default), new objects are added above the currently selected object(s).

#### SEE ALSO:

- [Customising the Toolbar](../21-workspace/customise/04-toolbar.md)
- [Object defaults](../08-object-control/26-object-defaults.md)
- [Viewing](../03-get-started/12-viewing.md)
- [Ordering objects](../08-object-control/12-ordering-objects.md)
- [Transforming objects](../08-object-control/16-transforming-objects.md)
- [Snapping](../17-design-aids/11-snapping.md)
