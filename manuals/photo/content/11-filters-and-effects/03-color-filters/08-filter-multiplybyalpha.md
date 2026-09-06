# Multiply by Alpha

The Multiply by Alpha filter ensures the transparency in an image is stored using a premultiplied alpha representation.

Some apps, such as compositing software and game engines, expect premultiplied alpha even though an image file format may store a non-premultiplied alpha representation by default.

When an image containing non-premultiplied alpha data is composited using a system that expects premultiplied alpha data, a halo effect may be noticeable along semi-transparent edges, for example.

The filter addresses this by converting to premultiplied alpha, enabling improved antialiasing along the edges.

![Before](../../../assets/shared/filter_multiplybyalpha_before.jpg)
![After](../../../assets/shared/filter_multiplybyalpha_after.jpg)

> **Note:** Non-premultiplied alpha is sometimes called straight alpha or unassociated alpha. Conversely, premultiplied alpha is sometimes referred to as associated alpha.

## About the Multiply by Alpha filter

This filter can be found in the **Filter** menu, in the **Colors** category.

This filter has no customizable settings.

#### SEE ALSO:

- [Applying filters](../01-applying-filters.md)
- [Divide by Alpha](03-filter-dividebyalpha.md)
