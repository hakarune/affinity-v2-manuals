# Features of Affinity Designer

Here's an overview of the features of Affinity Designer. Choose a category from the menu below, which includes options to view all features, or only those that are new in this version—marked with a red bullet (▪).

## New in V2.1

- [Vector Flood Fill Tool](../08-object-control/19-flooding-areas.md)
  - Flood with solid colour, gradients or bitmaps
  - Drag-and-drop swatches from Swatches panel
  - Flooding with assets or stock images
  - Takes stackable semi-transparent fills and bitmap fills with alpha
  - Intelligent flooding to visibly contrasting edges or object outlines/paths
- [Vector warp](../08-object-control/09-warping-objects.md) junction snapping:
   - Global snapping aware
  - Snap options to align intra-group junction(s) when dragged
  - Lasso selection with alt modifier
- Distort placed images and documents using non-destructive Live [Mesh Warp](../20-distortion-filters/01-mesh-warp-filter.md) or [Perspective](../20-distortion-filters/02-perspective-filter.md) filters
- [Rename artboards](../04-artboards/04-renaming-and-viewing.md) directly on the pasteboard
- Enhanced [Brushes panel](../23-panels/04-brushes-panel.md):
   - Show brush names
  - Show brushes as thumbnails
  - Disable Associated Tools for all raster brushes
  - [Highlights the active brush](../11-pixel-painting/04-creating-custom-pixel-brushes.md)
  - [Indicates modified brush settings](../11-pixel-painting/04-creating-custom-pixel-brushes.md)
  - [Auto-scroll/auto-switch to last used brush](../11-pixel-painting/01-painting-pixel-brush-strokes.md) when reusing brush tools (intra- and inter-category)
  - [Alt-click on a new brush keeps your current brush width](../11-pixel-painting/01-painting-pixel-brush-strokes.md)
  - [Update Brush and Reset Brush](../11-pixel-painting/04-creating-custom-pixel-brushes.md) if modified
- Paint with [bitmap textures drag-and-dropped](../10-vector-painting/02-modifying-vector-brush-strokes.md) to Colour or Swatches panel
- [Show special characters](../12-text/10-special-characters-and-glyphs.md) on Text menu
- Assets panel:
   - [Expand All/Collapse All subcategories](../23-panels/03-assets-panel.md)
  - [Sort assets by name](../23-panels/03-assets-panel.md)
  - Modifier-free reordering of [asset subcategories](../08-object-control/24-using-assets.md)

  Layers panel:
   - Hide layer type icons
  - [`Alt`-click to Expand/Collapse All](../23-panels/11-layers-panel.md) (child layers) in Layers panel
  - [`Alt`-drag to duplicate](../07-layers/02-create-layers.md)
  - Step-through renaming of [layers](../07-layers/04-selecting-and-editing-layers.md) and [export slices](../15-exporting/01-exporting-using-export-persona.md) with Tab key
  - [Rename layers](../07-layers/04-selecting-and-editing-layers.md) via the Layer menu (plus shortcut)

  [Disable auto-selection with Move Tool, plus `Cmd`  override](../08-object-control/01-selecting-objects.md)
  [Keyboard shortcuts](../26-keyboard-shortcuts/01-keyboard-shortcuts.md) for layer and brush blend modes
  [Guides](../17-design-aids/06-ruler-and-column-guides.md) improvements:
   - Double-click any guide to open Guides Settings
  - Drag distance (delta) shows in on-screen readout
  - Drag a guide from rulers will switch on guide visibility (if set to off)
  - Clone guides with `Cmd`-drag
  - Delete guides with `Alt`-click
  - Snap guides to ruler units based on the spread origin with `Shift`-drag
  - Snap guides to drag distance (delta) based on ruler units with `Shift` + `Alt`-drag
  - Snap to original guide position when moving guides
  - Snap to original guide when cloning guides
  - Nudge guide values with mouse wheel/arrow keys
  - Link margin values or X/Y spread origin values in Guides Settings

  One-click [bitmap fill creation](../06-colour/12-gradient-and-bitmap-fills.md) from assets or stock images
  Create [bitmap fills by drag-and-drop](../06-colour/12-gradient-and-bitmap-fills.md) from Finder/File Explorer to Colour or Swatches panel
  [Adjust stroke width](../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md) using Node Tool or shape tools using [ or ] keys
  [Dashed line improvements](../05-drawing-curves-and-shapes/02-draw-curves-and-shapes.md)
  - Balanced dashes
  - Additional dash/gap pairing for more complex dash combinations
  - Zero-length dash or gap widths for more balancing control
  - Set dash or gap widths in 0.1 increments
  - Set dash or gap width values using draggable indicators

  [Clear arrowhead settings](../23-panels/16-stroke-panel.md)
  [PDF document properties (metadata)](../03-get-started/05-importing-pdf-documents.md) are retained on import
  [Close All](../03-get-started/17-close.md) to close multiple open documents (with Apply to All option)
  Search Bar for [searching add-on content](../03-get-started/01-app-activation-and-installing-content.md) in your Account
  [V5 PANTONE® Solid, Process Coated and Uncoated update](../06-colour/06-selecting-colours.md)

