# Draw QR codes

Affinity allows you to draw a square shape in which it will generate a QR code using data you specify via the context toolbar.

![Example QR code](../../assets/shared/qrCode.png)
*An example QR code that links to a website.*

When setting a QR code's data, you can select from several common data types. Available settings depend on the selected type.

- **Text**—for encoding any text you wish, especially if it doesn't fall into one of the other types.
- **URL**—for visiting a resource, usually online, such as a web page, a downloadable file, or an FTP site.
- **Phone**—for making an audio call to a suitable telephone number.
- **SMS**—for sending a single-line or multiline text message to a telephone number.
- **Email**—for sending a message to a specified recipient, optionally with a default subject and body.
- **WhatsApp**—for sending a message to a user of Meta's instant messaging service.
- **FaceTime**—for making a video or audio call to a user of Apple's communication service.
- **Location**—for looking up a physical location using its longitude, latitude and elevation.
- **Wi-Fi**—for joining a wireless network using provided credentials, e.g. network name, encryption type and password.
- **vCard**—for sharing contact information as an electronic business card.
- **Data Merge**—for generating a QR code using a field of a data merge source you've already added to your Affinity document. Use in conjunction with **Data Merge Manager** and the **Data Merge Layout Tool**.

The Text data type can be used to encode freeform information. For example, it can be used to generate QR codes for:

- sharing calendar events as vCal (.vcal) and iCalendar (.ics) data.
- making calls with other communication services, such as Skype and Zoom.
- deep-linking to content in a mobile app using the app's custom URL scheme.

## Data validation

Each data type requires you to provide one or more values.

When a value is required and empty or is otherwise invalid, Affinity displays an alert icon ![Validation error](../../assets/shared/ui/preflightWarning.png) next to it. Hover the pointer over the icon for an explanation of what is considered to be valid.

Some values are optional. For example, you do not need to provide a message body for an email.

When using the Text data type, you will need to validate the data manually.

## QR code legibility

QR codes are constructed from small, square blocks called modules. Affinity automatically determines the appropriate module size based on data length and content. A QR code can consist of anything from 21 by 21 modules up to 177 by 177 modules.

QR codes are usually printed in black and white. In Affinity, the color of modules that are usually printed black can be changed using the **Fill** setting on the context toolbar.

Modules that are usually printed white are transparent. If this results in background elements of your design showing through the QR code, consider creating a rectangle behind the QR code to ensure the code can be scanned. QR codes also require a margin on all sides in which nothing is printed.

For further advice on QR code presentation, including the use of color and the code area and margin, see the [FAQ at the technology's official website.](https://www.qrcode.com/en/faq.html)

**To create a QR code:**

1. On the shape tools flyout, select the **QR Code Tool**.
2. In the document view, drag on the page to set the required size of the QR code.
3. On the context toolbar, select the **Data** setting. On the dialog that appears:
  1. Select the **Type** of data for which to generate a QR code.
  2. (Optional) Select **Clear** to remove any and all prepopulated information.
  3. Set all required information to a valid value.
  4. (Optional) Set additional information as needed.
4. Select **OK**.

The QR code automatically regenerates as you change its data.

> **Tip:** When creating a QR code for a URL, select **Visit Target URL** to the right of the URL to verify the target is correct.

> **Note:** A QR code's data can be modified at any time by using the QR Code Tool to select the code and then clicking the Data setting on the context toolbar.

#### SEE ALSO:

- [QR Code Tool](../20-tools/03-shape-tools/23-qr-code-tool.md)
- [Data Merge Layout Tool](../20-tools/01-layout-tools/07-data-merge-layout-tool.md)
- [Data merge](../13-references/11-data-merge.md)
