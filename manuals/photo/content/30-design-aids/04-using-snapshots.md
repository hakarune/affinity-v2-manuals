# Using snapshots

A snapshot stores the state of your work at an arbitrary point in time, much like a freeze frame.

In contrast to reverting edits step-by-step using the **History** panel, snapshots let you instantly restore your work to an explicitly defined stage.

You might do this in advance of carrying out a sequence of complex operations to allow yourself to step back to a specific point in time if things don't go to plan.

Multiple snapshots can be created. So, if you're experimenting with different design ideas, you can also create a different snapshot for each one to help you decide which idea you prefer, all while working in a single document.

If needed, you can create a new document from a snapshot.

## About the Snapshots panel

The **Snapshots** panel is available in the **Photo Persona** and the **Develop Persona**.

In the Develop Persona and Photo Persona, the panel is collapsed in the right studio and hidden by default, respectively. For the latter, the panel can be displayed via **Window** menu.

In the Photo Persona, it can be used in conjunction with the **Undo Brush Tool** to paint back to a chosen snapshot.

**To create a snapshot:**

1. On the **Snapshots** panel, click **Add Snapshot**.
2. (Photo Persona only, optional) On the dialog, enter a name to help identify the snapshot at a later time. If you don't, the snapshot's name will be its date and time of creation.
3. (Photo Persona only) Click **OK**.

**To restore a snapshot:**

1. On the **Snapshots** panel, select a snapshot from the list.
2. (Photo Persona only) Click **Restore Snapshot**.

**To paint pixels from a snapshot (Photo Persona only):**

1. On the **Layers** panel, select a pixel layer.
2. On the **Snapshots** panel, click the **Set undo brush source** icon to the left of the required snapshot.
3. Select the **Undo Brush Tool**.
4. Paint where you want to restore pixels from the selected snapshot.

**To create a new document from a snapshot (Photo Persona only):**

1. On the **Snapshots** panel, select a snapshot from the list.
2. Click **New Document From Snapshot**.

**To delete a snapshot:**

1. On the **Snapshots** panel, select a snapshot from the list.
2. Click **Delete Snapshot**.

## Snapshot layers

A snapshot layer is created from a predefined project snapshot and is added to your project as a single, flattened pixel layer.

**To create a snapshot layer:**

- From the **Layer** menu, select a snapshot from the **New Layer from Snapshot** submenu. The snapshot layer is added above the current layer (or at the top of the Layers panel if no layer is selected).

#### SEE ALSO:

- [Snapshots panel (Photo Persona)](../33-panels/22-snapshots-panel.md)
- [Snapshots panel (Develop Persona)](../04-develop-persona-raw/09-snapshots-panel.md)
- [Undo Brush Tool](../32-tools/07-retouch-tools/05-undo-brush-tool.md)
- [History panel](../33-panels/11-history-panel.md)
