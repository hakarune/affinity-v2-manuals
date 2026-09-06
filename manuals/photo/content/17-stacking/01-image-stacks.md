# Image stacks

Non-destructive image stacks blend together a series of images based on the same scene or almost identical subject matter. Visual differences between images in the series can then be removed, composited together, or used for creative effects.

## About image stacks

Use image stacks for:

- Exposure merging: Merging images of varying exposures.
- Object Removal: Use a series of images to blend out unwanted subject matter from a specific image in an image set.
- Noise reduction: Blend together multiple shots of the same subject and average out the noise.
- Creative effects: Simulate long exposure imagery and combine bright subjects (e.g., fireworks) for a composite effect.

## About stack modes

A choice of modes can be applied to your stack depending on what you want to achieve. Median can be used for most blending operations such as object removal, exposure merging (exposure blending) and noise reduction.

> **Note:** Stack modes include:
>
> - **Mean**—averages pixel content across the stack of images. Good for long exposure simulation and noise reduction.
> - **Median**—removes pixel content that is not consistent in each image. Suitable for object removal and noise reduction.
> - **Outlier**—exposes pixel content that differs in each image: great for sequence composites.
> - **Maximum**—uses the maximum pixel values from each image. Can be used for creative exposure blending where the subject is lighter than the background.
> - **Minimum**—uses the minimum pixel values from each image. Suitable for exposure blending where the subject is darker than the background.
> - **Range**—indicates areas that change across the image stack. Good for analyzing what has changed between each image.
> - **Mid-Range**—uses the middle pixel values from each image. Can be used to increase tonal range if used with bracketed exposures.
> - **Total**—produces the total value of pixels from each image. Usually results in overexposure, but can be used to lighten very underexposed imagery.
> - **Standard Deviation**—analytical: measures the distribution of information between the images. Useful for object removal as it clearly indicates areas that will be averaged out with a Median mode.
> - **Variance**—analytical: as Standard Deviation, indicates how pixel values are spread between images. More intense distributions are shown very clearly.
> - **Skewness**—analytical: highlights edge detail and indicates the intensity of pixel value distribution. Can be used to determine tonal and spatial differences between images.
> - **Kurtosis**—analytical: detects the peakedness of an image. A brighter result represents low noise levels and a tonal uniformity (most pixels at dominant gray level). Darker results represent greater noise and less tonal uniformity (more pixels further away from dominant gray level).
> - **Entropy**—analytical: represents the number of bits required to encode information in the stack. Could be used with stacked video frames (within the same scene or shot).

**To create a stack:**

1. From the **File** menu, select **New Stack**.
2. From the dialog, click **Add** to locate and select your images for blending. Click **Open** to add the images to the stack list.
3. (Optional) Uncheck **Automatically Align Images** to manually align images later in the **Layers** panel.
4. Choose a Perspective or Scaling operation from the menu to allow for successful auto-alignment. The former applies a perspective adjustment to each image; the latter repositions and/or sizes the image layer.
5. Check **Live Alignment** to add a live perspective filter to each pixel layer in the stack; this allows the perspective of any layer to be adjusted after stacking without affecting its pixel layer (this may affect performance depending on size and number of images to be stacked). Select the layer's perspective filter layer and adjust corner handles on the page.
6. Click **OK**.

Your images are blended and presented in a Live Stack Group in the **Layers** panel. You can manually align layers if auto-alignment isn't 100% accurate.

> **Note:** Live stacking is designed to work with tens of images, not hundreds. We recommend against attempting to create live stacks with hundreds of images.

> **Note:** Once stacked, you may notice 'checkerboard' transparency at the very edge of your stack group. This is an intentional result of auto-alignment and can be either cropped away or, if you're merging the stack image layers together, inpainted out instead.

**To change stack mode:**

1. On the **Layers** panel, click the Stack mode icon on the Live Stack Group. The default mode is Median as indicated by the icon.
2. From the pop-up menu, select a stack mode suited to the type of photos you are stacking (see above). The icon will change depending on the mode selected.

> **Note:** Once you've applied a stack mode, the image layers in the stack shouldn't require manipulation (of opacity, blend modes, blend ranges, etc.) except for possible re-alignment (if auto-adjustment was not satisfactory). However, depending on image content you may need to apply additional adjustments to the stack or mask some areas for best results.

#### SEE ALSO:

- [Object removal using stacks](03-object-removal-using-stacks.md)
- [Exposure merging using stacks](02-exposure-merging-using-stacks.md)
- [Noise reduction using stacks](04-noise-reduction-using-stacks.md)
- [Creative effects using stacks](05-creative-effects-using-stacks.md)
- [About astrophotography stacking](../18-astrophotography-stack-persona/01-about-astrophotography-stacking.md)
