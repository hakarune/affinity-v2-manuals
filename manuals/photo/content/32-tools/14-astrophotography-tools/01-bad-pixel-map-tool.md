# Bad Pixel Map Tool

The Astrophotography Stack Persona's **Bad Pixel Map Tool** provides automatic and manual methods of identifying defective pixels in specific kinds of calibration frame.

### Settings

The following settings can be adjusted from the context toolbar:

- ![Presets manager](../../../assets/shared/ui/cogicon.png) **Presets**—opens a list of presets and also allows access to the **Preset manager**.
- **Detect bad pixels**—if you have supplied any dark or flat frames, checking this option attempts to automatically identify hot and cold pixels in them, respectively.
- **Hot pixel threshold**—a numeric value that controls how readily pixels in a dark frame are identified as defective.
- **Cold pixel threshold**—a numeric value that controls how readily pixels in a flat frame are identified as defective.
- **Mode**—when **Pixel** is selected, you can zoom in and click on a specific pixel to identify it as defective, so it will be remapped. When **Column** is selected, you can highlight any column defects, which causes the entire column of pixels to be remapped.
- **Reset**—resets all pixel mapping.
- **Show bad pixels**—when checked, hot and cold pixels are indicated in the document view.
- **Show Bayer**—only applies to image formats that require debayering, e.g. full color. When checked, the tool switches to the Bayer pixel format so you can easily identify singular bad pixels.

> **Tip:** Saving a bad-pixel map as a preset avoids the need to manually recreate it each time images from the same camera setup are processed.

#### SEE ALSO:

- [Cloning and healing](../../09-retouching/04-cloning-and-healing.md)
- [Healing Brush Tool](../07-retouch-tools/10-healing-brush-tool.md)
- [Sources panel](../../33-panels/24-sources-panel.md)
