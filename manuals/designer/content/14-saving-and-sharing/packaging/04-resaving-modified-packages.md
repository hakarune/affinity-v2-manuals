# Resaving modified packages

After making changes to a document stored in [.afpackage file format](01-about-packaging.md), you need to choose the appropriate Save command for the next step of your workflow.

Changes cannot be saved directly back to the package's file by selecting **File>Save**. Choose one of the following:

- **File>Save As**—to save as an .afdesign file, which returns the document to the regular open/edit/save workflow. This command is a good choice when you want to save quickly and often as you work, or if you will make changes across multiple editing sessions.
- **File>Save As Package**—to save as an .afpackage file. You can save in an empty folder to create a new package and leave the original unchanged, or to the original package's folder to update it. This command is a good choice if changes are quick to complete and the document will be sent to a collaborator who may be missing some of its fonts or images.

### Saving over the original package

When you save a modified package to its original folder, the app will warn that the folder is not empty and prompt for confirmation. Choose one of the following options:

- **Yes**—to overwrite the existing .afpackage file and related files that have been modified since the package was last saved. Newly used fonts and images will be added to the package. Files will not be deleted from the folder, even if they are no longer used in the document.
- **No**—to choose a different folder.
- **Cancel**—to abandon the packaging process, e.g. if you have decided to save as an .afdesign file instead.

#### SEE ALSO:

- [About packaging](01-about-packaging.md)
- [Creating packages](02-creating-packages.md)
- [Opening packages](03-opening-packages.md)
- [Resource Manager](../../09-placing-external-content/03-resource-manager.md)
