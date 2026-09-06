# Transforming curves and shapes

Just as objects can be transformed, the nodes of curves and shapes can be transformed too.

![node transform before](../../assets/shared/node_transform_before.png)
![node transform after](../../assets/shared/node_transform_after.png)

Node transformation works by forming a selection box around selected nodes. In doing so the box can be transformed in the same way that an object's selection box can be. As a result, the position of nodes relative to each other is altered in the transformation process which reshapes the curve or shape in different ways.

> **Note:** Transformation is possible on both two-dimensional and axonometric designs (e.g., isometric).

**To transform multiple nodes:**

1. With the **Node Tool**, select one or more nodes on a curve or shape.
2. On the context toolbar, enable **Transform Mode** in the **Transform** section.
3. Resize, rotate and skew either directly on the curve or shape using selection box handles or use the **Transform** panel for absolute precision.

> **Tip:** With the **Transform** panel you can transform in relation to a configurable anchor point.

> **Tip:** The context toolbar also offers some options to enable transform origin, hide selection when dragging, switch on alignment handles within the selection box for more precise transforms, control selection areas to encompass all the curve outline and cycle the type of selection box.

**To transform shapes for a simple distortion effect:**

1. Select two nodes on the shape previously converted to curves.
2. Enter **Transform Mode**.
3. With the `Cmd`  pressed, drag any selected node inwards or outwards.

This is particularly effective on simple shapes such as rectangles.

![perspective on shapes](../../assets/shared/perspective.png)

#### SEE ALSO:

- [Node Tool](../20-tools/01-layout-tools/02-node-tool.md)
- [Selecting and aligning nodes](09-selecting-and-aligning-nodes.md)
- [Transforming objects](../09-object-control/13-transforming-objects.md)
- [Transform panel](../21-panels/34-transform-panel.md)
- [Converting objects to curves](../09-object-control/17-convert-objects-to-curves.md)
- [Keyboard shortcuts for transforming operations](../24-keyboard-shortcuts/01-keyboard-shortcuts.md)
