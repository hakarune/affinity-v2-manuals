# Export Settings

Each file format available on the [Export dialog](03-export.md) and the Export Persona's [Export Options](../15-exporting/02-export-options-panel.md) panel offers a variety of settings that affect the resulting file(s).

> **Tip:** On the Export Options panel, the available settings are determined by the selected **Preset**.
>
>
> On the Export dialog, the available settings are determined by the file format that is selected at the top of the dialog.

## General settings

The following settings are available for all file formats, dependent on applicability to the export workflow that is in use.

|  | Export Persona | Export dialog |
| --- | --- | --- |
| **Mode**—with Selection enabled, the export options can be modified for the selected export area to be different from the default export option settings; Defaults, when enabled, sets the default export options for new slices. | ![check](../../assets/shared/check.png) |  |
| **Preset**—sets predefined export options for a range of common file formats, colour modes, and bit depths. Select from the pop-up menu. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Resample**—select which resampling method to use if the image is to be upsampled or downsampled on export. For the PDF, SVG and EPS file formats, this setting is available in the dialog's **Advanced** section.   The following resample settings are available:   - **Nearest Neighbour**—simple resampling which has the fastest processing time. Use for hard-edge images. - **Bilinear**—algorithmic resampling for use when shrinking images. - **Bicubic**—algorithmic resampling for use when enlarging images. Resampling is smoother than Bilinear but has a slower processing time. - **Lanczos 3**—complex algorithmic resampling which gives the best results but with the longest processing time. Available as 'separable' and 'non-separable'; the latter gives marginally better results, but is slightly slower than 'separable'. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Area**—instead of exporting the whole page, you can export the currently selected layer content, with or without other (deselected) layers, using the 'Selection Area' or 'Selection Only' option respectively.   To export drawn slices or specific layers, use [Export Persona](../15-exporting/01-exporting-using-export-persona.md). |  | ![check](../../assets/shared/check.png) |
| **Don't export layers hidden by Export Persona**—when selected, layers which have been hidden while in Export Persona are excluded from the exported file even if they display on the page.   If this option is off, all objects on the page (which are within the Area selected above) will be exported regardless of whether they are hidden in Export Persona. |  | ![check](../../assets/shared/check.png) |

## Multi-format settings

Availability of the following settings depends on the selected file format.

When using the Export dialog, many of these settings are only available in the dialog's **Advanced** section.

> **Tip:** If the header of the table below is out of view, hover over a tick to confirm the relevant format.

