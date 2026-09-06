# Working with SVGs

SVGs, or Scalable Vector Graphics, are a versatile type of vector file that can be easily adapted and optimised for use on the web and with cutting machines.

## About SVGs

SVGs are an XML-based vector graphic format used to display images. The difference between the SVG file format and other image formats, such as PNG or JPEG, is that SVG code can be easily read and manipulated via CSS and Javascript, allowing a web browser or program to create the graphic instead of just displaying it. Because SVGs are vector based this makes them very flexible, allowing you to manipulate the graphic in ways that can't be done with other image formats.

> **Note:** Despite SVGs being a predominately vector based format, raster objects within files will still degrade on resize.

### Using SVGs for web design

SVGs are generally considered the best file format for putting illustrations, icons and logos on the web. Because SVGs are so flexible, they can be resized without losing any quality, looking crisp at all resolutions. This flexibility also allows you to keep the file sizes small and allows for easy editing to optimise your graphics for different web layouts.

> **Note:** Despite SVGs being a predominately vector based format, raster objects within files will still degrade on resize.

### Using SVGs with cutting machines

SVGs are the preferred file type for use with cutting machines such as Cricut, Silhouette, Eclips, Brother, and Cameo. This is for a number of reasons:

- They contain directional information (or paths) that help guide the cutting machine in the right direction when cutting out the image.
- The lines in SVG files are very precise, and will not lose quality even if you completely resize them.
- SVGs can be easily edited from the cutting program itself.

**To prepare an SVG file for export to the web:**

- Ensure the design is sitting in an area of whole pixels (e.g., no decimal points) to keep the image crisp.
- The SVG export settings may automatically alter the DPI of the file to ensure a reasonable file size. For a file that is to be viewed on a retina screen, a DPI of 144 or higher is preferred.
- Ensure **Export text as curves for font independence** is checked to ensure your file is displayed precisely as intended.

**To prepare an SVG file for export to a cutting program:**

- Ensure your document is set to 72 DPI.
- Your cutting machine's application may push all layers within your document to the edge of the material when cutting to prevent material wastage. To add padding around the edges of your document, create a new rectangle layer underneath your curve layers.
- Your cutting machine's application may take all layers within your document and reorder them before cutting to prevent material wastage. If your design contains multiple curve layers but you want to retain the layout of your document, you will need to merge all of the separate curve layers into a single curve layer. You can do this by selecting each of the curve layers and going to **Layer>Geometry>Merge Curves**.
- We advise that you export to SVG using the default settings.

#### SEE ALSO:

- [Export](03-export.md)
