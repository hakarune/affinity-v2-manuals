# Using plugins

Installed Photoshop-compatible 64-bit plugins can be made available to Affinity Photo 2 to extend the range of effects available to you.

## About plugins

Configuring plugins in Affinity Photo 2 can be automatic or be configured manually on a per plugin basis.

> **Note:** With an active internet connection, detected or added plugins are evaluated and their support status is reported next to the plugin name under the "Detected Plugins" list.

- *Automatic*: Some third-party plugins can install automatically to Affinity Photo 2's default plugin folder. No further configuration is needed.
- **macOS:** *Manual*: Installed plugins are located manually and then linked to from within Affinity Photo 2 as described below. You'll need to target the parent plugin folder itself, then allow supporting files, necessary for the plugin to operate, to be accessed.
- **Windows:** *Manual*: Installed plugins are located manually and then linked to from within Affinity Photo 2 as described below. You just need to target the parent plugin folder itself.

> **Note:** Due to the varying standard of third-party plugins, you may experience problems when using this feature. This is beyond Serif's control, so we recommend that you save your work before using plugins, then test your plugins before commencing.

**To view auto-configured installed plugins:**

1. **macOS:** From the **Affinity Photo 2** menu, select **Settings** (or **Preferences**).
2. **Windows:** From the **Edit** menu, select **Settings**.
3. Select the **Photoshop Plugins** tab.
4. **macOS:** Click **Open Default Folder in Finder**.
5. **Windows:** Click **Open Default Folder in Explorer**.

> **Note:** This default location is not configurable.

**To enable untested or potentially unsupported plugins:**

- Check "Allow Unknown Plugins to be used" beneath the Detected Plugins list.

**To link to your plugin file manually:**

1. **macOS:** From the **Affinity Photo 2** menu, select **Settings** (or **Preferences**).
2. **Windows:** From the **Edit** menu, select **Settings**.
3. Select the **Photoshop Plugins** tab.
4. **macOS:** Under the **Plugin Search Folders** box, click **Add**, then navigate to the parent folder that contains the .plugin file. For example, this could be in a Photoshop folder such as /Applications/Adobe Photoshop CS6/Plug-ins.
5. **Windows:** Under the **Plugin Search Folders** box, click **Add**, then navigate to the parent folder that contains the .plugin file. For example, this could be `C:\plugins\nik`.

> **Note:** You can add as many plugins as you like by repeating the above process.

**macOS:**

**To allow access to supporting plugin files:**

1. From the **Photoshop Plugins** tab, under the **Plugin support folders** box, click **Authorize Global**.
2. **macOS:** The folder dialog will default to root ("Macintosh HD"). You can click **Authorize** here and access to support files will be applied recursively, or you can specify a particular directory that contains the support files.
3. **Windows:** The folder dialog will default to root. You can click **Authorize** here and access to support files will be applied recursively, or you can specify a particular directory that contains the support files.
4. Press **Close**.

**To apply an installed plugin:**

- From the **Filters** menu, select the plugin from the **Plugins** pop-up menu.

> **Note:** You'll be prompted to restart Affinity Photo 2 for the plugins to take effect.

> **Tip:** If your plug-in entries are displayed but are grayed out, ensure that you have a pixel layer selected rather than a mask, adjustment, live filter, shape, curve, or text layer.

#### SEE ALSO:

- [Applying filters](01-applying-filters.md)
