# Color management

The color and tonal information in a digital document is stored as numbers. When we share these documents between devices, the device has to work out how to display the color. As not all devices can display the same color gamut it can lead to colors looking different on each device.

![Color Profiles](../../assets/shared/clr_profiles_before.png)
*Images without color profiles (or with unsupported color profiles) may not look the same across each device.*

To ensure that the color looks the same on each device, we use color profiles to tell the device how to display or render the color information.

![Color Profiles](../../assets/shared/clr_profiles_after.png)
*Images with the correct profile for a calibrated device should closely match.*

In Affinity Photo 2, an opened file's color profile is honored by default. You have the option to convert it to the current working color space. When placing images into an existing document, the image's embedded color profile will always be converted to the document's current working space.

On export, you can choose to embed the document's or a named color profile to ensure accurate color management. Alternatively, the exported file can be unprofiled by not embedding the document or named profile.

## Assigning color profiles

Affinity Photo 2 lets you choose global default color profiles, assign a color profile as you create a document, or at any point during your session.

> **Note:** Most commercial printers will accept sRGB as they'll be able to do their own profiling at the print stage to get the best results for your work.
>
> For the CMYK color model, it's best to consult your print partner for an appropriate CMYK color profile recommendation.

**To select default global color profiles:**

1. **macOS:** From **Affinity Photo 2>Settings** (or **>Preferences**) (Color option), select an RGB, CMYK, Grayscale or LAB color profile from the pop-up menus.
2. **Windows:** From **Edit>Settings** (Color option), select an RGB, CMYK, Grayscale or LAB color profile from the pop-up menus.
3. Choose a **Rendering Intent** option and check **Black Point compensation**.

> **Note:** The chosen profile will be used as the current working space and will be offered when creating new documents, or will be used if you choose to convert an opened file's color space (discarding its own color profile).

**To select a new document's color profile:**

- As you create a [new document](../03-get-started/03-create-new-documents.md), select an option from the **Color Profile** pop-up menu.

**To convert the color space of file to be opened to the current working space:**

- **macOS:** Prior to opening the file, from **Affinity Photo>Settings** (or **>Preferences**) (Color option), check the **Convert opened files to working space** option. The document's current color profile is displayed at the top left of your workspace.
- **Windows:** Prior to opening the file, from **Edit>Settings** (Color option), check the **Convert opened files to working space** option. The document's current color profile is displayed at the top left of your workspace.

Options exist to warn that a file's working space will be converted, or that an unprofiled file will be assigned the current working space's profile.

**To change your document's color profile at any time:**

1. From the **Document** menu, select **Convert Format / ICC Profile**.
2. Select a profile from the list in the dialog.
3. Click **Convert**.

**To embed a color profile on file export:**

1. With Export Persona active, choose your **Preset** in the Export Options panel.
2. (Optional) Select a different **ICC profile** from the pop-up menu. Otherwise, the document's color profile will be embedded.
3. Check **Embed ICC profile**.

> **Note:** You can also embed an ICC profile via **File>Export** (click **More** in the dialog).

## About soft proofing

Soft proofing simulates output as you edit and design with respect to the color profile and the paper medium you intend to print on.

In Affinity Photo 2, this can be done by applying a **Soft Proof** adjustment to your project. You can then preview how your output will appear, preventing any nasty surprises at print time.

Because soft proofing is applied as an adjustment you can apply multiple adjustments, and therefore produce soft proofs for multiple output devices.

As an example, if you want to create several different output types, you might want to start with a color profile on document creation with a wide gamut (e.g., Adobe RGB 1998), and then change the profile to match the output destination. However, color information may be thrown away if changing to a smaller color gamut—simply changing back to a profile with a wider gamut will not restore the additional color information. By applying a soft proof adjustment you prevent this, allowing you to work in a wider gamut until you are ready to change to your chosen output profile.

> **Preferences — Settings (or Preferences):** Related behaviors can be adjusted from [the app's settings](../37-settings-preferences/01-settings-preferences.md):
>
> - **Color>Color profiles**
> - **Color>Rendering intent**
> - **Color>Black point compensation**
> - **Color>Convert opened files to working space**

## Installing ICC color profiles

Affinity Photo 2 detects and can use ICC color profiles installed on your operating system when exporting files. No special steps have to be taken in the app to make profiles available for its use when exporting files; installed profiles are available from the ICC profile pop-up menu of the Export dialog.

Your operating system includes software to assign an installed profile to your printer.

**To install a color profile:**

**macOS:** - Place the .icc file in /Library/ColorSync/Profiles.

**Windows:**

1. Open the **Color Management** control panel.
2. Select the **All Profiles** tab.
3. Select **Add**.
4. Browse to the .icc file and select **Add**.

**To assign an installed color profile with your printer:**

**macOS:**

1. In Finder, select **Go>Utilities** and open ColorSync Utility.
2. Select the **Devices** tab.
3. Select the printer with which to associate the profile.
4. Select the profile from the pop-up menu next to **Current Profile**.

**Windows:**

1. Open the **Color Management** control panel.
2. Select the **Devices** tab.
3. Select the device with which to associate the profile.
4. Select **Use my settings for this device**.
5. Select **Add**, then the profile you want to use for this device, then **OK**.
6. (Optional) To make the profile the default for this device, select it and then **Set as Default Profile**.

#### SEE ALSO:

- [Create new documents](../03-get-started/03-create-new-documents.md)
- [Export Options panel](../28-export-persona/02-export-options-panel.md)
- [Export](../27-sharing/01-export.md)
- [Soft proof adjustment](../10-adjustments/04-other-adjustments/05-adjustment-softproof.md)
- [Color models](02-color-models.md)