| Show descriptions:  All / None | PNG | JPEG | GIF | TIFF | PDF | PSD | SVG | WMF | EPS | EXR | HDR | TGA | WEBP | JPEG‑XL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Size**   By default, displays the native dimensions of your image. Type value(s) to set an alternative width and/or height for your exported image.    ![Locked aspect ratio](../../assets/shared/ui/locked.png)   ![Unlocked aspect ratio](../../assets/shared/ui/unlocked.png)   **Lock aspect ratio**—when selected (default), the image's native aspect ratio is honoured. If this option is off, the exported image's width and height can be set independently.   > **Warning:** If your exported design exceeds the maximum dimensions for the file format to which you are exporting, the design will be scaled on export to fit the maximum dimensions. The Export dialog will warn you about this before you proceed. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Raster DPI**   This option lets you choose the resolution for effects which will be rasterised on export. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Rasterise**   Select an option for rasterising design elements which are unsupported by the file format. Select from the pop-up menu:  - **Nothing**—no elements within the design are rasterised on export, therefore unsupported elements are not included in the exported file. - **Everything**—all elements within the design are rasterised for a resulting exported file which perfectly matches your original design. - **Unsupported properties**—only unsupported elements are rasterised in the exported file. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Downsample images**   Select whether to downsample raster images within the design. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Above (DPI)**   If this set DPI is exceeded by raster design elements, those elements will be rasterised down to this set DPI. This option is dependent on the **Downsample images** option being active. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Pixel format**   Sets the colour mode for the exported image. Select from the pop-up menu. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Use document resolution**   Ensures the export is the same DPI as the current project's setting. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Use DPI**   Overrides the current project's resolution setting for the export. The exported image's DPI is set using the adjacent input box |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Allow JPEG compression**   When selected, rasterised design elements will be compressed to decrease exported file size. If this option is off, rasterised design elements will be exported as uncompressed. |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Quality**   Sets the resulting quality of rasterised design elements in the exported image—or the overall image in the JPEG format's case. Higher quality may result in significantly larger file sizes.   For the JPEG format, this is an independent setting. For the other formats, it is dependent on the **Allow JPEG compression** option being active. |  | ![check](../../assets/shared/check.png) |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Matte**   Sets the background colour for the exported image. Select from the pop-up panel. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **ICC profile**   By default, this is set to the ICC profile of the project (document). However, the project's ICC profile can be overwritten for this export area. Select from the pop-up menu. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Embed ICC profile**   When selected, the ICC profile is included within the exported image's data, allowing the image to be viewed using the correct profile on any device. If this option is off, the viewing device must possess the ICC profile otherwise a substitute profile is used. | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Include bleed**   When selected, the bleed area of your document, if set, will be included in the output. See [Setting bleed](01-setting-bleed.md). | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| **Palettised**   When selected, encodes the exported image by mapping it to the Palette and Colours settings set below. (This option cannot be switched off for GIF images.) | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  |  |  |  |  |
| **Palette**   By default, this is set to be automatically determined. However, you can specify an encoding palette yourself. Select from the pop-up menu. | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  |  |  |  |  |
| **Colours**   Selects the number of colours available in the palette. Select from the pop-up menu. | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |  |  |  |  |  |
| **(Use) Relative coordinates**   When selected, objects in the exported file have relative positions for maximum editability. If this option is off, object positions are fixed to create a file which is optimised for viewing. |  |  |  |  |  |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Embed metadata**   When selected, any raster image's original metadata is preserved in the exported file. If this option is off, all original metadata is removed; use this for privacy reasons or to reduce file size (for web use). | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  | ![check](../../assets/shared/check.png) |  |  | ![check](../../assets/shared/check.png) |  |  |  |  |  |
| **Export text as curves**   When selected, the text in the resulting file will be drawn as curves (therefore displaying precisely as intended, even if viewed on a device without the used fonts installed). However, this option will increase file size, and text won't be editable as text or available to "text to speech" in other apps. If this option is off, text will be exported as text and the viewing device will need the used fonts installed for it to be displayed correctly. |  |  |  |  |  |  | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |  |  |  |  |  |  |
| **Compression**   By default, this is set to ZIP. For TIFF, options to apply LZW compression or no compression are available. For EXR, options include RLE, PIZ and PXR24. |  |  |  | ![check](../../assets/shared/check.png) |  |  |  |  |  | ![check](../../assets/shared/check.png) |  |  |  |  |

**macOS:**

## Settings unique to  format

## Settings unique to JPEG format

| Show descriptions: All / None |
| --- |
| **Progressive**   When selected, the exported image is progressively compressed for optimized viewing when downloading. |
| **Convert clips to paths**   When checked, converts top level clipping curves to vector paths. |

## Settings unique to TIFF format

| Show descriptions: All / None |
| --- |
| **Save Affinity layers**   Layers in the document are preserved in the exported TIFF image. These layers will only be readable when the file is opened in an Affinity application. |

## Settings unique to PDF format

