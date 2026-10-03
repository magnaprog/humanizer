# Upstream and installation review, 3 October 2026

This update reconciles three different sources. A local version number did not mean that either GitHub repository held the installed changes.

| Source | Observed state before this update |
| --- | --- |
| `magnaprog/humanizer` main | `a4672cd24cf22c369ffc8149ff26fcfc2ffe7c0d`, version 3.0.0 |
| `blader/humanizer` main | `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8`, version 3.1.0 |
| Codex and Claude Code installations | Identical seven-file copies, skill metadata 3.3.0, without Git history |
| Free-code installation | A symlink to the Claude Code copy |

The installed `SKILL.md` had SHA-256 `3ac05279aff87d723ead232627120cac41d24ce7c3f0b6e595c25a73dc8c4c2f`. Both copies matched the earlier 2 October audit. The local installer record still named `blader/humanizer`. Plugin metadata also pointed upstream and omitted the explicit root skill loader present in both repositories. The installed folders lacked the repository's validator and OpenAI UI metadata.

The repositories had diverged: upstream contained 43 commits absent from the fork, and the fork contained one commit absent from upstream. This review uses a merge to retain that history and then reconciles the content. Release 3.4.0 incorporates the useful installed safeguards; it does not treat the unversioned copies as a separate Git ancestor.

## What changed

| Area | Decision and reason |
| --- | --- |
| 26-pattern organization | Adopt upstream's consolidation and numbering. Retain technical naming consistency as a precision safeguard, even though upstream no longer treats synonym cycling as a current authorship cue. |
| Inline code and edited text | Adopt explicit protection for inline commands and the rule that text being edited is content, not instructions. |
| Shared conversational context | Adopt the new reply check, restricted to visible shared context. Preserve explanations the user requests and the context needed by standalone documents. |
| Package maintenance | Adopt pinned CI dependencies, changelog separation, manifest/schema corrections, pattern-name checks, section-reference checks, and the word budget. Retain the optional Cursor manifest without claiming a live Cursor test. |
| Scientific and factual prose | Retain the installed rules for quantities, denominators, aggregation, terminology, acronym definitions, citations, mathematical markup, scope, and assumptions. Preserve distinctions between association and causation, exact results and estimates, and checkpoints and fitted models. |
| Contrasts and qualification | Preserve substantive negatives, alternative designs, uncertainty, and interpretation. A rhetorical pattern cannot authorize deleting a material claim. |
| Voice | Keep supplied reactions and details. Correct the fork's original voice examples, which introduced sleeping humans, an unsupported split among developers, and "most" beta testers. |
| Punctuation and word forms | Replace blanket bans and occurrence quotas with contextual checks. Keep required notation and formatting. Provide a deterministic inventory when requested, separately from ordinary rewrite output. |
| Authorship claims | Do not import unvalidated strength rankings, claims that a word is a tell wherever it appears, or the claim that pre-ChatGPT text cannot be AI-written. Remove unsupported human-versus-model generalizations and detector performance promises. |
| Examples | Correct additions such as a new management mechanism, a hash-map implementation, an exact count of vendors with missing prices, a user study, or invented emotional reactions. Preserve bounds such as "over 3,000" and first-use acronym expansions. |
| Fork identity | Installation links and package repository URLs point to `magnaprog/humanizer`. Original authorship and MIT license remain. |
| Validator | Fix duplicate pattern numbers/rows being hidden by dictionary construction. Report malformed marketplace JSON plainly. Require the supporting files referenced by the installed skill. |

The skill is shorter because overlapping rules were consolidated, not because evidence limits were removed. Project-specific examples and an obligatory punctuation report are not global requirements. The general editing workflow covers terminology, sentence flow, paragraph openings, and final claim preservation without requiring external searches for ordinary grammar.

## Open upstream PRs

The open-PR list contained four entries at this review. Their complete file diffs were inspected; all four had no reviews, issue comments, or inline review comments at the time of retrieval. These decisions concern the exact heads below, not later revisions. No upstream PR branch was merged wholesale.

