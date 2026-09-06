# Features of Affinity Photo 2

Here's an overview of the features of Affinity Photo 2. Choose a category from the menu below, which includes options to view all features, or only those that are new in this version—marked with a red bullet (▪).

## New in V2.6

- [Machine Learning (ML)](../35-extras/01-affinity-and-machine-learning-ml.md) selections:
  - [Object Selection Tool](../32-tools/03-selection-tools/01-object-selection-tool.md)
    - Intelligent object selections
    - Select multi-part components
    - Optional control over soft edges and matting
    - Works on image and RAW layers
  - [Select Subject](../08-selections/05-select-subject-ml.md)
    - Automatic selection of the main subject on raster or image layers
    - Record as a macro for faster workflows
    - Works on image and Raw layers
- Search within current [Brushes Panel](../33-panels/05-brushes-panel.md) category
- Load image layer in Develop, Liquify and Tone Mapping Personas as raster layer<sup>*</sup>
- Image/Raw layer improvements:
  - Merge Down/Selected will rasterize and merge
  - Inpainting will rasterize and apply<sup>*</sup>
  - Paint Brush and Erase tools, on painting, will nest the new layer or mask, respectively
  - Deleting pixel selections will rasterize or mask content<sup>*</sup>
  - Duplicating pixel selections will create masked or rasterized pixel content from just that copied area<sup>*</sup>
  - Moving marquee pixel selections with `Cmd`-drag will rasterize the layer and move just that content
- Live Perspective filter shortcut of `Cmd`+T
- Flood Select, Marquee and Freehand selection tool improvements:
  - Tools now use `Shift` to add; `Alt` to subtract
  - Antialiasing enabled by default
