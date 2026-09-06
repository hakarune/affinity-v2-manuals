# Spacing

Layer content across multiple layers can be spaced evenly between layer selection bounds using Alignment commands. The spacing of objects ensures there is an equal distance between object *edges*.

![Before](../../assets/shared/distribute_before.jpg)
![After](../../assets/shared/distribute_spacing.jpg)
*Before and after spacing.*

### Spacing using key objects

**macOS:**

Instead of spacing being calculated between selection bounds, you can control spacing in relation to any targeted key object in the current selection. This targeting is done using an `Alt`-click on the target item. By keeping this modifier active after targeting, you can set the overall spacing based on the spacing between the key object and the *rightmost* item in the selection. Without the modifier applied, the spacing is based on the spacing used between the key object and the *leftmost* item.

**Windows:**

Instead of spacing being calculated between selection bounds, you can control spacing in relation to any targeted key object in the current selection. This targeting is done using an `Alt`-click on the target item. By then holding the `Cmd`  after targeting, you can set the overall spacing based on the spacing between the key object and the *rightmost* item in the selection. Without holding this key, the spacing is based on the spacing used between the key object and the *leftmost* item.

![Spacing objects using key objects](../../assets/shared/keyobject_spacing.png)
*A targeted key object (A) used to set spacing horizontally from the rightmost item (B) or the leftmost item (C).*

**To space layer contents:**

1. Select multiple layers.
2. On the Toolbar, click **Alignment**, click **Space Horizontally** or **Space Vertically** from the pop-up panel, and then click **Apply**.

> **Note:** With **Auto Distribute** selected (default), the layers are spaced evenly within the selection bounds. If this option is off, a specified distance between contents can be set in an input box adjacent to the option.

> **Note:** Make use of advanced distribute options in-panel by customizing the Toolbar (**View>Customize Toolbar**).

**To target a key object to space in relation to:**

1. Select multiple items.
2. With the `Alt`  pressed, click the target item. A selected key object possesses a strong outline.

**To space items using a key object:**

1. Ensure a key object is targeted as above.
2. To space in relation to the leftmost object: select **Space Horizontally** or **Space Vertically** from the Toolbar's **Alignment** menu.
3. **macOS:** To space in relation to the rightmost item: with the `Alt`  pressed, select **Space Horizontally** or **Space Vertically** from the Toolbar's **Alignment** menu.
4. **Windows:** To space in relation to the rightmost item: with the `Cmd`  pressed, select **Space Horizontally** or **Space Vertically** from the Toolbar's **Alignment** menu.

#### SEE ALSO:

- [Aligning](06-aligning.md)