| Show descriptions: All / None |
| --- |
| **Preview export when complete**   Opens the exported file in your device's default PDF viewer. |
| **Compatibility**   Sets the version and type of PDF to be exported. Select from the pop-up menu. |
| **Colour Space**   Choose whether to use the document's current colour space or export using a selected colour space. Select from the pop-up menu. |
| **Profile**   Choose whether to use the document's current colour profile or export using a specific colour profile. Select from the pop-up menu. |
| **Embed profiles**   When selected (default), the chosen (or document's) colour profile will be embedded in the exported file. If this option is off, the exported file will not have the colour profile embedded with it (the viewing device will need to have the appropriate colour profile installed to view the exported PDF accurately). |
| **Convert image colour spaces**   When checked, all placed images will convert to the colour space chosen on export (as set in the **Profile** option above). When unchecked, the colour space of the imported placed image is honoured. |
| **Honour spot colours**   When selected, spot colours within the design are exported as spot colours. If this option is off, spot colours are converted to an equivalent colour within the exported file's colour space (see above). |
| **Overprint black**   When selected, design elements which use CMYK black are set to overprint. If this option is off, CMYK black elements are set to be indistinguishable to other colours during printing. |
| **Include hyperlinks**   When selected, the PDF output will include all created hyperlinks. |
| **Include bookmarks**   When selected, PDF bookmarks are included in the PDF output. (Primarily used when working on Affinity Publisher documents in Affinity Designer or Affinity Photo.) |
| **Include layers**   When selected, the PDF output will include all created layers (except invisible/hidden layers unless the corresponding setting is also selected). |
| **Include invisible layers**   When selected, layers at the top hierarchical level that are hidden and contain child layers that are not hidden will be included in the PDF output as invisible layers. |
| **Include printers marks**   When selected, the PDF output will show printer marks around the page edge. All printer marks are added by default. However, particular types of printer marks can be switched off, depending on your preference. These include:   - Crop marks - Registration marks - Colour and greyscale bars - Page information   > **Note:** Professional printing services often print on larger sheets and trim them to your page design's size. To ensure movement during printing does not result in white edges, make your design fill the document's bleed area, turn on **Include bleed** to add this information to your PDF file, and turn on **Include printers marks** to assist with trimming. |
| **Embed fonts**   Select an option for handling fonts used in the document.   - **Text as Curves**—all text is converted to curves. This ensures the resulting exported file will display correctly regardless of the fonts installed on the viewing device. - **All Fonts**—any fonts used in the document are embedded in the exported file. This ensures the resulting exported file will display correctly regardless of the fonts installed on the viewing device. - **Uncommon Fonts**—fonts used are only embedded in the exported file if they are not part of the fonts traditionally installed on most devices. The viewing device must have the expected fonts installed to view any common fonts in the exported file. - **No Fonts**—no fonts are embedded in the exported file. A viewing device must have all the used fonts installed to accurately view the exported file. |
| **Subset fonts**   When selected, embedded fonts will only include the glyphs used in the document. If this option is off, all glyphs for the used fonts are embedded in the exported file, regardless of whether they appear in the document or not. |
| **Allow advanced features**   When selected, all design features supported by the PDF file format are exported as vectors. If this option is off, depending on the nature of these features, they are rasterised or converted to curves on export. These features include:   - Artistic text which has been horizontally or vertically stretched. - Text which has an applied stroke. - Linear and radial gradients. - Non-solid transparencies.   > **Warning:** If the **Allow advanced features** option is selected on export, the resulting PDF, when imported into other applications, may cause the above advanced features to be rasterised or rendered incorrectly. The third party's app may also display an error message on PDF import. |

## Settings unique to PSD format

| Show descriptions: All / None |
| --- |
| **Compatibility mode**   When selected, the exported file will be compatible with other applications which do not support some features (file size may also increase). If this option is off, the exported file may not be readable by other applications (depending on the features used in the image). |
| **Smallest file sizes**   When selected, the exported file will be compressed where possible but may not be readable by other applications. If this option is off, no compression will take place for the exported file. |
| **Rasterise all layers**   When selected, layer content is rasterised in the exported file (the layer structure is retained). If this option is off, no rasterisation takes place on export. |
| **Gradients**   This setting offers two strategies for how to export this specific project attribute. Select from the pop-up menu.   - **Preserve accuracy**—the listed attribute will be rasterised to preserve its intended design. - **Preserve editability**—the listed attribute will be exported with its original settings to allow for easy editing. |
| **Adjustments**   This setting offers two strategies for how to export this specific project attribute. Select from the pop-up menu.   - **Preserve accuracy**—the listed attribute will be rasterised to preserve its intended design. - **Preserve editability**—the listed attribute will be exported with its original settings to allow for easy editing. |
| **Layer effects**   This setting offers two strategies for how to export this specific project attribute. Select from the pop-up menu.   - **Preserve accuracy**—the listed attribute will be rasterised to preserve its intended design. - **Preserve editability**—the listed attribute will be exported with its original settings to allow for easy editing. |
| **Lines**   This setting offers two strategies for how to export this specific project attribute. Select from the pop-up menu.   - **Preserve accuracy**—the listed attribute will be rasterised to preserve its intended design. - **Preserve editability**—the listed attribute will be exported with its original settings to allow for easy editing. |
| **Adv Blending**   This setting offers two strategies for how to export this specific project attribute. Select from the pop-up menu.   - **Preserve accuracy**—the listed attribute will be rasterised to preserve its intended design. - **Preserve editability**—the listed attribute will be exported with its original settings to allow for easy editing. |

## Settings unique to SVG format

| Show descriptions: All / None |
| --- |
| **Export text as curves**   When selected, the text in the resulting file will be drawn as curves (therefore displaying precisely as intended, even if viewed on a device without the used fonts installed). However, this option will increase file size, and text won't be editable as text or available to "text to speech" in other apps. If this option is off, text will be exported as text and the viewing device will need the used fonts installed for it to be displayed correctly. |
| **Longer text spans**   When selected, text is placed relative to previous lines of text (therefore producing smaller file sizes and simpler file structures). If this option is off, text is placed with absolute coordinates |
| **Use hex colours**   When selected, colours in the exported file are expressed as RGB Hex values (therefore reducing file size but less human-readable). If this option is off, colours are exported as standard RGB values. |
| **Flatten transforms**   When selected, transformed objects are 'fixed' in the exported file. This allows for the file to be viewed more accurately across applications. If this option is off, objects remain dynamically transformed to allow for more flexible editing. |
| **Use tile patterns**   When selected, rasterised areas may be converted to a vector shape with a filled bitmap to give smoother, sharper edges. However, this might not be supported by some apps. If this option is off, objects will exist as singular elements within the exported file. |
| **Set viewBox**   When selected, the exported file includes coordinates and dimensions which define the view box of the image. If this option is off, no view box data is included in the exported file. The export area is used to define the view box. |
| **Add line breaks**   When selected, the code in the exported file will be optimized for human viewing and reading. If this option is off, the image will be exported with code on a single line which will make the file size significantly smaller. |

## Settings unique to WMF format

| Show descriptions: All / None |
| --- |
| **Enhanced Windows Metafile**   When checked, the exported file with be in EMF format. When unchecked, the export file will be in WMF format. |
| **Clip Transparency**   When checked, any transparent area around your content is absent in the exported file. When unchecked, the transparent area is retained. |

## Settings unique to EPS format

| Show descriptions: All / None |
| --- |
| **PostScript level**   Sets the version of the exported PostScript file. Select from the pop-up menu. |
| **Minimise size**   When selected (default), the exported file will be compressed to create the smallest file size possible. |

## Settings unique to EXR format

| Show descriptions: All / None |
| --- |
| **Colour profile from name**   This is dependent on OpenColorIO. With a valid configuration, appending the filename during export will convert to that colour space from scene linear. For example, name your file *output acescg.exr* to convert to ACEScg if your OCIO configuration lists that as a valid colour space. |
| **Multi channel**   When exporting to OpenEXR format, converts layers with affixes—e.g. .RGB or .RGBA after the layer's name—back to multi channel data. |
| **Include unknown channels**   When checked, channels whose type cannot be determined will still be exported as a single luminance-based channel. |
| **Image pixels**   Choose whether to encode Image channels (**RGBA** etc) as 16-bit (half float) or 32-bit (full float). |
| **Spacial pixels**   Choose whether to encode Spatial channels (**XYZ** etc) as 16-bit (half float) or 32-bit (full float). |
| **Other pixels**   Choose whether to encode other/undetermined channels as 16-bit (half float) or 32-bit (full float). |

## Settings unique to WEBP format

| Show descriptions: All / None |
| --- |
| **Lossless**   When checked, the newer, lossless WebP compression algorithm is used. |

#### SEE ALSO:

- [Export dialog](03-export.md)
- [Export Persona](../15-exporting/01-exporting-using-export-persona.md)
- [Export Options panel](../15-exporting/02-export-options-panel.md)
