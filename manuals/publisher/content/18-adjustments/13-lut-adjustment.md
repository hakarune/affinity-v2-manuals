# LUT adjustment

The LUT adjustment allows you to emulate image colors used in a variety of media platforms.

![Before](../../assets/shared/adjustment_lut_before.jpg)
![After](../../assets/shared/adjustment_lut_after.jpg)

A LUT (look-up table) remaps pixel color values based on a defined XYZ matrix. This allows you to quickly replicate the appearance of various types of media, such as reproducing the cold, blue tone attributed to science fiction and horror movies.

The look up table is stored within a file previously exported from Affinity Photo 2 or other apps (e.g., video packages). Alternatively, it can be inferred by comparing images.

![Adjustment](../../assets/shared/ui/adjustmentLayerIcon.png) Apply this adjustment via the **Adjustment** button on the **Layers** panel or via **Layer** > **New Adjustment**.

### Settings

The following settings can be adjusted in the dialog:

- **Load LUT**—sets the LUT file which gets applied to the document. In the pop-up dialog, navigate to and select a file, and click **Open**.
- **Infer LUT**— Applies a LUT adjustment without the need of a separate LUT file by comparing a 'source' image and its adjusted exported image. With a new 'target' image loaded, click **Infer LUT**, then in the pop-up dialog, navigate to and select both source and adjusted files in turn, and click **Open**.

> **Note:** The following types of LUT files are available: ***.3dl**, ***.csp**, ***.cube**, and ***.look**.

#### SEE ALSO:

- [Applying adjustments](01-applying-adjustments.md)
