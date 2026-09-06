# Warping using Liquify Persona

Liquify Persona provides the perfect environment for highly accurate warping of images.

![Before](../../assets/shared/liquify_before.png)
![After](../../assets/shared/liquify_after.png)
*Before and after using the Liquify Pinch Tool.*

When a warp is applied to an image, the overlaid mesh will update to describe the warp on a grid. Furthermore, modifying the grid will update the warped image below.

Image warping is controlled using a combination of the [Liquify tools](../32-tools/11-liquify-tools-liquify-persona/01-liquify-tools.md). These can be divided into three types:

- Direct—these affect the image by painting over image pixels. These include the **Liquify Push Forward**, **Liquify Push Left**, **Liquify Twirl**, **Liquify Pinch**, **Liquify Punch**, **Liquify Turbulence** and **Liquify Reconstruct** tools.
- Indirect—these affect the mesh. These include the **Mesh Clone** Liquify tool.
- [Masking](02-masking-in-liquify-persona.md)—these apply or remove masked areas. These include the **Freeze** and **Thaw** Liquify tools.

These Liquify tools are supported by a dedicated [Brushes panel](03-brush-panel.md).

Warping can be further modified and controlled using the [Mesh](05-mesh-panel.md) and [Mask](04-mask-panel.md) panels.

**To apply a Liquify distortion effect:**

1. Select a pixel layer.
2. Do one of the following:
  - To apply the effect *non-destructively*: Apply the effect as a live filter layer from the **Layers** panel or **Layer>New Live Filter Layer>Distort**.
  - ![Liquify Persona](../../assets/shared/ui/liquify_persona_on.png) To apply the effect *directly to the image*: From the Persona toolbar, select **Liquify Persona**.
3. Use the warp tools as described below.
4. Select **Apply** or **Done**.

**To warp using the Liquify tools:**

1. Click a Liquify tool.
2. Adjust settings on the **Brush** panel.
3. Do one of the following:
  - Click or drag on the image to apply the default warp effect.
  - `Alt`-click or `Alt`-drag on the image to apply the opposite warp effect. (Not available on all tools.)
4. The effect of the tool is cumulative. If the result is not strong enough, repeat the step above.

> **Note — Modifier keys:** The following modifier (s) can be used:
>
> - **macOS:** Press the `Ctrl` and `Alt` s and drag on the page. Dragging left or right will decrease or increase the brush size, respectively. Alternatively, use the [ or ] s, respectively. Dragging up or down will decrease or increase the brush hardness, respectively.
> - **Windows:** Press the `Cmd` and `Alt` s and drag on the page. Dragging left or right will decrease or increase the brush size, respectively. Alternatively, use the [ or ] s, respectively. Dragging up or down will decrease or increase the brush hardness, respectively.
> - With many Brush tools in Photo or Liquify Persona, you can quickly change the opacity of your brush using numerical keys.

**To warp using Clone Mesh:**

1. Click the **Liquify Clone Mesh Tool**.
2. Adjust settings on the **Brush** panel.
3. `Alt`-click on the area of the mesh you wish to copy.
4. Click on the area of the mesh to 'paste' the copied effect.
5. Repeat the step above to apply the copied effect elsewhere on the image.

**To remove a warp effect:**

For individual pixels:

1. Click the **Liquify Reconstruct Tool**.
2. Click or drag on the image to remove the warp effect.

For the entire image:

- On the **Mesh** panel, click **Reset Mesh**.

**To strengthen or subdue the current warp effect:**

1. On the **Mesh** panel, set the **Reconstruct Mesh** value:
  - **Above 100%** to strengthen the effect.
  - **Below 100%** to subdue the effect.
2. (Optional) Click **Apply** and then repeat the above step to further strengthen or subdue the effect.

**To permanently apply the warp effect:**

- On the context toolbar, click **Apply**. The warp is permanently applied to the image and the Photo Persona environment will display.

> **Note:** To discard applied warp effects and exit Liquify Persona, click **Cancel** on the context toolbar.

## Mesh controls

The Toolbar provides quick access to mesh controls which allow you to reset, save and load a mesh.

- ![Reset Mesh](../../assets/shared/ui/reset_mesh.png) **Reset Mesh**—applies a new mesh and removes all currently applied effects from the underlying image.
- ![Save Mesh](../../assets/shared/ui/save_mesh.png) **Save Mesh**—saves the current mesh for future application.
- ![Save Mesh](../../assets/shared/ui/load_mesh.png) **Load Mesh**—applies a previously saved mesh.

For more information on mesh controls, see the [Mesh panel](05-mesh-panel.md) topic.

## View modes in Liquify Persona

There are a variety of view modes available in Liquify Persona which give you the opportunity of seeing how your warped image compares to the original.

**To activate view modes:**

On the Toolbar, do one of the following:

- Click **None** to display the warped image in isolation.
- Click **Split** to display both warped and original image on the same page. A sliding divider can be repositioned to view the image 'Before' and 'After' warping
- Click **Mirror** to display warped and original image side-by-side on separate pages. Panning and zooming affects both pages simultaneously so the same area is always displayed in both pages

#### SEE ALSO:

- [Liquify Tools](../32-tools/11-liquify-tools-liquify-persona/01-liquify-tools.md)
- [Brushes panel](03-brush-panel.md)
- [Mesh panel](05-mesh-panel.md)
- [Mesh Warp Tool](../32-tools/10-warp-tools/01-mesh-warp-tool.md)
- [Liquify](../11-filters-and-effects/04-distortion-filters/07-filter-liquify.md)
