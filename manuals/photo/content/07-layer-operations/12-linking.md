# Linking

Linking layers means you can share layer attributes between layers and have them all update simultaneously if any one of the linked layers' attributes is altered.

![Linking layers before](../../assets/shared/layers_linked_before.jpg)
![Linking layers after](../../assets/shared/layers_linked_after.jpg)
*Linked HSL adjustment layers applied to all balloons allow them to be recolored simultaneously by changing a single setting.*

## About linking

By default, layer attributes are shared when linking. Some layers have common attributes such as blend mode and opacity while other layers have attributes unique to the layer type, e.g. an adjustment layer or filter layer. For example, an HSL adjustment layer can be synchronized with another HSL adjustment layer but not with a White Balance adjustment layer; their common blend mode and opacity can be shared however.

### About unlinking

There may be an occasion where you might want to selectively unlink an attribute from a specific linked layer, giving it its own independent setting. For example, if you wanted a linked Gaussian Blur live filter layer to share the same attributes as other linked Gaussian Blur live filter layer, but not its Blend mode settings, you can unlink this attribute.

Relinking simply adopts the same attribute as all other linked layers—the reverse of unlinking.

### About linked layer attributes

The layer attributes are different depending on the type of layer. For a full list of linkable attributes, see [Links panel](../33-panels/15-links-panel.md).

![Links panel](../../assets/images/panel_links.png)
*The Links panel showing the link attributes for a selected Gaussian Blur linked layer (the Blending mode & ranges are unlinked for the layer).*

**To create linked layers:**

1. Select the layer(s) to be linked.
2. On the **Layer** menu, select **Duplicate Linked**.

![Linking](../../assets/shared/ui/LayersTabLinkedIcon.png) To indicate linkage, linked layers on the **Layers** panel will show a clickable **Is Linked** icon on both the original and duplicated layer.

**To view linked layer attributes:**

1. Click the **Is Linked** icon on any linked layer.
2. On the now displayed **Links** panel, review which attributes associated with the layer.

> **Tip:** ![Linking](../../assets/shared/ui/LayersTabLinkedIcon.png) Hover over the **Is Linked** icon to see that layer's unlinked attributes.

> **Tip:** ![Select previous](../../assets/shared/ui/previousSpread.png) ![Select next](../../assets/shared/ui/nextSpread.png) Use **Select previous** and **Select next** to navigate between linked layers. This is useful to review the unlink status of each linked layer's attributes in turn.

**To unlink one or all linked layer attributes:**

- On the **Links** panel, click **Unlink** on a layer attribute. To unlink all attributes at the same time, click **Unlink** in the layer type header, e.g. Gaussian Blur.

**To relink linked layer attributes:**

1. On the **Layers** panel, click the **Is Linked** icon on the 'source' linked layer to reveal the **Links** panel.
2. Drag the layer whose attribute you want to relink from the **Layers** panel to the Link Drop icon in the Links panel. The cursor changes to a curved arrow when over the icon.

#### SEE ALSO:

- [Links panel](../33-panels/15-links-panel.md)
- [Layers panel](../33-panels/13-layers-panel.md)
