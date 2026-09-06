# Object defaults

When you create new objects, their appearance is initially determined by the default settings for the particular object you are creating.

These defaults can be changed in the current document, saved globally for future documents or returned to factory settings at any time. Synchronizing defaults lets you base a new default on the currently selected object, with the option to save the defaults or revert to saved defaults if needed.

Each new document will always open with your saved default, as it is global setting unless you resave or reset to factory settings.

> **Note:** Object defaults are stored separately for stroke and fill attributes, artistic text attributes, table format and frame text attributes. The stroke attribute is the only object default that is applied to new picture frames.

**To synchronize defaults to current selection:**

1. Select an object with the attributes you wish to save as default settings.
2. From the Toolbar, select **Synchronize defaults from selection**.

Synchronized defaults override saved defaults for this document only. This is a great way to work with a set of defaults temporarily for a single document without having to save them.

For tables, synchronizing will make the currently selected table's table format and your chosen table text style as being the default. Any local text formatting of the table is not saved.

**To save defaults:**

- From the **Edit** menu, select **Defaults**, then **Save**.

The defaults used for this document become the global defaults for all future documents.

**To revert synchronized defaults back to saved defaults:**

- From the Toolbar, select **Revert defaults**. If an object is currently selected, its attributes revert to the default settings.

**To reset defaults to factory settings:**

- From the **Edit** menu, select **Defaults**, then **Factory Reset**. If an object is currently selected, its attributes revert to the default settings.

#### SEE ALSO:

- [Toolbar](../02-user-interface/02-toolbar.md)
