# Force Pixel Alignment

Force Pixel Alignment will snap objects, nodes and handles, and pixel selection areas to full pixels when created, moved or modified. If this option is switched off, objects and selections can occupy partial pixels.

This snapping method works together with other forms of snapping. If you snap to an object that is not aligned to a pixel, then the resulting snap will not be pixel aligned. To snap only to pixels, be sure to switch off other modes of non-pixel snapping, such as grids and guides if they are not on-pixel.

> **Tip:** Force Pixel Alignment is particularly useful for web graphic development.

## Move By Whole Pixels

In addition to Force Pixel Alignment, the **Move By Whole Pixels** option allows you to constrain the movement of objects, nodes and handles to whole pixels.

Move By Whole Pixels is particularly useful for repositioning an object by a particular pixel distance while also maintaining the relevant partial pixels an object occupies.

> **Warning:** If you deactivate **Move By Whole Pixels** but have **Force Pixel Alignment** active, moving an object which occupies partial pixels will also transform it marginally.

> **Note:** Force Pixel Alignment complements any active [snapping](11-snapping.md) settings.

**![Force Pixel Alignment](../../assets/shared/ui/force_pixel_alignment.png)

 To activate/deactivate Force Pixel Alignment:**

- Click **Force Pixel Alignment** on the Toolbar.

**![Move By Whole Pixels](../../assets/shared/ui/move_by_whole_pixels.png)

 To activate/deactivate Move By Whole Pixels:**

- With **Force Pixel Alignment** active, click **Move By Whole Pixels** on the Toolbar.

**To temporarily override snapping:**

- Press the `Alt`  while you're positioning. Snapping won't occur while the  is depressed.

#### SEE ALSO:

- [Snapping](11-snapping.md)
