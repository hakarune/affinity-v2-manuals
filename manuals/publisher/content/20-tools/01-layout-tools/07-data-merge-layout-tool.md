# Data Merge Layout Tool

The **Data Merge Layout Tool** lets you draw a grid layout on your page that will repeat as new pages are created during data merge. Data records are merged sequentially into fields in each grid layout's cells page by page.

The tool's use is optional in data merging and is intended for creating N-up print layouts. Data can also be merged into fields added directly to the publication page without using repeating layouts.

### Settings

The following settings can be adjusted from the context toolbar:

- **Preserve Cell Size**—When unchecked, your cell size will change in relation to the grid layout size. When checked, you can specify a fixed **Cell Width** and **Cell Height** once you've drawn your grid layout. Use the latter if you have a particular cell size in mind.
- **Gutter**—specifies a buffer gap around each grid cell.
- **Rows**—sets the number of rows for the grid layout.
- **Columns**—sets the number of columns for the grid layout.
- **Record Offset**—offsets which data record to start from on merging. For example, you could start from the second record instead of the first by using an offset value of 1.
- **Record Advance**—By default the next record is taken (Advance = 1) but you can skip records by setting an advance value of >1. For example, a value of 5 would only take the fifth, tenth, and fifteenth record. Setting value of 0 will repeat the first record in each cell of the first page's grid layout post merge; the second record being added to the second grid layouts. For example, use this for a whole page of mailing labels of the same record.
- ![Record Origin Top Left](../../../assets/shared/ui/record_origin_tl.png) ![Record Origin Top Right](../../../assets/shared/ui/record_origin_tr.png) ![Record Origin Bottom Left](../../../assets/shared/ui/record_origin_bl.png) ![Record Origin Bottom Right](../../../assets/shared/ui/record_origin_br.png) **Record Origin**—enable icons to set the start position in the grid that records will merge from. For example, for double-sided sheets, the cells on the back sheet need to be organized right to left (using bottom right cell setting) to match correctly with the fronts.
- ![Layout Order Rows then Columns](../../../assets/shared/ui/layout_order_rc.png) ![Layout Order Columns then Rows](../../../assets/shared/ui/layout_order_cr.png) **Layout Order**—enable icons to choose to have records fill either the grid in the order *Rows then Columns* (Column1 - Row1, Column1 - Row 2, Column2 - Row1, etc.) or *Columns then Rows* (Column1 - Row1, Column2 - Row 1, Column1 - Row2, etc.).
- **Show Record Order**—Overlays an arrow over the grid layout to indicate how records will flow according to the **Layout Order** setting.

Once the Data Area has been created it can be edited:

- **Cell Width**—Sets all cell's widths in the grid layout to a specific size, e.g. to a business card's dimensions, when the tool and grid is selected.
- **Cell Height**—Sets the height for all cells in the selected grid layout.

#### SEE ALSO:

- [Data merge](../../13-references/11-data-merge.md)
