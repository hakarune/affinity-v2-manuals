# Layer blend ranges

Blending ranges let you blend layers in a project tonally. This is done by controlling the opacity across the tonal range of the currently selected layer and/or the composite layer(s) beneath that layer.

## About blend ranges

Blend ranges allow you to specify how tonal values of a layer blend with the layer(s) below. You can set the range of the tonal values affected and can set the range to have any level of opacity (from opaque to transparent).

![Blend ranges example](../../assets/shared/blendranges.png)
*Before and after blend range applied.*

The blend range of the selected layer and the underlying layer(s) is controlled in the **Blend Options** dialog.

You can change the blend range for individual colour channels within the dialog.

### About blend gamma and antialiasing (RGB documents only)

The Blend Options dialog allows you to adjust the blend gamma of the selected layer. This gives you the option of designing using a linear-RGB colour space (1.0), regular sRGB-blending (2.2) or any gamma value up to 3.0. In other words, it gives you full control over how the tones of semi-transparent or antialiased edged objects interact with colours underneath.

![Blend gamma example](../../assets/shared/blendgamma.png)
*Blue rectangle using linear-RGB (1.0 gamma) and regular sRGB-blending (2.2 gamma), respectively.*

> **Note:** By default, text layers are set to a gamma of 1.45 and all other types of layer to 2.2 (regular sRGB-blending). These default settings can be changed in [Settings (or Preferences)](../27-settings-preferences/01-settings-preferences.md) (Tools option).

Antialiasing is the reduction of the jagged appearance of lines on a pixel grid. Antialiasing is achieved by the addition of semi-transparent pixels along the line to smooth the transition from the line's edge to background objects. This area of transition is sometimes referred to as the antialiasing ramp or antialiasing coverage.

In the dialog, you can adjust the antialiasing ramp (coverage) of the selected layer, as well as control how (and if) antialiasing is inherited or set independently of other layers. For improved workflow, child layers nested hierarchically in a parent layer can inherent the parent layer's antialiasing setting automatically but can be forced to apply antialiasing or ignore it.

![Antialiasing coverage example](../../assets/shared/blendcoverage.png)
*Antialiased line with linear coverage map and custom coverage map, respectively. [Viewed in Pixel mode](../03-get-started/12-viewing.md) at 800% zoom.*

### Settings

The following settings are available in the Blend Options dialog:

- **Blend Gamma**—controls the layer's blend gamma.
- **Antialiasing**—controls antialiasing behaviour for the selected layer: **Inherit** (default) adopts antialiasing from any parent layer, while **Force On** and **Force Off** respectively applies or disables antialiasing independently of any other layers.
- **Coverage Map**—controls the layer's antialiasing ramp.
- **Fill Opacity**—alters the opacity of the layer without affecting blending. Use for layers with one of the 'special 8' blend modes applied, especially Hard Mix.
- Channels—controls which channel is affected when adjusting the blend range. Select from the pop-up menu.

The following settings can be adjusted for both the **Source Layer Ranges** and the **Underlying Composition Ranges**:

- Graph—controls the affected range of pixels and the opacity of pixels within the specified range.
- **In**—sets the horizontal position of the selected node. Type directly in the text box or drag the pop-up slider to set the value.
- **Out**—sets the vertical position of the selected node. Type directly in the text box or drag the pop-up slider to set the value.
- **Linear**—when selected (default), the graduation between two nodes is linear (i.e., nodes on the graph are connected using straight lines). If this option is off, nodes are connected using smooth curves.
- **Reset**—returns the graph to the default position (a straight line between two nodes positioned at the top of the grid).

> **Note:** When adjusting the graphs in the dialog it is worth noting the following:
>
>
> - The graphs represent tonal values from darkest on the left to lightest on the right.
> - Objects on the selected layer become less visible as nodes on the **Source Layer Ranges** graph are moved downwards.
> - Objects on the underlying layer(s) become more visible as nodes on the **Underlying Composition Ranges** graph are moved downwards.

**![Blend Options](../../assets/shared/ui/settings_cog_layers.png)

 To change blend ranges, blend gamma and antialiasing ramp:**

1. On the **Layers** panel, select a layer and then click **Blend Options**.
2. Adjust the settings in the dialog.
3. Close the dialog.

**To adjust a graph directly:**

Do any of the following:

- Drag a node horizontally to affect more or less pixels.
- Drag a node vertically to affect the visibility of pixels at the tonal value selected.
- Click on the curve to add additional nodes.
- Click to select a node and then press the `Backspace`  to remove it.

**To modify the antialiasing ramp:**

1. Click the **Coverage Map** thumbnail.
2. From the displayed chart, select a node on the profile's line and drag it vertically or horizontally to a new position.
3. Repeat for other nodes as needed.

> **Note:** For more complex profiles, click on the profile line to add a node which can be positioned as for any generated node.

> **Tip:** To remove antialiasing, set a straight, horizontal profile line at the top of the chart.

**To reset antialiasing ramp to linear:**

1. Click the **Coverage Map** thumbnail.
2. From the displayed chart's pop-up dialog, click **Reset**.

**To save a coverage map profile:**

- Under the chart, click **Save Profile**. The profile shows under the chart.

**To apply a custom coverage map profile:**

1. Click the **Coverage Map** thumbnail.
2. Select a custom profile thumbnail from below the chart. The chart will update, showing the chosen profile.

#### SEE ALSO:

- [Layer blending](07-layer-blending.md)
