# Compound layer masks

Instead of working on a single mask layer, compound masks let you combine multiple mask layers non-destructively using Boolean operations (add, subtract, etc.), and then edit each 'component' mask layer independently of each other.

![Compound mask](../../assets/shared/compound_mask.jpg)
*Compound mask (C-M1) made up of three separate mask layers (m1, m2 and m3); Add Boolean operations were used in the compound.*

## About compound masks

While Affinity Photo 2 offers vector-based joins and non-destructive compounds, it also supports compound masks—a powerful masking system that uses the same Boolean operations (i.e., add, subtract, intersect or xor) but are instead applied to multiple mask layers non-destructively, i.e. without altering the individual mask layers.

Use compound masks for compositing and editing of complex textures, where you can combine more complex and diverse multiple masks. This gives a lot of flexibility as you can introduce different masking approaches and bring them together, e.g. a gradient mask layer combined with a painted mask layer.

Like other layers, any mask layer in the compound can be switched on/off, moved to another position on the layer stack or have its layer properties (e.g., opacity) altered.

> **Tip:** Compound masks only work with more than one mask layer present.

**To create an empty compound mask:**

Do one of the following:

- On the **Layer** menu, select **New Compound Mask Layer**.
- **macOS:** ![Mask Layer](../../assets/shared/ui/add_mask_layer.png) On the **Layers** panel, `Alt`-click **Mask Layer**, then select **Compound Mask**.
- **Windows:** ![Mask Layer](../../assets/shared/ui/add_mask_layer.png) On the **Layers** panel, `Click`-click **Mask Layer**, then select **Compound Mask**.

If there is a pixel layer previously selected, the compound mask will be clipped to that layer. When no layer is selected, it will be added to the top of your layer stack. You can drag the compound mask layer to a new position if needed.

**Adding existing mask layers to the compound mask:**

- On the **Layers** panel, drag the mask layer(s) over the Compound Mask layer entry and release.

> **Tip:** The addition of multiple mask layers will create the compound, using an Add operation by default.

**Adding pixel selection as masks to the compound mask:**

- Create an empty compound mask as before.
- Select a layer which you want make a pixel selection on, then create a pixel selection.
- Select the compound mask layer, then on the top menu select **Layer**> **New Mask Layer**.
- Repeat to build up multiple masks in the same compound masks.

> **Tip:** You can create masks from pixel selections made from channel information (e.g. targeting the Red channel) and add them to your compound mask as above. Similarly, you could target luminosity in your image for compound masking.

**To change the Compound Mask mode:**

1. On the topmost layer mask within the Compound Mask, click the mode icon.
2. Select a different compound mode from the pop-up menu—choose from **Add**, **Subtract**, **Intersect** or **Xor**.

**To release a mask layer from the compound mask:**

Do one of the following:

- Drag the mask layer out of the Compound Mask layer to another layer position.
- `Click`-click the mask layer, and from the menu, choose **Release Mask**.

> **Note — Modifier keys:** The following modifier keys can be used on mask layers in the Compound mask:
>
> - To view in isolation, hold down the `Alt`  and click on the mask thumbnail of the layer in the **Layers** panel.

#### SEE ALSO:

- [Layer masks](12-layer-masks.md)
- [Creating compounds](13-compound-layer-masks/01-compound.md)
- [Using channels](../13-channels/01-using-channels.md)
