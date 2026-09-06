# Colour management

The colour and tonal information in a digital document is stored as numbers. When we share these documents between devices, the device has to work out how to display the colour. As not all devices can display the same colour gamut it can lead to colours looking different on each device.

![Colour profiles](../../assets/shared/clr_profiles_before.png)
*Documents without colour profiles (or with unsupported colour profiles) may not look the same across each device.*

To ensure that the colour looks the same on each device, we use colour profiles to tell the device how to display or render the colour information.

![Colour profiles](../../assets/shared/clr_profiles_after.png)
*Documents with the correct profile for a calibrated device should closely match.*

In Affinity Designer, an opened file's colour profile is honoured by default. You have the option to convert it to the current working colour space. When placing images into an existing document, the image's embedded colour profile will always be converted to the document's current working space.

On export, you can choose to embed the document's or a named colour profile to ensure accurate colour management. Alternatively, the exported file can be unprofiled by not embedding the document or named profile.

## Assigning colour profiles

Affinity Designer lets you choose global default colour profiles, assign a colour profile as you create a document, or at any point during your session.

> **Note:** Most commercial printers will accept sRGB as they'll be able to do their own profiling at the print stage to get the best results for your work.
>
>
> For the CMYK colour model, it's best to consult your print partner for an appropriate CMYK colour profile recommendation.

**To select default global colour profiles:**

- From **Affinity Designer>Settings** (or **>Preferences**) (Colour option), select an RGB, CMYK, Greyscale or LAB colour profile from the pop-up menus.
- From **Edit>Settings** (Colour option), select an RGB, CMYK, Greyscale or LAB colour profile from the pop-up menus.
- Choose a **Rendering intent** option and check **Black Point compensation**.

> **Note:** The chosen profile will be used as the current working space and will be offered when creating new documents, or will be used if you choose to convert an opened file's colour space (discarding its own colour profile).

**To select a new document's colour profile:**

- As you create a [new document](../03-get-started/02-create-new-documents.md), select an option from the **Colour Profile** pop-up menu.

**To convert the colour space of file to be opened to the current working space:**

- Prior to opening the file, from **Affinity Designer>Settings** (or **>Preferences**) (Colour option), check the **Convert opened files to working space** option.
- Prior to opening the file, from **Edit>Settings** (Colour option), check the **Convert opened files to working space** option.

Options exist to warn that a file's working space will be converted, or that an unprofiled file will be assigned the current working space's profile.

**![Move Tool](../../assets/shared/ui/move_tool.png)

 To change your document's colour profile at any time:**

1. From the **File** menu, select **Document Setup**.
2. From the dialog:
   - Select the **Colour** tab.
  - From the **Colour Profile** pop-up menu, select a profile.
  - Select **Assign** or **Convert**.

    **Assign** adopts the new profile but leaves the values of the colours/pixels as is. **Convert** converts each colour from the old profile to the new one—colour/pixel values may change as a result.
  - Click **OK**.

> **Note:** Common colour profiles used in design include sRGB IEC61966-2.1 and Adobe RGB 1998, the former for on-screen display.

**To embed a colour profile on file export:**

1. With Export Persona active, choose your **Preset** in the Export Options panel.
2. (Optional) Select a different **ICC profile** from the pop-up menu. Otherwise, the document's colour profile will be embedded.
3. Check **Embed ICC profile**.

> **Note:** You can also embed an ICC profile via **File>Export** (click **More>** in the dialog).

## About soft proofing

Soft proofing simulates output as you design with respect to the colour profile and the paper medium you intend to print on.

In Affinity Designer, this can be done by applying a **Soft Proof** adjustment to your design. You can then preview how your output will appear, preventing any nasty surprises at print time.

Because soft proofing is applied as an adjustment you can apply multiple adjustments, and therefore produce soft proofs for multiple output devices.

As an example, if you want to create several different output types, you might want to start with a colour profile on document creation with a wide gamut (e.g., Adobe RGB 1998), and then change the profile to match the output destination. However, colour information may be thrown away if changing to a smaller colour gamut—simply changing back to a profile with a wider gamut will not restore the additional colour information. By applying a soft proof adjustment you prevent this, allowing you to work in a wider gamut until you are ready to change to your chosen output profile.

## Installing ICC colour profiles

Affinity Designer detects and can use ICC colour profiles installed on your operating system when exporting files. No special steps have to be taken in the app to make profiles available for its use when exporting files; installed profiles are available from the ICC profile pop-up menu of the Export dialog.

Your operating system includes software to assign an installed profile to your printer.

**To install a colour profile:**

- Place the .icc file in /Library/ColorSync/Profiles.

1. Open the **Colour Management** control panel.
2. Select the **All Profiles** tab.
3. Select **Add**.
4. Browse to the .icc file and select **Add**.

**To assign an installed colour profile with your printer:**

1. In Finder, select **Go>Utilities** and open ColorSync Utility.
2. Select the **Devices** tab.
3. Select the printer with which to associate the profile.
4. Select the profile from the pop-up menu next to **Current Profile**.

1. Open the **Colour Management** control panel.
2. Select the **Devices** tab.
3. Select the device with which to associate the profile.
4. Select **Use my settings for this device**.
5. Select **Add**, then the profile you want to use for this device, then **OK**.
6. (Optional) To make the profile the default for this device, select it and then **Set as Default Profile**.

#### SEE ALSO:

- [Create new documents](../03-get-started/02-create-new-documents.md)
- [Export Options panel](../15-exporting/02-export-options-panel.md)
- [Export](../14-saving-and-sharing/03-export.md)
- [Soft proof adjustment](../19-adjustments/19-soft-proof-adjustment.md)
- [Colour models](02-colour-models.md)
