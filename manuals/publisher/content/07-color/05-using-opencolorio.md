# Using OpenColorIO

In addition to 32-bit editing support, Affinity Publisher also implements OpenColorIO; a color management system that provides a full color-managed workflow. It is predominantly used for motion picture production but can be used for any situation where accurate end-to-end color management is required. All Affinity apps support both OCIO v1 and v2 color management configurations.

## Setting up OpenColorIO

By default, Publisher's OpenColorIO features are not immediately usable. An **.ocio** configuration file is required alongside a number of supporting files such as lookup tables.

The OpenColorIO website (http://www.opencolorio.org) contains some sample configurations that provide a number of suitable input and output profiles, including several Academy Color (ACES) configurations.

**To configure OpenColorIO:**

1. Download and extract (**.ocio** v1 only) your chosen OpenColorIO configuration to a folder.
2. **macOS:** From the **Affinity Publisher** menu, select **Settings** (or **Preferences**).
3. **Windows:** From the **Edit** menu, select **Settings**.
4. On the **Color** tab, under **OpenColorIO Configuration File**, choose **Select** and navigate to the **.ocio** file destination folder. Choose the **.ocio** configuration file within this folder.
5. **macOS:** Under **OpenColorIO Search Folder**, click **Select** and choose the destination folder (it should already be the current highlighted folder from when the **.ocio** configuration file was selected).
6. You will be prompted to restart the app, which is necessary for the OpenColorIO settings to take effect.

## Using OpenColorIO

OpenColorIO is exposed through two methods:

- The **32-bit Preview** panel contains a **Display Transform** option that only becomes available with a valid OpenColorIO configuration. This can be used to achieve a non-destructive, color managed workflow.
- An **OCIO** adjustment layer (see [OCIO Adjustment](../18-adjustments/14-opencolorio-adjustment.md)) can be added to losslessly convert between color spaces. You can have multiple **OCIO** adjustment layers within a document, which allows you to accommodate composite layers from different color spaces. An example layer stack might be (in hierarchical order):
  - **OCIO Adjustment**—from ***Utility - Linear - sRGB*** back to ***Role - scene_linear***
  - **sRGB Pixel Layer**—composite element
  - **OCIO Adjustment**—from ***Role - scene_linear*** to ***Utility - Linear - sRGB***
  - **Pixel Layer**—original layer

![OCIO Adjustment](../../assets/images/adjustment_ocio.png)
*An OCIO Adjustment layer going from **Role - scene_linear** to **Utility - Linear - sRGB**.*

> **Note:** When loading OpenEXR documents, Publisher always converts from the source color space to **scene_linear**. With a valid OpenColorIO configuration, Publisher will also present a message to let you know which color profile it has converted from. This is usually determined by a filename affix, for example **"render_acescg.exr"**.

#### SEE ALSO:

- [OCIO Adjustment](../18-adjustments/14-opencolorio-adjustment.md)
