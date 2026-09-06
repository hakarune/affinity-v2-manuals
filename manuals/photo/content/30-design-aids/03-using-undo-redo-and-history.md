# Using undo, redo and history

It's easy to revert changes to a file when you've either made a mistake or if you simply don't like the result.

Any edits you make to your document are stored in the [History panel](../33-panels/11-history-panel.md). You can then use this, or keyboard shortcuts, to undo an edit. You can also redo an edit which you have recently undone.

> **Tip:** A document's history can be saved along with the document, so earlier edits can be returned to even if the document is closed and reopened.

Using the panel, if you undo back to a step in history and you continue editing from that step you can reinstate your redo history that would otherwise be lost. This might be because you changed your mind or if you made an edit that accidentally removed your redo history. Two branches in the history are created:

- a visible new branch containing any new edits.
- ![Cycle future](../../assets/shared/ui/cyclefuture.png) a hidden branch (viewable via a Cycle future icon) storing the redo history.

**To undo or redo a change:**

Do one of the following:

- From the **Edit** menu, click **Undo** to go back one step, or **Redo** to redo the step previously undone.
- On the **History** panel, click one of the entries in the list to jump to that step.
- On the **History** panel, drag the slider left to undo a change, right to redo a change.

> **Tip:** Shortcuts:
>
> - **macOS:** Undo: `Cmd` + `Z`
> - **Windows:** Undo: `Cmd`+`Z`
> - **macOS:** Redo: `Shift` + `Cmd` + `Z`
> - **Windows:** Redo: `Cmd`+`Shift`+`Z`

**To return to root:**

- On the **History** panel, drag the slider to the farthest position to the left.

**To save history with a document:**

1. From the **File** menu, select **Save History with Document**.
2. In the **Saving With History** dialog, click **Yes** to accept the conditions discussed in the dialog.
3. [Save your document.](../03-get-started/11-save.md)

> **Warning:** Saving your document's history with your document may significantly increase the size of your project file.

> **Note:** You can switch off the save history feature by repeating step 1 of the procedure above.

**To reinstate your redo history:**

- Click **Cycle future** at the history step where you want to reinstate your original redo history. This history is hidden 'within' the icon, and will be reinstated on clicking.

**To configure the History panel settings:**

1. **macOS:** In the **Affinity Photo 2** menu, click **Settings** (or **Preferences**).
2. **Windows:** In the **Edit** menu, click **Settings** (or **Preferences**).
3. Click **Performance**.
4. Drag the **Undo Limit** slider left to reduce the number of stored changes, right to increase the number of stored changes.
5. Click **Close**.

#### SEE ALSO:

- [History panel](../33-panels/11-history-panel.md)
- [Save](../03-get-started/11-save.md)
