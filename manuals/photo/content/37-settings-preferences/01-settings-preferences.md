# Settings

Settings comprise a series of miscellaneous options that are applied across your app. They can be used to set up your own way of working.

Show settings for:

#### General options

| Name | Description |
| --- | --- |
| **Reopen document on startup** | Choose whether to restore the last session when launching app. |
| **Limit initial zoom to a maximum of 100%** | Choose whether to limit initial zoom to a maximum of 100% when loading files. |
| **Documents open in a new floating window** | Choose whether documents open in a floating window separate from the app's main window. |
| **Documents open in the current active group** | Choose whether documents open in the current active group, meaning the most recent floating window, or in the app's main window. |
| **Hide file extension** | Select whether to show or hide file extensions. |
| **Automatically update linked resources when modified externally** | Choose whether to automatically link newly created or imported content categories to all Affinity 2 apps on your device. |
| **Save thumbnails with documents** | You can exclude your thumbnail from being stored with your document. |
| **Enable "Save" over imported PSD files** | Choose whether to overwrite imported PSD files when using the **Save** command, rather than creating an *.afdesign file. We recommend reading the warning provided in the dialog before selecting this option. |
| **Normalize breaks on copy plain text** | Choose whether your pasted plain text retains breaks' consistency prior to further formatting. |
| **Insert filler text as text** | Choose whether to insert filler text as editable text. |
| **Import PSD text as text rather than bitmap** | Choose to open PSDs with editable text objects. |
| **Copy items as SVG** | Choose whether to create SVGs on the clipboard when copying objects for better cross-platform interaction. |
| **Prefer metafile to raster when pasting from external application** | Choose whether to prefer metafile to raster when pasting from external app. |
| **Load metadata from XMP sidecars** | Choose whether to import metadata from an XMP sidecar file automatically when opening the corresponding image, provided they have the same base filename and the sidecar file has the .xmp file extension (in lower case). |
| **Refine HEIC depth maps** | Choose whether to automatically refine HEIC depth maps. |
| **Import PSD smart objects where possible** | Choose whether to allow Affinity to import smart objects; by default, Affinity Photo converts Smart Objects in Photoshop documents to pixel layers. Note that smart objects that are linked, meaning their content comes from an external file, are not converted to embedded documents. |
| **Only return safe results for stock image searches** | Choose whether to apply a safe-search filter while searching for stock images. |
| **Link new content categories** | Choose whether newly created content categories are linked, and thus recognized by Affinity apps, on the same device. |
| **Enable file sharing on the local area network** | Choose whether file sharing is available on LAN. Additionally, opt for sharing via the Same Affinity account only, if preferred. |
| **Send anonymous usage information** | Send anonymous usage information collects Analytics data related to your computer OS, hardware and app usage for continual product improvement. This data is used for statistical analysis. Absolutely no personal information, as covered by data protection rules, is contained in the data collected. |
| **Open Lens Profiles Folder in Finder/Explorer** | You can open your app's lens profiles folder, where you can view, add and/or remove the currently pre-installed lens profiles. |
| **Open Affinity Fonts Folder in Finder/Explorer** | You can open your app's fonts folder, from which Affinity Font (.affont) files (previously installed by dragging onto the app) can be removed to uninstall them. (Affinity Fonts installed via the Account feature can be uninstalled using that feature.) |
| **Language** | Sets the UI language independently of the operating system. Select from the pop-up menu. |

#### Machine Learning

| Name | Description |
| --- | --- |
| **Machine Learning Models** | These optional features use Machine Learning (ML) models for automatic object and subject selection. This is in line with Affinity’s ambition to use ML for the benefit of faster workflow. Models are installed as pre-trained and because these operations all work 'on device' none of your data leaves your device at any time. These models and linked functionality are only available on Apple Silicon macOS devices running macOS Ventura 13.0 and newer as well as on Windows x64 and Arm64 hardware running Windows 10 or 11. |
| **Inference** | Choose whether you want to allow both CPU and GPU to perform machine learning operations in tandem, or allow for CPU processing only. |
| **Segmentation** | This model allows Affinity to create precise, detailed pixel selections from pixel layers or placed images. Use the **Object Selection Tool** to make your selections. |
| **Saliency** | This model allows Affinity to recognize the most prominent subject on a pixel layer or placed image. Install it alongside the Segmentation model to enable the single-click **Select Subject** item. |

#### Color options

