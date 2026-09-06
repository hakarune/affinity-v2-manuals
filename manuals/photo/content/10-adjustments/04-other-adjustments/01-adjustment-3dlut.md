# LUT adjustment

The LUT adjustment emulates image colors used in a variety of media platforms.

![Before](../../../assets/shared/adjustment_3dlut_before.jpg)
![After](../../../assets/shared/adjustment_3dlut_after.jpg)

A LUT (look-up table) remaps pixel color values based on a defined XYZ matrix. This allows you to quickly replicate the appearance of various types of media, such as reproducing the cold, blue tone attributed to science fiction and horror movies.

The look up table is stored within a file previously exported from Affinity Photo 2 or other apps (e.g., video packages). Alternatively, it can be inferred by comparing images.

### Settings

After selecting an individual LUT from the LUT adjustment, the following settings can be adjusted:

- **Load LUT**—sets the LUT used in the adjustment. In the pop-up dialog, navigate to and select a file, and click **Open**.
- **Infer LUT**—applies a LUT adjustment without the need of a separate LUT file by comparing a 'source' image and its adjusted exported image. With a new 'target' image loaded, click **Infer LUT**, then in the pop-up dialog, navigate to and select both source and adjusted files in turn, and click **Open**.

> **Note:** The following types of LUT files can be loaded: ***.3dl**, ***.csp**, ***.cube**, and ***.look**.

The following options are available from the adjustment:

- Category—displays the currently active category. Select from the pop-up menu.

![Panel Preferences](../../../assets/shared/ui/cogicon.png) The following options are available from the adjustment's **Options** menu:

- **Create New Category**—adds a new, custom LUT category to the panel.
- **Rename Category**—allows you to rename the currently selected category.
- **Delete Category**—removes the currently selected category (and all its LUTs) from the panel.
- **Duplicate Category**—adds a second copy of the currently selected category to the panel. The new copy is not automatically linked to your other Affinity apps.
- **Link Category**—makes the currently selected category available in all your Affinity 2 apps.
- **Sort Categories By**—allows you to sort the contents of the Category pop-up menu by **Name** or **Date Added**.
- **[Import LUT Category](../../29-add-ons/04-importing-add-ons.md)**—adds multiple LUTs from an .afluts file to the panel as a new category.
- **Export LUT Category**—creates an .afluts file containing the currently selected category and all its LUTs, as a backup or to share.
- **[Import LUTs](../../29-add-ons/04-importing-add-ons.md)**—adds one or more individual LUTs from external files to the currently selected category.
- **Sort LUTs By Name**—arranges the currently selected category's contents in alphabetical order.

> **Note:** LUTs within a category can be dragged up or down to set the order in which they are listed. Whether you sort a category's LUTs manually or automatically, their order is remembered for future editing sessions.

**macOS:** The following options are available by `Click`-clicking an individual LUT:

**Windows:** The following options are available by right-clicking an individual LUT:

- **Rename**—allows you to rename the LUT.
- **Delete**—removes the LUT from the panel.
- **Move To Category**—select a different category in which the LUT should be stored.
- **Export LUT**—creates a file containing the individual LUT, as a backup or to share.

**To export LUTs:**

1. On the **Adjustment** panel, `Click`-click the LUT you want to export, then select **Export** from the pop-up menu.
2. Adjust settings in the dialog.
3. Click **Export**.

#### SEE ALSO:

- [Applying adjustments](../01-applying-adjustments.md)
- [Exporting custom adjustments as LUTs](../05-exporting-custom-adjustments-as-3d-luts.md)
- [Importing add-ons](../../29-add-ons/04-importing-add-ons.md)