- [Rectangular Marquee Tool](../32-tools/03-selection-tools/04-marquee-selection-tools.md) can be drawn from center
- Marquee tools use the `Cmd` modifier to constrain<sup>*</sup>
- [Color panel](../33-panels/08-color-panel.md)’s Color Picker automatically colors selected object(s)
- Toggle marquee select intersection behavior with `Cmd` key
- Right-click [Layers Panel](../33-panels/13-layers-panel.md) options for Clear Mask and Fill Mask
- [Inpainting](../09-retouching/05-inpainting.md) and [Patch](../09-retouching/06-patching.md) tools remember previously chosen target layer
- Updated [SerifLabs RAW engine](https://affin.co/rawlist), including support for:
  - Canon EOS R5 Mark II
  - Fujifilm GFX 100S II
  - Google Pixel 9 Pro/Pro XL/Pro Fold
  - Leica D-LUX8
  - Leica Q3 43
  - Nikon Z 6 III
  - Panasonic DC-GH7
  - Sony ZV-E10 II

<sup>*</sup>Optional behaviors via Assistant/Settings

## Power, performance and compatibility

- Optimized for:
  - **macOS:** Grand Central Dispatch (GCD)
  - **macOS:** OpenGL
  - **macOS:** Core Graphics
  - **Windows:** Direct3D
  - 64-bit engine
  - **macOS:** GPU hardware acceleration (Metal) for integrated, discrete and external GPUs
  - **Windows:** Hardware GPU acceleration (OpenCL) for integrated, discrete and external GPUs
- Display support
  - **macOS:** Regular, Retina and expanded gamut DCI-P3
  - **Windows:** Wide color gamut (Display P3)
  - HiDPI
  - **macOS:** EDR
  - **Windows:** HDR (Windows; >400 nits recommended)
- Create massive gigapixel-sized documents
- 16-bits per channel editing
- Sub-pixel accuracy
- **macOS:** Mac with Apple M1/M2/M3 chip or Intel processor
- **macOS:** macOS Catalina 10.15 or later
- 64-bit plug-in support
- Photoshop plugin support
- DxO Nik Collection plugin support (all versions)
- Embedded Photoshop PSD Smart Objects retain editability
- Up-to-date Tablet support
- Multi-touch support
- **Windows:** Surface Studio with Surface Pen and Surface Dial support
- **macOS:** Force Touch support (Magic Trackpad 2/MacBook/MacBook Pro)
- **macOS:** Touch Bar support (MacBook Pro)
- End-to-end EXIF preservation
- Benchmark testing
- **Windows:** Windows® 11, Windows® 10 May 2020 Update (2004, 20H1, build 19041) or later

## Raw development

- Choice of SerifLabs or Apple Core Image RAW engines (SerifLabs for Windows only)
- GPU-accelerated Raw development
- Remove automatic tone curve and apply your own
- Automatic (and manual) lens correction and noise reduction
- Develop Assistant settings for setting default tone, lens correction, noise reduction, and exposure control behavior
- Adobe Lens Correction Profile (LCP) support
- ACM lens profile support
- Dedicated tones, lens, noise reduction and sharpening panels
- Support for the latest cameras
- Split view with syncing
- Solid and gradient overlays for restricting adjustments
- Show clipped highlights, shadows, and tones (in output color space)
- Hot pixel removal (SerifLabs RAW Engine only)

## Professional color support

- CMYK, Lab, Grayscale and RGB color modes
- Color panel (RGB, HSL, LAB, CMYK, Grayscale)
- Swatches panel for pre-supplied and custom color palettes
- Generate palette from image
- Global colors
- Color tints
- Color Picker Tool (color mode aware, pick from anywhere on screen, color averaging, layer selection)
- Color Replacement Brush
- Paint Mixer Brush
- Gradient Tool (Linear, Elliptical, Radial, Conical, Bitmap)
- Professional color support
- Spot colors and overprint
- PANTONE® color support
- ICC color profiling
- Import Adobe Swatch Exchange (ASE) color palettes (including spot colors)
- Drag-and-drop colors from Chroma app (SoftPress)

## Solid photo-editing power

- Sizing and transforming:
  - Resize images and canvas
  - Crop to original/custom ratios, absolute dimensions or print sizes
  - Straighten photos
  - Mesh Warp Tool
  - Non-destructive perspective filter
  - Liquify tools in dedicated Persona workspace
  - Pixel art resizing
- Channels:
  - View and isolate color channels
  - Work on channels for document, layer, adjustment, filter, selection or mask
  - Save pixel selections as spare channels
  - Isolate and edit spare channels as layers
  - Duplicate spare channel for backup
- HDR/32-bit
  - Merge bracketed exposures together to create 32-bit images
  - Unique Persona for Advanced Tone Mapping
  - Edit effortlessly in 32-bit unbounded color format
  - Maintain a true 32-bit lossless workflow and preview full tonal range
  - Multichannel OpenEXR and Radiance import and export
  - Full OpenColorIO Integration
  - Color managed workflow: choose between display transform, linear light and OpenColorIO transforms
  - HDR and EDR display support (for 32-bit unbounded HDR documents)
- Powerful auto-stitched panoramas
- Live projections (equirectangular and perspective)
- Stacking
  - For noise reduction
  - For exposure merging
  - For moving object removal
  - Auto-alignment
  - Non-destructive behavior
- Focus merging with source cloning
- Astrophotography
  - Dedicated Persona for stacking
  - Raw and FITS image support
  - Stack light and calibration frames (dark/dark flat/flat/bias)
  - Stack, tone stretch and retouch entirely in 32-bit
  - Create full color, composite (HaRGB, SHO), grayscale or false color images
  - Stack images for different filters simultaneously using file groups (auto-alignment avoids resampling)
  - Support for FUJIFILM X-Trans sensor images
- Selection tools
  - Shaped selections
  - Intelligent Selection Brush Tool
  - Freehand Selection Tool with Polygonal and Magnetic modes
  - Refine selections to capture fine detail
  - Flood selection
  - Store and save selections
  - Quick masks
- Comprehensive metadata editing
- Assets for storing layer content

## Powerful layer management:

- Drag-and-drop layers
- Non-destructive adjustment layers with clipping previews
- Shareable LUTs
- Non-destructive live filter layers with 'live' before/after split views
- Non-destructive Live Liquify filter layers
- Apply adjustments, filters and blend modes at the stack, layer, group, selection or object level
- Fill layers
- Linking layers
- Pattern layers
- High-quality layer effects
- Clipping within layers
- Blend modes
- Blend ranges (linear and non-linear) and blend gamma control
- Per-object hierarchical antialiasing
- Lock child layer positions
- Layer masks (brush-based and gradient)
- Colored layer entry tagging for easy identification
- Image control:
  - Place images on dedicated layers
  - Resampling: Nearest Neighbor, Bilinear, Bicubic and Lanczos 3 pixel scaling

## External resource management

- Linked resources
- Embedded/linked resource policy on new document creation
- Resource Manager
- Collect linked resources

## Brushes

- Painting:
  - High-quality brush galleries
  - Change brush size, hardness, and opacity on the fly
  - Undo Brush with 'paintback' to saved snapshot
  - Import/export brushes, including ABR file import
  - Custom brushes (including image-based brushes)
  - Create brushes from any pixel selection on pixel or mask layer
  - Assign tools to brushes selectively
  - Optimized for graphics tablets
  - Multi-controller support including pressure and velocity
  - Controller-specific brush dynamics
  - Customizable controller ramps
  - Wet Edges support with customizable ramps
  - Sub-brushes (combined brushes)
  - Brush symmetry and mirroring
  - Choice of brush and nozzle controllers/ramps
  - Stroke stabilization for smooth strokes
  - Nozzle rotation using left and right arrow keys
- Retouching
  - Retouching tools
    - Red-eye removal
    - Inpainting for object removal
    - Clone Brush/Healing Brush
    - Blemish Removal/Patching
  - Retouching brushes:
    - Dodge, Burn and Sponge brushes
    - Blur, Sharpen, Median and Smudge brushes
  - Frequency separation

## Macros and batch processing

- Record and save actions as macros
- Edit individual recorded steps and their parameters
- Customize macro settings post recording
- Import, export, and maintain a macro library
- Run batch jobs for bulk processing and conversion of images
- Apply macros in batch jobs for a seamless custom workflow

## Supporting vector design tools and concepts

- Precise Pen Tool
- Intuitive Move Tool (moves, scales and transforms)
- Rotate from movable origin
- Customizable nudge distances
- Node Tool for fine tuning vectors
- Customizable geometric shapes
- Full range of non-destructive Boolean geometry operations
- Duplicate and transform objects with precision
- Add noise to fills and strokes as a solid or graduated attribute
- Customizable stroke styles
- Styles presets with import/export
- Artistic and frame text
- Text on a path
- Character and Paragraph panels
- Advanced typography including ligatures
  - Flowing text
  - Spellchecking
  - OpenType font features
- Convert shapes and text to fully editable curves
- Save and synchronize defaults
- Expressions

## User interface

- Persona task-orientated workspaces
- Customizable tabbed workspace
- High DPI (retina) support
- Multiple document views
- Windowed and Full Screen modes
- Docked or floating panels
- Comprehensive keyboard shortcuts and modifiers
- Customizable keyboard shortcuts
- Customizable toolbars
- Saveable Studio panel presets

## Design Aids

- Rotate document view
- Incredible zoom range
- Intuitive panning
- Saveable zoom viewpoints
- Powerful snapping control
- Dynamic snapping guides
- Pixel-accurate alignment for web graphics and website mockups
- Managers for Brushes, Grids, Snapping and other operations
- Automatic, fixed and projection grids
- Context toolbar and hintline
- Fluid document History <8192 steps with branching control
- Save history with document (multi-session)
- Snapshots
- Keyboard modifiers for on-the-fly tool changes
- Mixed-mode assistant for layer creation behavior according to the user’s preferences

## Interoperability

- Affinity Photo 2 files can be opened in other Affinity products and vice versa
- In-app license activation
- Content sync of Affinity Store purchases

## Document control, Import, Export and Printing

- Easy Document Setup with preset thumbnails and template support
- Affinity Designer 1/2, Affinity Photo 1/2, Affinity Publisher 1/2 file placement
- High-quality Adobe® Photoshop® PSD import, place and export
- Adobe Illustrator (.ai) import and place
- PDF import
- PDF passthrough for absolute display/output fidelity
- Place images (PNG, JPEG, GIF, TIFF, SVG, EPS, EXR, HDR)
- SVG import and export, including Inkscape extended SVG support
- Stock panel for free and royalty-free image resources
- Export layers, groups and pages to PNG, JPEG, TIFF, GIF, EPS, SVG and PDF
- Preserve layers in exported TIFF images
- Draw custom-sized slices at export time
- Use slice presets for popular image formats
- Multiple export setups, formats and resolutions per slice
- Output all slices at once, just one slice, or selected slices
- Export automatically to retina (@2x, @3x)/high DPI
- Set export areas and file formats during or after photo editing
- Export document or current selection(s) to many raster image formats, PSD, PDF, EPS and more
- Export Preview
- Export as template
- Desktop printing with Layout, Paper Handling, Feed, and Duplexing control
- Web-ready PDFs (Acrobat) with presets
- Professional hi-res PDF/X printing (CMYK) with presets
- Spot colors and overprint control

#### SEE ALSO:

- [Affinity Photo 2](01-what-is-affinity-photo.md)
- [Personas](03-about-personas.md)
