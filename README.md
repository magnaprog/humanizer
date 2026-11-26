# Humanizer

Humanizer edits repetitive, inflated, or formulaic prose while preserving the writer's meaning. It keeps technical terminology, numerical context, uncertainty, citations, and document conventions intact.

This fork of [blader/humanizer](https://github.com/blader/humanizer) combines upstream's 26-pattern organization with safeguards developed during factual and scientific editing. See the [upstream review](docs/upstream-review-20261003.md) for the exact source commits, retained changes, and corrections. It is an editing skill; its patterns do not establish authorship or guarantee detector outcomes.

**Before:**
> The pipeline returns a ranked list of causes, not a single answer.

**After:**
> The pipeline returns multiple causes in ranked order.

A necessary scientific contrast should remain. For example, "The measurements are display values, not calibrated reflectance" already states a useful distinction.

## Installation

Install this fork, using `magnaprog/humanizer` as the source. A copy installed from `blader/humanizer` follows the separate upstream repository.

### Claude Code

```text
/plugin marketplace add magnaprog/humanizer
/plugin install humanizer@humanizer
```

The plugin command is `/humanizer:humanizer`. Both forks use the marketplace name `humanizer`; check an existing marketplace's source before changing it. A manual skill installation or the Skills CLI is also available:

```bash
npx skills add magnaprog/humanizer --global --agent claude-code
```

### Codex

```bash
npx skills add magnaprog/humanizer --global --agent codex
```

Codex discovers user skills under `~/.agents/skills`. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery rules. A separate duplicate under `~/.codex/skills` is not needed for this installation.

### Free-code and other compatible agents

For a manual installation, copy the skill directory with its supporting files, including `references/voice-examples.md` and the review document linked by the skill. Copying `SKILL.md` alone leaves those links unresolved. Follow your agent's configured skill directory.

On a free-code installation that uses `CLAUDE_CONFIG_DIR`, inspect that setting first. If its `skills/humanizer` is a symlink to Claude Code's skill, one update changes the shared target. Do not create another copy or replace that symlink without checking its purpose.

Check enabled plugins as well as manual skill directories in each configured
environment. An older `humanizer@humanizer` plugin can remain enabled after a
manual skill update. Inspect its marketplace source and installed version with
`claude plugin marketplace list` and `claude plugin list` under that environment's
`CLAUDE_CONFIG_DIR`. Update both routes when both are in use.

Before updating shared installations, preserve local modifications and coordinate with other writers. For an unmerged review branch, use the exact branch or commit named in the review instead of installing the current default branch. Reload skill discovery or start a fresh agent session after an update; existing conversations may retain previously loaded instructions.

## Usage

Call `/humanizer` with text, a file path, or a writing sample. You can also ask in ordinary language: "Humanize the prose in docs/launch-post.md."

The skill reads the source, drafts changes, checks every material claim and changed term, and reviews paragraph flow. Check third-party rewrites against the exact submitted source for changed claims, omissions, and truncation; keep any required verbatim service output separate from edited prose. A supplied writing sample controls voice when compatible with the task. It must not supply invented facts for the current passage.

The user's brief sets the depth of revision and governs authorial voice when an existing draft uses different pronouns. An authorized argument or document rewrite can rebuild the outline and paragraph roles while preserving evidence, scientific meaning, and material qualifications. The skill checks the whole document at the requested scope, including dependencies, captions, similar passages, and cross-references. It explains supported reasoning without inventing research motives or review by human experts. Cross-project examples supply editorial lessons, with proposed changes, adopted revisions, and later corrections kept distinct.

Author preferences govern pronouns, including a request for impersonal prose in
a paper with one author. Scientific edits preserve signed values versus absolute
magnitudes, aggregation order, and the definitions behind table and figure labels.
An inaccessible source cannot establish the absence of an event or explanation.

For pasted text, the default output contains a draft, a short review, and a final rewrite. File mode edits prose and reports issues separately. Embedded mode follows the parent task's output format. Code, inline commands, mathematical markup, labels, and source links remain intact unless the user authorized changes. Dated audit records, released change notes, frozen/generated content, and template-owned text remain unchanged unless explicitly in scope, including in files with editable prose.

For a results passage, the skill keeps the comparison and enough quantitative evidence to interpret it. A scientific document review also checks operational wording, the meaning of displayed zeroes and whether readers can follow captions, legends and accompanying instructions in their edition. The skill checks the scope of comparisons in figures, the meaning of bold rankings in tables, and which part of a cited study supports the present argument.

A requested annotation review or checklist preserves original IDs, versions, locations, context, decisions, and links to the final passages. The user's color meanings control the review. Overlapping marks and historical versions stay traceable; failed extraction, unresolved meanings, inaccessible sources, and protected passages cannot silently become completed revisions. Reports distinguish inventories, semantic reading, visual inspection, inherited decisions, applied edits, and final checks. Counts demonstrate coverage, not writing quality or authorship. Ordinary rewrites do not acquire mandatory reports.

On request, Humanizer searches a wording list before and after editing, including variant spellings and text inside exhibits. It distinguishes a resource allowance from a measured count and revision history from decisions that affect the interpretation of a result. It checks headings against their sections, uses the requested variety of English, and distinguishes a useful compound or serial list from wording that hides a relationship.

## The 26 patterns

These groups organize editorial checks. They do not rank measured detection strength. Keep a phrase that communicates the intended meaning well, and preserve required notation, supplied voice, and format conventions.

### A. Staging instead of stating

| # | Pattern | Check |
|---|---------|-------|
| 1 | **Not X but Y** | State the point directly when the whole distinction survives. |
| 2 | **One-line closers and dramatic fragments** | Remove repetitive closers and opening echoes; keep new interpretations and consequences. |
| 3 | **Sayings that sound deep** | Clarify the supplied claim without inventing a mechanism. |
| 4 | **Staged run-up before the point** | Remove empty announcements and stock warm-ups; keep useful questions and reassurance. |
| 5 | **Arguing with no one** | Keep actual objections, alternatives, and constraints. |

### B. Rhythm by rule

| # | Pattern | Check |
|---|---------|-------|
| 6 | **Forced triads** | Keep every distinct item and its relationships. |
| 7 | **Repeated sentence openings** | Improve flow while retaining consistent technical names. |
| 8 | **Dashes as the universal connector** | Clarify clause relations; preserve notation and style requirements. |
| 9 | **Stacked qualifiers** | Remove redundant hedges; keep evidence limits. |
| 10 | **Hyphenated pairs everywhere** | Follow established spelling and grammar. |
| 11 | **Passive voice and missing subjects** | Name an actor only when the source identifies one. |

### C. Inflation and borrowed authority

| # | Pattern | Check |
|---|---------|-------|
| 12 | **Overused AI words** | Prefer precise wording; retain established technical uses. |
| 13 | **Inflated significance** | Remove empty praise; preserve material interpretations. |
| 14 | **Vague connection or association** | Name only the relationship established by the source. |
| 15 | **Shallow -ing riders** | Keep distinct claims and check their support. |
| 16 | **Sales language** | Replace empty sales framing with supplied information. |
| 17 | **Borrowed authority** | Preserve material attributions and flag missing support. |
| 18 | **Avoiding is, are, and has** | Use simpler verbs only when equivalent. |

### D. Formatting by rule

| # | Pattern | Check |
|---|---------|-------|
| 19 | **Bold as decoration** | Preserve useful structure, acronym expansions and meaningful table rankings. |
| 20 | **Decorative headings** | Follow the document template and retain semantic notation. |
| 21 | **Curly quotation marks** | Follow the target typography. |

### E. Leftovers from the chat and the draft

| # | Pattern | Check |
|---|---------|-------|
| 22 | **Chatbot residue** | Remove wrappers that do not belong in the deliverable. |
| 23 | **Knowledge-limit disclaimers and guesses** | Retain real evidence limits; flag unsupported guesses. |
| 24 | **A heading repeated in the first sentence** | Remove pure repetition; keep useful definitions. |
| 25 | **Writing about the document instead of its subject** | Keep necessary methods, provenance, and change history. |
| 26 | **Re-explaining what the reader knows** | Omit repeated openings and known background only when shared context is visible. |

## Sources and verification

The editorial list draws on [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and upstream Humanizer. These sources describe patterns; they do not validate this fork's performance. The [voice examples](references/voice-examples.md) illustrate preservation of supplied details. The [scientific editing follow-up](docs/scientific-editing-20261005.md) records the 3.4.1 decisions and limited rewrite checks.

Run the package checks with:

```bash
python3 scripts/validate-package.py
python3 -m unittest discover -s tests
npx --yes skills@1.5.20 add . --list
claude plugin validate .
```

Package checks establish structural consistency and discoverability. They do not prove the quality of arbitrary rewrites. The review document records the manual semantic checks and their limits.

## Version history

See [CHANGELOG.md](CHANGELOG.md). The fork and upstream have separate version histories; a higher local version number alone does not show that upstream changes were integrated.

## License

MIT. Upstream authorship and the original license are retained.
