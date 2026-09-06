# Supported file formats

Affinity Photo 2 is capable of opening many raster and vector file formats. Photo also imports PDF and Adobe PSD files, and exports a range of raster file formats and the PSD file format.

| File type | Open/Import | Export |
| --- | --- | --- |
| Adobe Illustrator (AI) | ![check](../../assets/shared/check.png)<sup>1</sup> |  |
| Adobe Freehand (10 and MX) | ![check](../../assets/shared/check.png)<sup>2</sup> |  |
| Adobe Photoshop (PSD) | ![check](../../assets/shared/check.png)<sup>3</sup> | ![check](../../assets/shared/check.png)<sup>10</sup> |
| Adobe Photoshop (PSB) | ![check](../../assets/shared/check.png) |  |
| DNG | ![check](../../assets/shared/check.png)<sup>9</sup> |  |
| EPS | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| GIF | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| HEIF/HEIC/HIF | ![check](../../assets/shared/check.png)<sup>4</sup> |  |
| JPEG | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| J2K,JP2 | ![check](../../assets/shared/check.png) |  |
| JPEG-XR/JXR (WDP/HDP) | ![check](../../assets/shared/check.png)<sup>11</sup> |  |
| JPEG-XL | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| PDF | ![check](../../assets/shared/check.png)<sup>1,8</sup> | ![check](../../assets/shared/check.png)<sup>10</sup> |
| PNG | ![check](../../assets/shared/check.png)<sup>13</sup> | ![check](../../assets/shared/check.png)<sup>5,</sup><sup>13</sup> |
| RAW | ![check](../../assets/shared/check.png)<sup>6</sup> |  |
| SVG | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| TGA | ![check](../../assets/shared/check.png)<sup>5</sup> | ![check](../../assets/shared/check.png) |
| TIFF | ![check](../../assets/shared/check.png)<sup>7</sup> | ![check](../../assets/shared/check.png)<sup>5</sup> |
| WEBP | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| OpenEXR | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| Radiance HDR | ![check](../../assets/shared/check.png) | ![check](../../assets/shared/check.png) |
| FITS | ![check](../../assets/shared/check.png)<sup>12</sup> |  |

<sup>1</sup> Files with multiple artboards (AI) or pages (PDF) can be imported; each artboard/page will be kept as a distinct page on its own layer.

<sup>2</sup> Multi-page Freehand files open with each page concatenated onto a single page. Add file extension .fh10 or .fh11 to import. Text import is not supported.

<sup>3</sup> Includes Smart Objects, loaded as editable [embedded documents](../14-placing-external-content/02-placing-content.md).

<sup>4</sup> For iPhone images, the HEIC file may include an upsampled depth map, loaded as an editable second layer. For Canon EOS models (1 DX MkIII, R5 and R6), HIF files (HDR 10-bit PQ-encoded) can be opened.

<sup>5</sup> Supports transparency.

<sup>6</sup> For a comprehensive up-to-date list of RAW file support, please see the following links:

- [SerifLabs RAW](https://affin.co/rawlist) (Mac & Windows)
- [Apple Core Image RAW](https://affin.co/rawapple) (Mac only)

<sup>7</sup> 12 bit TIFF (RGB or Grayscale) included, plus legacy TIFF files exported from Photoshop with CICP data embedded in an ICC profile.

<sup>8</sup> JBIG2 PDF encoding is supported.

<sup>9</sup> Apple ProRAW DNG support (from Apple iPhone12 Pro) is supported.

<sup>10</sup> Text will be rasterized on export.

<sup>11</sup> Includes JPEG-XR 101010 (e.g. XBOX screen captures).

<sup>12</sup> Flexible Image Transport System files commonly used in astrophotography, with a .fit or .fts file extension.

<sup>13</sup> Includes 32-bit HDR support ([PNG specification - Third edition](https://www.w3.org/TR/png-3/)) for interchanging HDR broadcast imagery in a lossless format. Legacy PNG files exported from Photoshop with CICP data embedded in an ICC profile can be imported.

#### SEE ALSO:

- [Open documents](../03-get-started/01-open-documents-and-images.md)
- [Importing PDF documents](01-supported-file-formats/02-importpdf.md)
- [Importing Adobe documents](01-supported-file-formats/01-importadobe.md)
- [Placing content](../14-placing-external-content/02-placing-content.md)
- [Export](../27-sharing/01-export.md)
