# ![Shape Builder Tool](../../../assets/shared/ui/Shape_builder.png)

 Shape Builder Tool

The **Shape Builder Tool** adds separate shapes together to make more complex shape designs. Shape areas can also be deleted.

The tool lets you initially select objects to be included in the shape building operation. By default, you can then select 'candidate' shape areas within that selection and add, delete or create them as a final step. Alternatively, a one-step select-and-add, select-and-delete and select-and-create approach can be taken.

Adding and creating both produce a new combined shape but adding replaces the original shape areas, while creating forms a new object and retains the original shapes.

> **Tip:** Tool shortcut : `S`

### Settings

The following settings can be adjusted from the context toolbar:

- **Action**—enables one of three shapebuilding modes:
   - ![Add](../../../assets/shared/ui/add_to_shape.png)

     If disabled, you can build up selected areas, then click this option to *add* them together once final selections are made; when enabled, shape areas are automatically added together in one operation according to the chosen drag method. For either state, the original object are replaced by the new combined shape.
  - ![Delete](../../../assets/shared/ui/remove_from_shape.png)

     If disabled, you can build up selected areas and then *remove* them by clicking this option; when enabled, areas are selected and deleted in one operation as you click.
  - ![Create](../../../assets/shared/ui/create_new_shape.png)

     As for the Add operation but a shape copy is *created*, leaving the original objects intact rather than removing them.
- **Drag method**—choose between using a freehand line, straight line or selection marquee to select areas or select-and-add areas in one operation.
- **Clean up**—offers menu options to automatically remove unwanted curves and shape areas when shapebuilding:
   - **None**—no removal of internal curves, connected curves or shape areas occurs.
  - **Internal curves**—parts of open curves extending into areas will be removed.
  - **Connected curves**—open curves extending over selected/unselected area boundaries will be removed.
  - **All unused geometry**—shapes and open curves, both inside and outside of the selected area, will be removed.
- **Use style from first selected area**—when checked, object styles (including fill/stroke colour, layer effects and stroke properties) are carried over to the new areas from the area you begin dragging from or drawing a marquee selection; dragging from outside the selected objects will only pick up the currently set default stroke/fill. When unchecked, the currently set default stroke/fill will be applied to all areas.

#### SEE ALSO:

- [Adding objects by shape building](../../08-object-control/07-adding-objects-by-shape-building.md)
