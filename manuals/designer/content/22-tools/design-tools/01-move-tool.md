# ![Move Tool](../../../assets/shared/ui/move_tool.png)

 Move Tool

The **Move Tool** allows you to select objects on your page. Once selected, the Move Tool allows you to move, rotate, and resize your selected object, as well as change its properties.

> **Note:** Use the `Shift`  with the tool to constrain objects to Vertical, Horizontal or diagonal (45°).

> **Tip:** Tool shortcut : `V`.

### Settings

The following settings are available on the context toolbar when **no objects** are selected:

- **Auto-select**—controls the automatic selection behaviour:
   - **On (default)**—objects and groups can be selected on the page or Layers panel.
  - **Off**—objects and groups can be selected from the Layers panel only.
  - **Objects**—only objects can be selected on the page, while grouped items will be selected as if ungrouped; both groups and layers can be selected from Layers panel.
  - **Groups**—only groups can be selected on the page; both groups and layers can be selected from Layers panel.
- **Document Setup**—displays a pop-up panel for adjusting document settings.
- **Settings** (or **Preferences**)—provides access to the Preferences dialog for advanced application settings.

The following settings are available on the context toolbar when **individual objects** are selected (other settings are shown conditional on the type of object selected):

- **Fill**—click the colour swatch to display a pop-up panel to update fill colour.
- **Stroke**—click the colour swatch to display a pop-up panel to update stroke colour.
- **Stroke properties**—set the stroke style, width, joins, cap ends, order and arrowhead settings via a pop-up panel.
- Line style—click to display a pop-up panel to set the **Width** and line style.
- **Lock Children**—when checked, any child object(s) of a selected ungrouped object cannot be altered when the selected object is transformed. Great for maintaining the size, position and aspect ratio of a clipped picture when resizing its parent object.
- **Group**—converts selected objects into a group for easier selection and modification.*
- **Ungroup**—splits selected group into individual objects for focussed manipulation.*
- ![Enable Transform Origin](../../../assets/shared/ui/rotationcntr.png)

   **Enable Transform Origin**—displays a movable transform origin about which the object can be rotated.
- ![Hide Selection](../../../assets/shared/ui/hide_selection_while_dragging.png)

   **Hide Selection while Dragging**—when selected, the object's selection box is temporarily hidden when transforming the object. If this option is off, the selection box remains visible during transformation. The selected behaviour persists across all objects unless it is manually switched.
- ![Show Alignment Handles](../../../assets/shared/ui/alignment_mode.png)

   **Show Alignment Handles**—when selected, displays alignment handles at the centre and edges of the selected object. Hovering over these handles displays a floating guideline across the page. You can drag the handles to position the centre or edges of the selected object in line with this guide.
- ![Transform Objects Separately](../../../assets/shared/ui/multiple_transform.png)

   **Transform Objects Separately**—when selected, where multiple objects are selected, they can be be resized, rotated and sheared independently of each other instead of transforming the bounding box.
- ![Convert to Curves](../../../assets/shared/ui/converttocurves.png)

   **Convert to Curves**—converts the selected object into a series of connected lines and nodes.
- **Align Horizontal**—align objects according to **Left** or **Right** edges, or by **Centre**. Single objects align in relation to page edge.
- **Align Vertical**—align objects according to **Top** or **Bottom** edges, or by **Middle**. Single objects align in relation to page edge.

> **Note:** *Nested groups can be created when an existing group is part of a selection being grouped. If these nested groups are ungrouped, the previously grouped objects remain within their original group. To split a nested group into individual objects (removing all previous groups), from the **Layer** menu, select **Ungroup All**.

The following settings are available on the context toolbar when a placed image or document is selected:

- Image/document information—Displays the image's or document's native dimensions and its placed DPI and percentage scaling; use the drop-down arrow to edit DPI or scaling, or reset to original size (100% scaling).
- **PageBox**—choose from the following:
   - **TrimBox**—the page displayed to the page edge.
  - **BleedBox**—the page with bleed or printer marks shown.
  - **Minimum Content**—the bounding box of the object(s) in the document.
  - **Minimum Visible Content**—As for Minimum Content but the bounds of any hidden objects are also taken into account.
  - **Maximum Content**—the bounding box of the object(s) including the object's control handles outside the box.
  - **Maximum Visible Content**—As for Maximum Content but the bounds of any hidden objects are also taken into account.
- **Artboard**—select an artboard to display (Designer document).
- **Spread**—select a spread to display (PDF or Publisher document).
- **Edit Image**/**Edit Document**—click to open a separate window from which you can edit your placed (or framed) image or document.
- **Replace Image**/**Replace Document**—click to display a pop-up panel from which you can select a file to replace the current placed (or framed) image or document.

> **Note:** Under **Preferences>Tools**, the **Move Tool Aspect Constrain** option can be used to specify whether or not to constrain the aspect ratio by default when resizing. The option can also be set to automatic, letting the software decide based on the selected content.

#### SEE ALSO:

- [Selecting objects](../../08-object-control/01-selecting-objects.md)
- [Keyboard shortcuts for tools](../../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
