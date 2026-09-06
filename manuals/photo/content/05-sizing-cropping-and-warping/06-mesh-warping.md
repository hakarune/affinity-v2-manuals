# Mesh warping

Mesh warping lets you distort specific areas of your image without affecting other areas. It can be used for dramatic warping effects or for more subtle focused retouching of facial features.

![Before](../../assets/shared/warp_before.jpg)
![After](../../assets/shared/warp_after.jpg)
*Warping an image*

## About mesh warping

The **Mesh Warp Tool** and **Mesh Warp** live filter each provide a flexible mesh grid which can warp your image by repositioning the grid's lines, nodes, and patches; underlying pixels are transformed under the line, node or patch. The extent of warping you want to carry out is governed by the complexity of the grid.

You'll initially start with a mesh grid without lines, but adding your own lines and nodes lets you warp with ease. Position lines adjacent to areas in your image that you want to apply warping to.

> **Note:** The Mesh Warp Tool and Mesh Warp live filter provide the same settings on their context toolbars.

**To create a mesh:**

1. Do one of the following:
  - To apply a destructive mesh warp, from the **Tools** panel on the left, click the **Mesh Warp Tool**.
  - To apply a non-destructive mesh warp, select **Layer>New Live Filter Layer>Distort>Mesh Warp**.
2. Double-click on the edge of the mesh grid—the top edge gives a vertical line; a side edge gives a horizontal line.
3. Repeat for as many lines as you need.

> **Note:** If you want to start again, click **Reset** on the context toolbar.

**To add nodes to the grid:**

- Double-click anywhere within the grid.

**To select multiple nodes in the grid:**

Do one of the following:

- Press the `Shift`  and click each node in turn.
- Drag across multiple nodes to create a marquee selection.

**To apply warping:**

1. (Optional) On the context toolbar, use the **Mode** option to manipulate just the grid ('Source') or both grid and image simultaneously ('Destination').
2. Drag a node, a node's corner handle, line or patch. Patch warping is achieved by clicking in an area contained by mesh lines and dragging the circle—this warps the entire area.
3. Select **Apply** or press `Return`.

> **Note:** The mesh is really just an assembly of bendable curves. When you alter these curves, distorting the grid, the underlying image deforms accordingly.

#### SEE ALSO:

- [Mesh Warp Tool](../32-tools/10-warp-tools/01-mesh-warp-tool.md)
- [Warping using Liquify Persona](../22-liquify-persona/01-warping-using-liquify-persona.md)
