# Stroke panel

The **Stroke** panel lets you set the properties of lines and curves, as well as shape outlines and vector brush strokes.

## About the Stroke panel

Every object can take a stroke around its outline which can take on various properties, e.g. width, colour, opacity, line style, etc.

![Stroke panel](../../assets/images/panel_stroke.png)
*The Stroke panel showing properties applied to an object.*

The following controls are found on the panel:

- ![No Line Style](../../assets/shared/ui/No_Line_Style.png)

   ![Solid Line Style](../../assets/shared/ui/Solid_Line_Style.png)

   ![Dash Line Style](../../assets/shared/ui/Dash_Line_Style.png)

   ![Texture Line Style](../../assets/shared/ui/Texture_Line_Style.png)

   **Style**—select a line style button to change how the line is drawn. Choose from None, Solid Line Style, Dash Line Style, and Texture Line Style, respectively. The last option applies the currently selected brush in the Brushes panel to the stroke.
- **Width**—drag to change the width (thickness) of the selected line or enter absolute values, expressions and formulas (percentages).
- ![Round Cap](../../assets/shared/ui/Round_Cap.png)

   ![Butt Cap](../../assets/shared/ui/Butt_Cap.png)

   ![Square Cap](../../assets/shared/ui/Square_Cap.png)

   **Cap**—select one of the cap style buttons (Round, Butt, or Square) to vary the contour of the line end.
- ![Round Join](../../assets/shared/ui/Round_Join.png)

   ![Bevel Join](../../assets/shared/ui/Bevel_Join.png)

   ![Mitre Join](../../assets/shared/ui/Mitre_Join.png)

   **Join**—select a setting (Round, Bevel, or Mitre) to determine the contour of sharp corners on the stroke. With **Mitre** joins, the **Mitre** setting dynamically controls if bevelling occurs by extending each line at the junction by the number of line widths. If the two outer edges meet within that limit, the result is a sharp corner; if not, you’ll get a flat (Bevel) corner.
- **Mitre**—sets the length of the extension of Mitre joins to create either sharp or flat corners.
- ![Align Stroke Centre](../../assets/shared/ui/Align_Stroke_Centre.png)

   ![Align Stroke Inside](../../assets/shared/ui/Align_Stroke_Inside.png)

   ![Align Stroke Outside](../../assets/shared/ui/Align_Stroke_Outside.png)

   **Align**—select one of the align buttons to control where the stroke is placed in relation to the object edge, i.e. centered, or on its inside or outside.
- ![Draw stroke behind](../../assets/shared/ui/line_draw_back.png)

   ![Draw stroke in front](../../assets/shared/ui/line_draw_front.png)

   **Order**—select one of the order buttons to control where the stroke is placed in relation to the object. **Draw stroke behind** hides the inner half of the object's outline behind a closed shape—useful with very small objects or when shrinking outlined text. **Draw stroke in front** always reveals the whole line.
- **Scale with Object**—check to scale both line and shape together when resizing a closed shape. Uncheck to keep line width constant.
- **Start**/**End**—select an arrowhead style for the start/end stops of the stroke from the pop-up menu.
- **Percentage**—with styles selected, you can enter a percentage to adjust the size of your selected arrowheads in proportion with the stroke width.
- ![Arrowhead Inside](../../assets/shared/ui/arrowhead_inside.png)
- ![link](../../assets/shared/ui/chainlinkconnected.png)
- ![Arrowhead Swap](../../assets/shared/ui/arrowhead_swap.png)
- ![Arrowhead reset](../../assets/shared/ui/Reset_preset.png)
- **Properties**—click to edit the brush used as your Texture Line Style via a Brush dialog.
- **Pressure**—displays your current pressure profile after applying a line or brush stroke. Clicking the profile lets you edit the profile and save it for future use.
- **Dash**—when Dash Line Style is selected, the three 'Dash - Gap' pairings displayed will allow you to set the design of the dot or dash. To configure you can input values directly or drag across individual dash (white) or gap (black) strips under the number sequence. (See [Draw curves and shapes](../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md).)

  ![Dash pattern control](../../assets/shared/strokepanel_dashpattern.png)
- **Phase**—when Dash Line Style is selected, this option allows you to manually offset the starting point of the dash design if **Balanced Dash Pattern** is disabled.
- ![Balanced Dash Pattern](../../assets/shared/ui/balanced_dash.png)

> **Note:** To change the line colour, use the Colour or Swatches panel.

> **Preferences:** ### Settings
>
>
> Related behaviours can be adjusted from [the app's settings](../27-settings-preferences/01-settings-preferences.md):
>
>
> - **Miscellaneous>Reset Brushes**
> - **User Interface>Show brush previews**
> - **User Interface>Always show brush crosshair**

#### SEE ALSO:

- [Draw curves and shapes](../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md)
- [Edit curves and shapes](../05-drawing-curves-and-shapes/03-edit-curves-and-shapes.md)
- [Colour panel](06-colour-panel.md)
- [Swatches panel](18-swatches-panel.md)
- [Expressions for field input](../28-expressions-for-field-input/01-expressions-for-field-input.md)
- [Customising the workspace](../21-workspace/customise/02-workspace.md)