| Name | Description |
| --- | --- |
| **Color Profile** | You can set up your default RGB, 32bit RGB, CMYK, Grayscale and LAB color profiles for use in future documents. Select from the pop-up menus. |
| **Rendering Intent** | **Rendering Intent**—choose the rendering intent for your images. Select from the pop-up menu. |
| **Black point compensation** | Choose whether to apply black point compensation when opening an image. |
| **Convert opened files to working space (and warn)** | Choose whether to convert an opened file's color space to the working space and also choose whether to warn that this has occurred. |
| **Warn when assigning working profile to unprofiled files** | Choose whether to receive a warning when a working profile is assigned to an unprofiled image. |
| **Enable EDR by default in 32bit RGB views** | Choose whether to allow for the extended dynamic range images to be displayed in 32bit RGB mode. |
| **OpenColorIO Configuration File: Select** | Select a OpenColorIO Configuration File. |
| **OpenColorIO Search Folder: Select** | Select a OpenColorIO Search Folder. |
| **Perform OCIO conversions based on filename (and warn when converting on load)** | Choose whether OCIO conversions are based on file name and also choose whether to warn that this has occurred. |
| **Associate OpenEXR alpha channels** | Choose whether to merge EXR alpha channel information to its associated RGB pixel layer's alpha channel. |
| **Post divide EXR colors by alpha** | Choose whether to divide EXR color channels by the alpha channel. |
| **Perturb zero EXR alpha** | Choose whether to leave zero alpha information untouched, or, with **Post divide EXR colors by alpha** enabled as well, for zero alpha information to be altered so post-division with color channel information can be achieved. |

#### Performance options

| Name | Description |
| --- | --- |
| **RAM Usage Limit** | **RAM Usage Limit**—allows you to set your preference for optimizing app performance for your projects. |
| **Disk Usage Warning At** | **Disk Usage Warning At**—choose the limit at which you are warned about disk usage. |
| **Undo Limit** | **Undo Limit**—choose the history length you are able to access. |
| **View Quality** | **View Quality**—choose the way in which the image displays during modifications. Select from the pop-up menu. |
| **Dither gradients** | Choose whether to dither gradients, when working on projects, to speed up performance. |
| **Use precise clipping** | Choose a clipping option for optimizing performance. |
| **File Recovery Interval** | **File Recovery Interval**—sets the interval for saving temporary data for currently open documents, allowing a document restore to be offered at startup if the app develops a fault. |
| **Display** | **Display**—choose whether to use hardware acceleration such as **Metal**, **OpenGL** or **OpenGL (Basic)**, or use **Software** acceleration. If your computer experiences performance problems, use the above option order until performance is acceptable. If your Mac has an additional discrete graphics card, checking the **Use only integrated GPU** will not allow access to it, therefore reducing power consumption and conserving battery life (useful for unplugged MacBook Pros). |
| **Renderer** | **Renderer**—choose your rendering experience. Select from the pop-up menu. **Default**—renders using the default method - typically the installed graphics card. ***Graphics display adapter***—the name here varies depending on your graphics card and its driver. If you have multiple graphics cards installed you may see more than one option here. **WARP**—use Windows Advanced Rasterization Platform just for presenting the document. Try this if you are experiencing performance issues with the default option. |
| **Retina Rendering** | Choose your rendering experience. Select from the pop-up menu. **Automatic (Best)**—renders as non-retina followed by retina for balanced performance and quality. **Low quality (Fastest)**—renders as non-retina only for highest performance level but compromises on quality. **High quality (Slowest)**—renders as retina only for high quality but may compromise performance. |
| **Hardware Acceleration** | Checking **Enable Metal compute acceleration** boosts some tasks' performance if a compatible GPU is available. See the [Hardware acceleration](../35-extras/03-performance/01-hardware-acceleration.md) topic. |
| **Hardware Acceleration** | Checking **Enable OpenCL compute acceleration** boosts some tasks' performance if a compatible GPU is available. See the [Hardware acceleration](../35-extras/03-performance/01-hardware-acceleration.md) topic. |

#### User interface options

