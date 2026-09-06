# Color management

The color and tonal information in a digital document is stored as numbers. When we share these documents between devices, the device has to work out how to display the color. As not all devices can display the same color gamut it can lead to colors looking different on each device.

![Color profiles](../../assets/shared/clr_profiles_before.png)
*Documents without color profiles (or with unsupported color profiles) may not look the same across each device.*

To ensure that the color looks the same on each device, we use color profiles to tell the device how to display or render the color information.

![Color profiles](../../assets/shared/clr_profiles_after.png)
*Documents with the correct profile for a calibrated device should closely match.*

In Affinity Publisher, an opened file's color profile is honored by default. You have the option to convert it to the current working color space. When placing images into an existing document, the image's embedded color profile will always be converted to the document's current working space.

On export, you can choose to embed the document's or a named color profile to ensure accurate color management. Alternatively, the exported file can be unprofiled by not embedding the document or named profile.

## Assigning color profiles

Affinity Publisher lets you choose global default color profiles, assign a color profile as you create a document, or at any point during your session.

> **Note:** Most commercial printers will accept sRGB as they'll be able to do their own profiling at the print stage to get the best results for your work.
>
> For the CMYK color model, it's best to consult your print partner for an appropriate CMYK color profile recommendation.

**To select default global color profiles:**

- From **Affinity Publisher>Settings** (or **>Preferences**) (Color option), select an RGB, CMYK, Grayscale or Lab color profile from the pop-up menus.
- Choose a **Rendering intent** option and check **Black Point compensation**.

> **Note:** The chosen profile will be used as the current working space and will be offered when creating new documents, or will be used if you choose to convert an opened file's color space (discarding its own color profile).

**To select a new document's color profile:**

- As you create a [new document](../04-get-started/01-create-new-documents.md), select an option from the **Color Profile** pop-up menu.

**To convert the color space of file to be opened to the current working space:**

- **macOS:** Prior to opening the file, from **Affinity Publisher>Settings** (or **>Preferences**) (Color option), check the **Convert opened files to working space** option.
- **Windows:** Prior to opening the file, from **Edit>Settings** (Color option), check the **Convert opened files to working space** option.

Options exist to warn that a file's working space will be converted, or that an unprofiled file will be assigned the current working space's profile.

**To change your document's color profile at any time:**

1. From the **File** menu, select **Document Setup**.
2. From the dialog:
  - Select the **Color** tab.
  - From the **Color Profile** pop-up menu, select a profile.
  - Select **Assign** or **Convert**.  
 **Assign** adopts the new profile but leaves the values of the colors/pixels as is. **Convert** converts each color from the old profile to the new one—color/pixel values may change as a result.
  - Click **OK**.

> **Note:** Common color profiles used in design include sRGB IEC61966-2.1 and Adobe RGB 1998, the former for on-screen display.

**To embed a color profile on file export:**

1. On the **File** menu, select **Export**.
2. (Optional) Under the **Advanced** section in the dialog, select a different **ICC profile** from the pop-up menu. Otherwise, the document's color profile will be embedded.
3. Check **Embed ICC profile**.

> **Note:** By default, exported files will have their color profiles embedded within them, although you have the option to make the image unprofiled during export.

## About soft proofing

Soft proofing simulates output as you design with respect to the color profile and the paper medium you intend to print on.

In Affinity Publisher, this can be done by applying a **Soft Proof** adjustment to your project. You can then preview how your output will appear, preventing any nasty surprises at print time.

Because soft proofing is applied as an adjustment you can apply multiple adjustments, and therefore produce soft proofs for multiple output devices.

As an example, if you want to create several different output types, you might want to start with a color profile on document creation with a wide gamut (e.g., Adobe RGB 1998), and then change the profile to match the output destination. However, color information may be thrown away if changing to a smaller color gamut—simply changing back to a profile with a wider gamut will not restore the additional color information. By applying a soft proof adjustment you prevent this, allowing you to work in a wider gamut until you are ready to change to your chosen output profile.

> **Preferences — Settings:** Related behaviors can be adjusted from [the app's settings](../25-settings-preferences/01-settings-preferences.md):
>
> - **Color>RGB, 32 bit RGB, CMYK, Grayscale, LAB Color Profile (these set default profiles for new documents)**
> - **Color>Rendering intent**
> - **Color>Black point compensation**
> - **Color>Convert opened files to working space**

## Installing ICC color profiles

Affinity Publisher detects and can use ICC color profiles installed on your operating system when exporting files. No special steps have to be taken in the app to make profiles available for its use when exporting files; installed profiles are available from the ICC profile pop-up menu of the Export dialog.

Your operating system includes software to assign an installed profile to your printer.

**To install a color profile:**

**macOS:** - Place the .ICC file in /Library/ColorSync/Profiles.

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

- [Create new documents](../04-get-started/01-create-new-documents.md)
- [Export](../14-publishing-and-sharing/02-export-as-graphic.md)
- [Soft proof adjustment](../18-adjustments/19-soft-proof-adjustment.md)
- [Color models](02-color-models.md)
