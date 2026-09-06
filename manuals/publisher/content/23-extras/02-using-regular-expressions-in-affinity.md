# Using regular expressions in Affinity

Affinity supports the use of regular expressions to find document content that matches specified patterns.

Regular expressions are used in several contexts in Affinity:

- On the **States** panel to toggle the visibility of layers whose names match a pattern.
- On the **Find and Replace** panel (available only in Affinity Publisher) to find document text that matches a pattern. Regular expressions are widely used across the word-processing and DTP community.
- To perform calculations in fields. See [Field input](02-using-regular-expressions-in-affinity/01-fieldinput.md) and [Expressions in field input](../26-expressions-for-field-input/01-expressions-for-field-input.md) for more information, including examples.

Writing regular expressions involves special syntax to specify patterns you want to find in text. Example scenarios and expressions provided below demonstrate common syntax you're likely to need to write your own expressions.

A comprehensive guide to the full power of regular expressions is beyond the scope of Affinity Help. You can learn more from online resources such as [www.regular-expressions.info](http://www.regular-expressions.info/) and [regexone.com](http://regexone.com/).

## Case sensitivity

When an expression matches letters, the States panel is case sensitive unless you explicitly state otherwise in the expression. The Find and Replace panel is case sensitive when the **Find** box's **Match Case** formatting option is enabled.

On each panel, case sensitivity can be overridden for part or all of an expression:

- The case of specific letters in an expression can be ignored by using a character class. For example, to match the letter *a* in either case, use *[aA]* in your expression. Character classes can also be used when matching a range of characters. For example, *[a-eA-E]* matches an individual letter from *a* to *e* regardless of its case.
- The case of all letters in an expression can be ignored by prefixing the expression with *(?i)*. For example, *(?i)internet* will match both *Internet* and *internet*.

## Example regular expressions

**Layer names containing either of two words followed by a specific word**

In an Affinity Photo document, we've used retouching tools to remove dust and blemishes from a photo by painting on layers above it.

Accordingly, each of these layers is named *Dust removal* or *Blemish removal*.

On the States panel, we can add a query that checks layer names match the regular expression *(?i)(Dust|Blemish) removal*, meaning either *Dust* or *Blemish*, followed by a space and then 'removal'. Letter case is ignored for the whole expression.

> **Tip:** After adding a query to the panel, use its **Hide** or **Show** button to instantly set the visibility of all layers that match the specified regular expression.

**Layer names containing two words in any position and order**

In an Affinity Designer document, we've used the layer name *offset fill* to identify layers that have been manually repositioned to create a handmade misprinted effect.

It's possible that we've typed these words in reverse order in some places.

On the States panel, we can add a query that checks whether layer names match the regular expression *(?i)(?=.*offset)(?=.*fill).*$*. This matches layer names that contain both words wherever each occurs in the name. Letter case is ignored for the whole expression.

**Layer names that follow a specific naming convention**

In an Affinity Designer document for a CAD architectural design, layer names identify building components with a two-letter prefix, followed by one or more groups of an underscore followed by some digits. For example, *Ss-35_10_15*.

On the States panel, we can control the visibility of layers that belong to a particular component category by using an expression like *[Ss][Ss](_[0-9]{1,})+*. The expression will work even if the prefix's letter case has been mistyped.

Conversely, we can control the visibility of all other component categories' layers with a small change near the start of the expression, so it becomes *(^[Ss][Ss])(_[0-9]{1,})+*.

**Instances of a word in document text except where preceded by a specific word.**

In an Affinity Publisher document, we want to find instances of a word throughout our text, but omit instances preceded by a specific word.

On the Find and Replace panel, with **Regular Expression** selected on the **Find** box's **Formatting** options, we can use the expression *(?>!proin )aliquam*. The results will include instances of *aliquam* except those preceded by *proin* and a space.

It's possible to exclude instances containing one of several preceding words. For example, to exclude instances where the word *error* is preceded by the article 'the' or 'an', use the expression *(?>!(the|an) )error*.

#### SEE ALSO:

- [Layer states](../09-object-control/21-layer-states.md)
- [Find and replace](../10-text/11-checking-text/02-find-and-replace.md)