| Name | Description |
| --- | --- |
| **Background Grey Level** | Controls the grayscale level of the pasteboard surrounding the document. |
| **Artboard Background Grey Level** | Controls the grayscale level of the pasteboard surrounding artboard(s). |
| **Text Contrast** | Adjusts the luminance of text in the user interface. |
| **UI Brightness** | Adjusts the luminance of window backgrounds in the user interface. |
| **UI Contrast** | Instantly sets Text Contrast and UI Brightness for high contrast between text and window backgrounds, or to their default values. |
| **UI Font Size** | Optionally increase the font size of UI text. |
| **UI Style** | Displays the user interface in a dark or light style or a default style which sets the UI depending on your operating system version's setting. |
| **UI Style** | Displays the user interface in a dark or light style. |
| **Icon Style: Color/Mono** | Makes icons display in color/grayscale (monochromatic iconography), respectively. |
| **Tooltip Delay** | Set the length of time before a tooltip appears when hovering over a UI element. |
| **Decimal Places for Unit Types** | Controls the number of decimal places allowable for each document measurement unit and degree readouts. |
| **Automatically lock background layer on import** | Locks (or keeps unlocked) an imported image as a background layer. |
| **Show Lines in points** | Choose whether line width (thickness) displays in points or in the document's measurement units. |
| **Show Text in points** | Choose whether text is expressed in points or in the document's measurement units. |
| **Show brush previews** | Choose whether the brush cursor display a preview of pixels to be placed. When enabled, a circular preview of the current brush's nozzle is displayed; disable the option to hide the nozzle preview if the preview obscures existing page content. When **Force pressure** on the brush tool's context toolbar is enabled, previews are automatically disabled. |
| **Always show brush crosshair** | Overlays a cross-hair over the brush cursor for better targeting. |
| **Auto commit filters** | Choose whether to commit filters if subsequently carrying out a new operation while the Apply dialog is still open or whether to receive a prompt to Apply or Discard the filter instead. Clicking Apply will always commit the filter, irrespective of the this setting. |
| **Always use white background for font dropdown** | Choose whether to preview fonts on a white (default) or black background in the font selection dropdown list. |
| **Enable touch bar support** | Choose whether to activate Touch Bar support. Enabling this option requires app restart. |
| **Enable Pointer Support** | Choose whether to enable pointer support. Enabling this option requires app restart. |
| **Ask for name when creating Layers and Groups** | Choose whether you would like to be prompted to name a new layer, group or warp group upon creation. |

#### Tools options

| Name | Description |
| --- | --- |
| **Tool Handle Size** | Makes selected layer content's bounding box handles and curve nodes (and handles) smaller or larger. |
| **`Ctrl`-click show context menu** | Choose whether `Click`-click displays context menus (alternative to right-click with a multi-button mouse). |
| **Force Touch context menu** | Enable or disable the Force Touch context menu; when enabled, the menu is accessed by a strong-press on a Force Touch-compatible trackpad. |
| **Select object when intersects with selection marquee** | Choose whether an object is added to a selection when partially covered by the selection marquee or whether it has to be encompassed by the marquee. |
| **Use `Shift` modifier to cycle tools** | When enabled, cycling between tools is only possible with the  modifier pressed. Affects text and shape tools, and Pixel Persona's Paint Brush/Pixel, Selection and Dodge/Burn tool cycles. |
| **Use `Shift` key to cycle tool groups** | When enabled, cycling between tool groups is only possible with modifier pressed. |
| **Use mouse wheel to zoom** | Choose whether the middle mouse button will allow scrolling or zooming. |
| **Use 'scrubby' zoom** | Choose whether dragging with the Zoom Tool zooms around the cursor (scrubby zoom) or creates a 'zoom to' marquee. |
| **Enable Dial support** | Check the option to use Surface Studio's Surface Dial (or equivalent radial device). |
| **Enable canvas rotation with trackpad** | Choose if the canvas can be rotated using a trackpad or not. |
| **Enable canvas rotation with `Cmd` +scroll wheel** | Choose if the canvas can be rotated using a scroll wheel or not. |
| **Enable canvas rotation with `Alt` +scroll wheel** | Choose if the canvas can be rotated using a scroll wheel or not. |
| **Touch for gestures only** | When enabled, only your connected tablet pen can use tools on the canvas but you can still use gestures. Useful for preventing accidental tool use when interacting with the canvas. When disabled, you have full touch control plus gestures, with or without a tablet pen. |
| **Move Tool Aspect Constrain** | Controls the default constraining behavior when resizing objects using the Move Tool. Select from the pop-up menu. |
| **Tablet input method** | Choose whether your tablet pen should use the best quality high resolution input data (if supported), low resolution input data (the system cursor position—this setting is switched on by default), or enable Windows Ink in your drivers. |
| **Create Text with Blend Gamma** | Controls the default blend gamma applied to text on creation. |
| **Nudge Distance** | Sets the nudge amount by which an object is moved when using the arrow keys. Select measurement units from the pop-up menu. |
| **Modifier Nudge Distance** | Sets the amount by which an object is moved when using the arrow keys along with the `Shift` . |
| **Synchronize tools between documents** | Makes tool settings persistent between different documents. |
| **Additional dictionary folder** | Add an additional folder that you can copy dictionary files into. The directory is scanned during start-up and found dictionaries will be added. |

#### Shortcuts options

| Name | Description |
| --- | --- |
| **Shortcuts** | Use these options to define your own keyboard shortcuts. See the [Customizing keyboard shortcuts](../31-workspace/04-customize/01-keyboard-shortcuts.md) topic. |