| PR and head | Decision |
| --- | --- |
| [#304](https://github.com/blader/humanizer/pull/304), `2b0b0c0303fd887f89bc4cd4ca462e1bb2758fdc` | The malformed marketplace-JSON fix is already implemented here and has a negative test. Do not require its exact README pattern anchor: this fork does not have that navigation link. The numbered tables and heading are checked. |
| [#305](https://github.com/blader/humanizer/pull/305), `2b0379c1651ef5c51574755607f9bee9d3763bae` | Adopt the intent of preserving facts, leaving effective prose alone, and avoiding mechanical rhythm or punctuation substitutions. Equivalent corrections are already present. Do not copy its remaining inference that the replacement function avoids the old complexity, its unsupported generalization about people trusting symmetry, or its blanket punctuation/authorship claims. |
| [#307](https://github.com/blader/humanizer/pull/307), `b6039ead39f824baf5527471dc3f71fd4774505a` | Defer removal of `$schema`. Current official Claude documentation lists it as editor metadata ignored at runtime, and local direct manifest validation passes with `--strict`. The SDK warning described by the PR was not reproduced. The claim that no tool reads it conflicts with its documented autocomplete purpose. Revisit if a supported loader demonstrates a problem. |
| [#308](https://github.com/blader/humanizer/pull/308), `4ae291eb0c12a4788fcf418dc6eae7ac1822de27` | Add redundant closing echoes, stock warm-ups, drum-roll questions, and repeated reply openings to existing checks. Preserve genuine reassurance, useful FAQ/tutorial questions, and acknowledgments that serve the exchange. Do not adopt automatic removal merely on seeing a phrase or the PR's separate version bump. |

The manifest decision follows the [official field reference](https://code.claude.com/docs/en/plugins-reference#fields). CLI validation does not establish compatibility with every Agent SDK version. The PR review covers all four entries open at retrieval; it does not claim a separate review of every historical closed PR. Merged changes reachable from the pinned upstream main are included in the main comparison.

## Manual semantic checks

These are source-to-rewrite inspections. They are not automated model evaluations and do not establish an error rate on arbitrary input.

| Check | Required result in the revised guidance |
| --- | --- |
| Association between a merger and outcomes | Remains an association; no new causal mechanism. |
| Display values versus calibrated reflectance | Keeps the explicit scientific contrast. |
| Ranked causes | Keeps plurality and ranking. |
| A measurement followed by an interpretation | Preserves the interpretation without inventing an experimental condition. |
| Restarting authentication to rotate tokens | Keeps the practical consequence for active sessions. |
| Unknown actor in passive prose | Keeps the actor unspecified. |
| More than 3,000 square feet | Keeps the strict bound and the original type of space. |
| Acronyms in bold text | Removes decoration while retaining first-use expansions. |
| Three actual event activities | Retains every activity rather than enforcing a list length. |
| Unidentified expert prediction | Preserves the material attribution and flags the missing support separately. |
| Historical implementation description | Does not invent the new data structure, complexity, or completion of an intended replacement. |
| Pricing provenance | Keeps the origin and unconfirmed-entry convention without inventing a count. |
| Known context in a reply | Removes only background already supplied by the reader. |
| Voice example about generated code | Does not invent a time, reaction, or percentage. |
| File and embedded output | Keeps code and mathematical markup; does not insert an unsolicited punctuation report. |

## Verification scope

The repository checks cover consistent versions/descriptions, one root skill, the Claude loader, pattern names/numbers, supporting files, and the prompt's word budget. Seven isolated validator tests exercise valid input, duplicate headings, duplicate README rows, malformed JSON, missing support, a missing loader, and version mismatch. Skill discovery and Claude marketplace validation must also pass before publication, as required by `AGENTS.md`.

These checks do not prove that a language model will always preserve meaning. The installed paths and file hashes need a separate deployment receipt. No benchmark score, universal authorship test, or detector-evasion guarantee is claimed. The independent paper audit's suggested patch was reviewed for its findings; it was not blindly applied to the reorganized upstream prompt.

## Independent rewrite exercise

A separate Codex invocation received the complete candidate prompt and ten source passages, with no expected answers. The initial file-based attempt could not initialize its nested read-only sandbox. The next invocation received the candidate directly as text and performed no file access.

Source-to-output review found a concrete failure: "was added to replace" became "replaced," asserting completion from an intended purpose. The prompt was revised to state that distinction explicitly, and sentence-merging guidance was tightened to preserve each result's conditions. The follow-up exercise covers intended replacement, pending measurements, matched versus unmatched comparisons, an explicitly completed replacement, and an abandoned migration.

All five follow-up outputs preserve the tested distinctions. The [input/output record](rewrite-checks-20261003.json) includes all nineteen cases and the initial failure. A further four-case exercise on the final prompt checks the PR #308 additions: redundant release-note framing is removed, genuine reassurance and FAQ structure remain, and repeated reply context is omitted. All four outputs preserve the requested meaning and genre. These exercises are small diagnostic checks, not a performance benchmark. Its raw prompts, outputs, source hashes, and reviewer decisions are retained with the private installation receipt. Initial failures remain in that record.

## Maintenance

Use the fork as the installation source. During PR review, pin the review branch or commit explicitly: `main` remains the previously published version until the PR merges. Check both installed copies before replacing either, preserve a backup, and retain a free-code symlink that shares Claude Code's installation. Do not assume that a running agent reloads instructions already in its context.

For future upstream updates, compare actual commits and semantic behavior, not version numbers alone. Recheck examples against their source text, especially when a cleanup appears to make a claim more concrete.

## Sources

- [Upstream commit reviewed](https://github.com/blader/humanizer/commit/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8).
- [Fork base](https://github.com/magnaprog/humanizer/commit/a4672cd24cf22c369ffc8149ff26fcfc2ffe7c0d).
- [OpenAI skill discovery](https://learn.chatgpt.com/docs/build-skills).
- [Wikipedia's contextual editorial guidance](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