## Power, performance and compatibility

- Optimised for:
   - Grand Central Dispatch (GCD)
  - OpenGL
  - Core Graphics
  - Direct3D
  - 64-bit engine
  - GPU hardware acceleration (Metal) for integrated, discrete and external GPUs
  - Hardware GPU acceleration (OpenCL) for integrated, discrete and external GPUs
- Display support
   - Regular, Retina and expanded gamut DCI-P3
  - Wide colour gamut (Display P3)
  - HiDPI
  - EDR
  - HDR (Windows; >400 nits recommended)
- Mac with Apple M1/M2 chip or Intel processor
- macOS Catalina 10.15 or later
- Create massive gigapixel-sized documents
- 16-bits per channel editing
- Sub-pixel accuracy
- Up-to-date tablet support
- Multi-touch support
- Surface Studio with Surface Pen and Surface Dial support
- Force Touch support (Magic Trackpad 2/MacBook/MacBook Pro)
- Touch Bar support (MacBook Pro)
- DirectX 10 compatible
- Windows® 11, Windows® 10 May 2020 Update (2004, 20H1, build 19041) or later

## Solid graphic design tools

- Artboards
- Intuitive Move Tool moves, scales, transforms
- Select multiple objects by type, colour, stroke weight, transparency, and more
- Rotate/transform from movable origin
- Customisable nudge distances
- Precise Pen Tool
- Contour Tool
- Arrowheads (and tails)
- Multiple strokes and fills per object
- Node Tool for fine tuning vectors
- Freeform Pencil Tool with Sculpt mode
- Stroke stabiliser for smooth pen, pencil and brush strokes
- Raster finishing without switching apps
- Smooth gradients (skew, scale and planar aware)
- Add noise to fills and strokes as a solid or graduated attribute
- Assets for object storage
- Customisable, saveable stroke styles
- Styles presets

## Powerful layer management

- Drag and drop layers
- Non-destructive adjustment layers
- Apply adjustments and blend modes at the stack, layer, group, selection or object level
- Clipping within layers
- High quality layer effects
- Pixel adjustments and effects on vectors
- Blend modes
- Layer and object Blend ranges (linear and non-linear)
- Per-object Blend gamma control
- Per-object hierarchical antialiasing
- Lock child layer positions
- Coloured layer entry tagging for easy identification

## External resource management

- Linked resources
- Embedded/linked resource policy on new document creation
- Resource Manager
- Collect linked resources
- Packaging for project portability

## Professional object control

- Symbols
- Corner Tool
- Boolean operations (Add, Subtract, Intersect, Divide, Xor)
- Live-preview non-destructive compounds (Boolean operations)
- Convert shapes and text to fully editable curves
- Duplicate and transform objects with precision
- Transform objects separately
- Point Transform Tool to scale/rotate about movable transform origin
- Customisable geometric shapes
- Select multiple objects by type, colour, stroke weight, transparency, and more
- Multi-node selection using polygon or freehand (lasso) drawing
- Multi-node selection, alignment and transform
- Control handle snapping to angles and distances

## Professional colour support

- 16-bits per pixel colour depth
- CMYK, Lab, Greyscale and RGB colour modes
- Colour panel (RGB, HSL, LAB, CMYK, Greyscale)
- Swatches panel for pre-supplied and custom colour palettes
- Colour Picker Tool (colour mode aware, pick from anywhere on screen)
- Global colours
- Colour tints
- Professional colour support
- PANTONE® colour support
- ICC colour profiling
- Import Adobe Swatch Exchange (ASE) colour palettes (including spot colours)
- Drag-and-drop colours from Chroma app (SoftPress)

## Vector brushes with stretch and corner controls

