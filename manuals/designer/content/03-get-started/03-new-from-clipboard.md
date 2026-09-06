# New from clipboard

You can create a new document based on the current contents on the clipboard. A 'paste as new document' command allows you to start a new project from a range of sources, e.g. from another project in Affinity products or from copied or captured imagery.

## Results from copied vector objects (or layers)

If you've copied a vector object to the clipboard, then the command will create a new document that is sized to the vector object. The copied object will *remain as a vector object* in the new document.

## Results from copied pixel selections

If you've copied a drawn pixel selection, the command will paste those pixels into a new 96dpi document in a *pixel layer*.

## Results from copied images or captured screenshots

If you copy images from Internet web pages or capture a screenshot to clipboard (e.g., using Apple's Screenshot app), the new document creates an *image layer*, not a pixel layer, from the copied data.
 The advantage being that the layer is non-destructive, i.e. it avoids rasterisation and loss of the image's original resolution and colour space. You can still manually rasterise by right-clicking the (Image) layer and choosing **Rasterise**.

**To create a new document based on clipboard contents:**

- From the **File** menu, click **New from Clipboard**.

> **Tip:** You can use this feature without having any document open.

#### SEE ALSO:

- [Creating new documents](02-create-new-documents.md)
- [Open documents and images](04-open-documents-and-images.md)
- [Keyboard shortcuts for file/document management](../26-keyboard-shortcuts/01-keyboard-shortcuts.md)
