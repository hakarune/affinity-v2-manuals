# Duplicating

Affinity Photo 2 lets you make duplicate layers to increase workflow or to temporarily create a 'backup' layer. Move data entry and power duplicate features also allows you to duplicate and repeatedly transform layer contents.

Affinity lets you make copies of your original layer content using several methods.

- Creating a single duplicate using a command.
- Creating many offset duplicates by using Move data entry.
- Creating many offset duplicates by using power duplicate.

![Before](../../assets/images/panel_layers_duplicate_before.png)
![After](../../assets/images/panel_layers_duplicate_after.png)
*Layers panel before and after layer duplication.*

**To duplicate:**

Do one of the following:

- On the page, drag a selected layer with the `Cmd`  pressed. While dragging, release the key to move the layer instead, or press the key while moving to duplicate rather than move.
- On the **Layers** panel, `Click`-click a layer, group or object and select **Duplicate**.
- On the **Layers** panel, press the `Alt`  down and drag the layer you would like to duplicate into its position.
- With an object selected, select **Layer>Duplicate**.

> **Note:** A duplicated layer is placed immediately above the original layer.

## Duplicate using Move data entry

As well as moving, rotating and sizing an individual object precisely, Move data entry lets you create any number of copies of an object in one operation which, when combined with move, rotate and scale operations, leads to some striking object transformations.

Move data entry has the following characteristics:

- You can duplicate curves and text as well as shapes
- It is controlled via a dialog
- Your chosen transformation is previewed on the page
- You can edit the properties of the object being transformed (affecting its its previewed duplicates) as well as its transform origin while the dialog remains open
- The duplicate(s) can be placed in front of or behind the original object
- The previous settings can optionally be used
- Scaling is cumulative, e.g. 80% scaling is applied to each duplicate in turn

![Examples of Move data entry](../../assets/shared/movedataentry_examples.png)
*(A) Linear offset (Horizontal: 6mm; Number of copies: 6),  
 (B) Rotating (Rotation: 30°; Number of copies: 12),  
(C) Scaling (Scale: 80% and 110%; Number of copies: 6),  
(D) Rotating and Scaling (Rotation: -4°; Scale: 93% and 101%, Number of copies: 50)*

You can achieve very different duplication results if you experiment with the **Insertion mode** option on the dialog.

![Insertion mode in front of or behind items](../../assets/shared/movedataentry_insertionmode.png)
*Effects of Insertion mode when set to add duplicates in front of (A) or behind (B) the original item*

> **Tip:** Try repositioning the object's transform origin on the page before using Move data entry—this lets you rotate duplicated objects around the origin to create ringed designs.
>
> ![Move data entry to Duplicate about Transform Origin](../../assets/images/move_data_entry_duplicate2.png)

**To duplicate (by Move data entry):**

1. With the **Move Tool** active, select one or more layers or groups.
2. Press the `Return`  to display a **Move / Duplicate** dialog.  
Enter new settings that will offset the duplicate(s) from its original position, with optional **Angle**, **Rotation** and **Scale** settings. The **Distance** setting is the measurement between duplicate layer midpoints.

  ![Move data entry to Duplicate](../../assets/images/move_data_entry_duplicate.png)
3. Check **Duplicate** and set the **Number of copies** you want.
4. (Optional) Choose an **Insertion mode** to add duplicate objects either in front of (![Insert new items in front](../../assets/shared/ui/insert_top_of_layer.png) **Insert new items in front**) or behind (![Insert new items behind](../../assets/shared/ui/insert_behind_selection.png) **Insert new items behind**) the original object.
5. Click **OK**.

Click **Reset** to clear previously applied settings and remove the duplicates.

Pressing the `Esc`  will cancel the operation; the entered settings will still be remembered.

> **Note:** If you swap to another tool while the dialog is open, the dialog and any object previews will disappear.

## Power duplicate

If you duplicate a layer(s) and then transform the duplicated contents, you can immediately duplicate the layer containing the transformed content. The transform is applied accumulatively to subsequent duplicates.

![Power duplicate](../../assets/shared/power_duplicate.jpg)
*(A) original content, (B) original content duplicated and rotated, (C) transformed duplicate duplicated numerous times.*

**To power duplicate:**

1. Select the layer(s).
2. From the **Layer** menu, select **Duplicate**.
3. Transform the duplicated layer content.
4. From the **Layer** menu, select **Duplicate**. A duplicate is created and the transform is automatically applied to the duplicate.
5. Repeat step 4 to create more duplicates with the transform accumulatively applied.

## Duplicating selections

If you have made a selection, you can immediately duplicate the selected content into a new layer (or layers).

**To duplicate selected content:**

1. Select content within the layer(s).
2. From the **Layer** menu, select **Duplicate Selection**.
3. The selected content will be duplicated into a new layer. If content has been selected across multiple layers, the content will be duplicated into multiple separate new layers.

#### SEE ALSO:

- [Selecting](02-selecting.md)
- [Transforming](../05-sizing-cropping-and-warping/05-transforming.md)
- [Keyboard shortcuts for layer operations](../36-keyboard-shortcuts/01-keyboard-shortcuts.md)
