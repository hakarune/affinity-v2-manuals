# Baseline grids

Baseline grids are perfect for creating multiple-page layouts that are consistent, professional and appealing. The baseline grid provides you with a series of equally-spaced horizontal guides that make it easy to perfectly cross-align body copy between frames and columns across your whole document.

![Before](../../assets/shared/baselinegrid_before.jpg)
![After](../../assets/shared/baselinegrid_after.jpg)

The baseline grid is overlaid over your page to help you align text. A baseline grid can be applied to the entire document or individual text frames within it, and will align baselines across linked or completely separate text frames.

The baseline grid's Grid Spacing option overrides the leading value of frame text. Setting the grid spacing to the same size as your body text leading means that your frame text should snap to, and perfectly align with, the baseline grid. The baseline grid is blue by default but can be any color you choose.

> **Note:** If you increase the font size of any text to be greater than the current Grid Spacing size, Publisher will set the line height to be twice the baseline height.

You can adjust your Document baseline grid for a baseline grid spanning across a whole page, or from the **Text Frame** panel or **Table** panel for a baseline grid that has instead been applied only to an individual text frame or table,respectively.

Frame-specific baseline grids are useful for text frames that use a different font sizes (e.g. for caption text, quotes, etc) to the main document's body text, where the frame text will adopt its own independent baseline grid rules and not those of the Document baseline grid.

> **Note:** Baseline grid settings are applicable for Frame Text only. They do not apply to Artistic Text.

### Settings

The following settings can be adjusted on a baseline grid:

- Use Baseline Grid—ticking this checkbox will enable the baseline grid.
- Start Position—specify the offset of the first grid line from the origin at **Relative To**.
- Relative To—specify what the baseline grid's starting position is in relation to. The Top of Page option is used for facing page spreads arranged vertically—you can restart the grid from the top of the second page in the spread.
- Grid Spacing—specify how far apart consecutive horizontal grid lines are.
- Color—click on the swatch to display a pop-up panel to set the line color. Drag the slider to set the opacity of the line color.
- Show Baseline Grids—ticking on this checkbox will show or hide document baseline grids (not available for baseline grids for text frames or tables).
- Display Threshold—adjust the zoom level below which document baseline grids will not be displayed (not available for baseline grids for text frames or tables). For example, choosing 100% will make the baseline grid visible at a zoom level of 100% or above.

**To enable the Baseline Grid:**

1. Do one of the following:
  - On the main toolbar, click **Show Baseline Grid**.
  - On the **View** menu, select the equivalent option.
2. From the dialog, check **Use Baseline Grid**.
3. Adjust the position and spacing of your baseline grid.

> **Note:** Text will move as the grid is adjusted using the **Grid Spacing** option, allowing you to precisely position and organize it on your page.

**To hide (show) the baseline grid:**

- From the Baseline Grid - Document dialog, uncheck/check **Show Baseline Grids**.

> **Note:** If you don't see the baseline grid immediately, ensure the document's current zoom level exceeds the grid's **Display Threshold**.

**To align text to the baseline grid:**

1. Go to the **Paragraph** panel.
2. Click on the **Spacing** tab.
3. Ensure that the **Align to Baseline Grid** checkbox is ticked.

**To snap objects to the baseline grid:**

- From the main toolbar, enable **Snapping**, then click the Snapping down arrow and ensure **Snap to Spread** is checked.

**To set up an independent text frame (or table) baseline grid:**

1. On the **Window** menu, select **Text>Text Frame** or **Table>Table**.
2. On the **Baseline Grid** section, check **Use Independent Baseline Grid**.
3. Adjust the independent grid settings.

> **Note:** If a text frame (table) is rotated relative to its governing grid, baseline grid snapping will be turned off for text in the frame.

**To ignore the underlying document baseline grid on text frames and tables:**

- With a table or text frame selected, on the **Table** panel or **Text Frame** panel, check **Ignore Baseline Grid**. Uncheck to allow the document baseline grid to influence the text frame or table again.

#### SEE ALSO:

- [Grids](04-grids.md)
- [Toolbar](../02-user-interface/02-toolbar.md)
- [Text Frame panel](../21-panels/32-text-frame-panel.md)
