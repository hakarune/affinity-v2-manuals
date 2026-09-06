# Linked Services

Affinity's Linked Services feature allows for a seamless experience when a document uses linked resources stored in your Dropbox or iCloud Drive and you need to continue working on the document on a different device.

## Why Linked Services is necessary

The path to a linked resource stored in Dropbox or iCloud Drive can be broken down into two parts. For example:

/Users/Serif/Dropbox/Affinity Projects/Flyer/Resources/image.tiff

The green part is the path to the resource within cloud storage and is the same on all devices.

The red part is the path to the folder to which cloud storage is synced. It may differ between devices, e.g. if user accounts have different names or Dropbox is configured to sync to a different drive, which can lead to missing resource warnings.

Normally, Affinity stores the full path to any linked resource. With Linked Services, the device-specific part is replaced with a reference to the relevant cloud storage provider, and only the cloud-related part of the path is stored. The earlier example would then be stored as:

Dropbox:/Affinity Projects/Flyer/Resources/image.tiff

Affinity knows to replace the prefixed reference with the path to cloud storage on the device that is currently in use.

## iCloud Drive

The benefits of Linked Services are automatic for linked resources in iCloud Drive. Your Mac, iPad or PC only needs to be signed into iCloud Drive via System Settings (or System Preferences), Settings or iCloud for Windows, respectively.

## Dropbox

You will need to install Dropbox's software and sign into the same account on each of your devices and then grant permission to each Affinity app on each of your devices to link to your Dropbox.

**To link your Affinity app to your Dropbox account:**

1. Select **Affinity Designer>Settings** (or **>Preferences**).
2. Select **Edit>Settings**.
3. Select **Linked Services**.
4. Next to Dropbox, click **Link**.
5. The Dropbox website will open. Follow its instructions to link your Dropbox account to Affinity. At the end of the process, you will be returned to your Affinity app.

**To unlink your Affinity app from your Dropbox account:**

1. Select **Affinity Designer>Settings** (or **>Preferences**).
2. Select **Edit>Settings**.
3. Select **Linked Services**.
4. Next to Dropbox, click **Unlink**.

#### SEE ALSO:

- [Placing content](02-placing-content.md)
- [Resource Manager](03-resource-manager.md)
- [Settings (or Preferences)](../27-settings-preferences/01-settings-preferences.md)