- High quality brush galleries
- Change brush size, hardness, and opacity on the fly
- Import/export brushes, including ABR file import
- Custom brushes (including image-based brushes)
- Multi-controller support including pressure and velocity
- Controller-specific brush dynamics
- Customisable controller ramps

## Text and typography

- Artistic and frame text
- Character and Paragraph panels
- Text styles
- Text on a path
- Path text overflow control
- Flowing text
- Spellchecking
- Advanced typography including ligatures
- OpenType font features
- Comprehensive bullets and numbering

## User interface

- Persona task-orientated workspaces
- Customisable tabbed workspace
- High DPI (retina) support
- Multiple document views
- Windowed and Full Screen modes
- Docked or floating panels
- Comprehensive keyboard shortcuts and modifiers
- Customisable keyboard shortcuts
- Customisable toolbars
- Saveable Studio panel presets

## Design Aids

- Pixel, Retina, and Outline view modes with Split View support
- Constraints for intelligent object scaling/anchoring
- Rotate document view
- Incredible zoom range
- Intuitive panning
- Saveable zoom viewpoints
- Dynamic snapping guides for precise alignment
- Fixed guides and column guides
- Rulers with spread origin control
- Multi-object alignment and distribution
- On-object alignment handles
- Pixel-accurate alignment for web graphics and website mockups
- Managers for Brushes, Grids, Snapping and other operations
- Automatic, fixed and projection grids
- Context toolbar and hintline
- Fluid document History <8192 steps with branching control
- Save History with Document (multi-session)
- Snapshots
- Keyboard modifiers for on-the-fly tool changes
- Mixed-mode assistant eases vector and pixel mode switching according to the user’s preferences
- Defaults (document and global)
- Isometric/advanced axonometric grids
   - Isometric Panel for easy grid creation, as-you-draw transforms and plane switching
  - On-page draggable grid origin with grid axis scaling and angle adjustment
  - Grid presets
  - Cube mode for custom grids from transformable cube

## Pixel-based designs

- Seamlessly switch to and from pixel editing mode to apply finish to vector artwork
- Pixel brushes for high-quality textures
   - Import/export brushes, including ABR file import
  - Custom brushes
  - Create brushes from any pixel selection on pixel or mask layer
  - Change brush size and colour on the fly
  - Sub-brushes (combined brushes)
  - Brush symmetry and mirroring
  - Choice of brush and nozzle controllers/ramps
- Pixel selection tools
   - Shaped selections
  - Smart selection brush works over pixel and vector data
  - Freehand Selection Tool with Polygonal and Magnetic modes
  - Refine selections to capture fine detail
  - Flood selection
- Pixel adjustment brushes
   - Dodge and Burn brushes
  - Smudge, Blur and Sharpen brushes
- Masks
- Pixel flood fill tool
- Pixel and vector artwork exported in harmony
   - Pixel artwork scaled if required on output
  - Nearest Neighbour, Bilinear, Bicubic and Lanczos 3 pixel scaling available
  - Set export areas and file formats during or after the design process

## Interoperability

- Retention of vector design elements when cutting and pasting between Affinity Designer and other applications
- Affinity Designer files can be opened in other Affinity products and vice versa
- In-app licence activation
- Content sync of Affinity Store purchases

## Document control, Import, Export and Printing

- Easy Document Setup with preset thumbnails and template support
- Affinity Designer, Affinity Photo, Affinity Publisher file placement
- High-quality Adobe® Photoshop® PSD import, place and export
- Adobe Illustrator (.ai) import and place
- PDF import
- PDF passthrough for absolute display/output fidelity
- Place images (PNG, JPEG, GIF, TIFF, SVG, EPS, EXR, HDR)
- SVG import and export, including Inkscape extended SVG support
- Stock Panel for free and royalty-free image resources
- Export slices, layers, pages, and artboards to PNG, JPEG, TIFF, GIF, EPS, SVG and PDF
- Preserve layers in exported TIFF images
- Export automatically to retina sizes (@2x and @3x)
- Set export areas and file formats during or after designing
- Export document or current selection(s) to many raster image formats, PSD, PDF, EPS and more
- Export Preview
- Desktop printing with Layout, Paper Handling, Feed, and Duplexing control
- Web-ready PDFs (Acrobat) with presets
- Professional hi-res PDF/X printing (CMYK) with presets
- Spot colours and overprint control
- Bleed (with preview) and printers marks

#### SEE ALSO:

- [Affinity Designer](01-affinity-designer.md)
- [Personas](03-personas.md)