#### Assistant options

When you perform certain operations—for example, pixel painting (or erasing) on vector layers, or applying adjustments to selections—the Assistant will take action according to your preferences and display an alert message to make you aware.

Use these options to control overall Assistant behavior:

| Name | Description |
| --- | --- |
| **Enable assistant** | When checked, the Assistant will perform your chosen action for any operation it can help with. When unchecked, the Assistant does not perform any actions. |
| **Automatically undo and redo assistant actions** | When checked, any action that has been recorded as multiple consecutive history states is treated like one state by the Undo and Redo commands. When unchecked, the commands need to be selected multiple times to undo/redo multi-state Assistant actions. |
| **Alert when assistant takes an action** | When checked, the Assistant will display an alert message whenever it takes action. When unchecked, alert messages are not displayed. |

Use these options to specify the required action for various operations and tool behaviors:

| Name | Description |
| --- | --- |
| **Painting with no layer selected** | In Pixel Persona, you can choose to create a new pixel layer for your brush strokes using 'Add new pixel layer and paint'; 'Take no action' means that no pixel painting is allowed. If a vector layer is selected, a new pixel layer is created above the vector layer. If a pixel layer is selected, your brush stroke is added to the pixel layer. |
| **Erasing from vector layers** | In Pixel Persona, this option lets you choose to erase on a created pixel mask over your vector object, immediately rasterize the vector layer and erase directly on it, or take no action. |
| **Other brushes on vector layers** | For retouching pixel brushes (e.g., Burn Brush Tool, Smudge Brush Tool, etc.), any applied brush stroke rasterizes the vector layer by default. You can change this behavior by selecting 'Take no action', which doesn't convert the layer or apply the stroke. |
| **Brush tool sharing** | Choose whether a selected brush and context toolbar settings are shared between tools of a similar nature (e.g. Dodge, Burn and Sponge Brush Tools), shared across all tools, or each tool's brush is set independently. |
| **Applying filters to vector layers** | When a filter is added to a vector layer, the Assistant can either rasterize the vector layer and apply the filter to it, or take no action. |
| **Adding adjustment layer to selection** | In Pixel Persona, if you've created a selection, any adjustment applied to the selection can be added as a new adjustment layer or made a child adjustment layer in the current layer. |
| **Adding mask layer to selection** | Analogous to 'Adding adjustment layer to selection' above, but for mask layers. |
| **Adding filter layer to selection** | Analogous to 'Adding adjustment layer to selection' above, but for filter layers. |

#### Linked Services options

| Name | Description |
| --- | --- |
| **Linked Services** | Use these options if you use multiple personal devices to edit documents that contain linked resources from cloud storage. See the [Linked Services](../14-placing-external-content/04-linked-services.md) topic. |

#### Photoshop Plugins options

| Name | Description |
| --- | --- |
| **Open Default Folder in Finder** | Gain direct access to the default folder which is searched for plugins. Plugins can be added to this folder for easy access from the **Filters** menu. |
| **Open Default Folder in Explorer** | Gain direct access to the default folder which is searched for plugins. Plugins can be added to this folder for easy access from the **Filters** menu. |
| **Add/Remove Plugin Search Folder** | Adds or removes a folder in which to search or access support files to make plugins accessible from the **Filters** menu. |
| **Add/Remove Plugin Support Folder** | Adds or removes folders that contain supporting files for plugins (for example directories containing executables or presets). |
| **Authorize Global** | Authorizes access to supporting plugin files across multiple users and further resolves compatibility issues. |

**macOS:** #### Software Updates

| Name | Description |
| --- | --- |
| **Check for updates** | Sets the frequency to which the app will check for any software updates. You can switch off update checking by selecting 'Never'. |

#### Miscellaneous options

| Name | Description |
| --- | --- |
| **Reset** | Your current Fills, Brushes, Object Styles, Text Styles, User Defaults and Fonts can be reset to factory defaults. Reset fonts updates the font cache to the current state of the system (from memory). |
| **Reset** | Your current Fills, Brushes, Object Styles, Text Styles and User Defaults can be reset to factory defaults. |

**To configure settings:**

- From the Affinity app menu, select **Settings**.

> **Note:** To navigate to particular preference options, use the arrow keys, pop-up menu or search facility at the top of the dialog.

> **Note:**
>
> **macOS:** Apple System Settings allow you to control elements of the Affinity user interface such as scrollbar behavior.

#### SEE ALSO:

- Object defaults
- [Color management](../12-color/04-color-management.md)
- [Customizing keyboard shortcuts](../31-workspace/04-customize/01-keyboard-shortcuts.md)
- [Using pen tablets](../35-extras/04-third-party-support/01-using-pen-tablets.md)
