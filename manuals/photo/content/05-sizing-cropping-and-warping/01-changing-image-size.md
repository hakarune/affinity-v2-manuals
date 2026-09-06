# Changing image size

In Affinity Photo 2 there are options to change a document's or image's pixel dimensions and/or print resolution.

You can change the 'size' of an image by scaling or resampling it. These can be undertaken independently or simultaneously.

## Scaling

Scaling will embed a specific print resolution into an image's metadata to force it to print at a specific dpi (e.g. 300 dpi). The image's pixel dimensions remain unaffected.

## Resampling

Resampling will do one of the following:

- Increase the number of pixels in an image (i.e. stretch it) to make its overall pixel dimensions bigger. This is known as upsampling. This will also increase the image's file size.
- Decrease the number of pixels in an image (i.e. compress it) to make its overall pixel dimensions smaller. This is known as downsampling. This will also decrease the image's file size.

When you resample an image, you have the option to:

- Maintain the image's aspect ratio or resize unconstrained.
- Select from a variety of interpolation methods (see note below).
- Simultaneously scale your image.

Resampling may be carried out to:

- Enlarge an image to specific dimensions in preparation for printing.
- Reduce an image for on-screen display and to optimize file size.

**To scale an image:**

1. From the **Document** menu, select **Resize Document**.
2. Ensure the **Resample** option is switched off.
3. Change the **DPI** to control the number of pixels (dots) which will be printed per inch when your document is printed. Set higher values (e.g., 300dpi) for professional printing.
4. Click **Resize**.

You will see no change in the image on the page as this procedure only affects the image's metadata.

**To resample an image:**

1. From the **Document** menu, select **Resize Document**.
2. Ensure the **Resample** option is switched on.
3. Enter your new document dimensions in the **Size** boxes—left box for width, right box for height.
  - To resize the width and height independently, click the link icon (to unlink) between the **Size** boxes.
4. (Optional) Select a different measurement unit from the **Units** pop-up menu. Rulers will update to the new measurement unit.
5. Change the **DPI** to control the number of pixels (dots) which will be printed per inch when your document is printed. Set higher values (e.g., 300dpi) for professional printing.
6. Select a **Resample** method from the pop-up menu.
7. Click **Resize**.

> **Note — Resampling methods:** The following resample settings are available:
>
> - **Nearest Neighbor**—simple resampling which has the fastest processing time. Use for hard-edge images and pixel work.
> - **Bilinear**—algorithmic resampling for use when downsampling images.
> - **Bicubic**—algorithmic resampling for use when upsampling images. Resampling is smoother than Bilinear but has a slower processing time.
> - **Lanczos 3**—complex algorithmic resampling that offers sharp results but with the longest processing time. Available as 'separable' and 'non-separable'; the latter gives marginally better results, but is slightly slower than 'separable'.

> **Tip:** Instead of adding absolute input values you can enter expressions instead. See [Expressions for field input](../38-expressions-for-field-input/01-expressions-for-field-input.md) for details.

#### SEE ALSO:

- [Image and canvas size](03-changing-canvas-size.md)
- [Creating new documents](../03-get-started/03-create-new-documents.md)
