# Scientific editing follow-up, 5 October 2026

Version 3.4.1 makes a few decisions from recent manuscript editing explicit.
It follows fork commit `e2aeb87f17575e4fa4db90a8c428b84ed8a87a8e`.
Both manual skill copies matched that revision before this review. Upstream main
remained at `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8`, and the heads of
upstream PRs 304, 305, 307 and 308 matched the previous review. Their earlier
[dispositions](upstream-review-20261003.md) therefore remain applicable.

| Editing issue | General guidance |
| --- | --- |
| A single author requests impersonal prose | Follow that preference. Name the method, data or finding when accurate; use passive voice where the action matters. Other documents can retain first person. |
| “Larger change” is ambiguous for negative values | Preserve the distinction between a signed value and its absolute magnitude. |
| A shorter label changes an operation | Preserve the quantity being transformed and the order of transformation, scoring and aggregation. Check the label against its definition in text, tables and captions. |
| A source cannot be accessed | Keep that access failure separate from evidence that an event or explanation is absent. |
| A review claims complete coverage | Identify the file version, actual passages read, checks repeated after editing and inherited decisions. Counts alone do not establish quality or factual support. |

The existing safeguards already cover meaningful technical terms, necessary
contrasts, grammatical suffixes and mathematical punctuation. The 26 patterns
remain editorial prompts. Specific word preferences, manuscript pronouns,
figure fonts, colors and citation styles belong to the relevant project.
They are not added as universal prohibitions or required formats.

The optional voice examples now show impersonal prose that retains a
retrospective data choice, and a numerical comparison that states absolute
magnitude explicitly. These are illustrative editing examples.

Two independent automated rewrite exercises used supplied passages without
expected answers or external research. Five of six initial rewrites preserved
the tested meaning. One incorrectly moved mean subtraction from a window to
its score. That output remains in the [exercise record](rewrite-checks-20261005.json).
A short transformation instruction was added, and three follow-up cases
preserved the relevant distinctions. This limited exercise does not estimate
general accuracy or compare live Claude, free-code and Codex behavior.

A separate automated review found no actionable issue in the six instruction,
example and version-file changes, including the transformation clause. Package
validation, seven existing validator tests, Skills CLI discovery, Claude
marketplace validation and the Codex skill validator passed. No executable
package behavior changed, so no new mechanical tests were added.

Installation uses the exact merged GitHub revision, with complete supporting
files. Before replacing a shared copy, compare its current hashes with the
pre-review snapshot. Preserve displaced directories and the installer metadata,
and update only Humanizer's source record. Existing free-code and Grok links
continue to use the Claude skill directory. Installation receipts are local
machine records; the repository remains portable.

Inspection also found an enabled free-code plugin at version 2.8.2 from
`blader/humanizer`, alongside the current manual skill link. The previous
installation check covered the manual copies and missed that plugin. The README
now includes both installation routes. Claude's
[plugin management documentation](https://code.claude.com/docs/en/discover-plugins)
describes the separate marketplace, cache, installed version and enabled state.
