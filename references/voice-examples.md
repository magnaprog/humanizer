# Voice and preservation examples

Read these examples when a rewrite loses useful detail or needs to match a supplied voice. They illustrate editorial decisions; they are not factual research or evidence of authorship.

## Keep the writer's reaction

**Before:**
> I was impressed by the demo, but I am not sure the results will hold on our data. I want to try it on last month's sample before choosing a tool.

**After:**
> The demo impressed me, but I want to try it on last month's sample before choosing a tool. I am not sure its results will hold on our data.

The uncertainty, proposed sample, and decision remain. The rewrite adds no new experience or sentiment. In technical prose, first person may identify who made a judgment or performed an action; follow the document's conventions and the author's preference.

## A single author who excludes first person

**Request:** Keep this paper impersonal; use neither I nor we.

**Before:**
> We evaluate three records. We chose the third record after inspecting the results from the first two. Our score subtracts each window's own mean before calculating distances.

**After:**
> The evaluation uses three records. The third record was chosen after inspection of the results from the first two. The score subtracts each window's own mean before calculating distances.

The subjects name the evaluation and score. The passive sentence preserves the
retrospective choice without inventing an independent selector. Replacing “we”
with “I” would conflict with the request; repeating “this work” would add little.
Other documents may appropriately use first person.

## Keep the meaning of a numerical comparison

**Source notes:** A score is D minus S. D decreases by 1 unit; S decreases by 3
units. The score therefore increases by 2 units.

**Ambiguous draft:**
> The larger change in S makes the score rise.

**After:**
> The decrease in S exceeds the decrease in D in absolute magnitude, so the score rises by 2 units.

The signed change of minus 3 is smaller than minus 1. Its absolute magnitude is
larger. The rewrite states which comparison explains the subtraction; it does
not change the score or its favorable direction.

## Keep concrete details

**Before:**
> The detector was trained on eleven years of data. Evaluation used a held-out test era. Compared with several baselines, it showed a modest advantage.

**Too compressed:**
> The detector outperformed several baselines.

**After:**
> The detector was trained on eleven years of data and evaluated on a held-out test era. It showed a modest advantage over several baselines.

The training duration, test separation, and magnitude qualification all matter. Shorter prose is useful only when those details survive.

## Do not add color by inventing facts

**Before:**
> The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

**After:**
> The agents generated 3 million lines of code. Some developers were impressed, while others were skeptical. The implications remain unclear.

A light edit can be enough. The source gives no time of day, proportion of developers, or personal reaction from the writer. Do not add them to create a livelier story.

## Keep evidence limits outside promotional framing

**Source notes:** The update adds batch processing, keyboard shortcuts, and offline mode. Beta testers report faster task completion.

**Draft:**
> The update marks a revolution in productivity. It adds batch processing, keyboard shortcuts, and offline mode. Beta testers report faster task completion. Industry experts expect an impact across the sector.

**Rewrite:**
> The update adds batch processing, keyboard shortcuts, and offline mode. Beta testers report faster task completion. Industry experts expect an impact across the sector.

**Issue reported separately:** The supplied notes do not identify the industry experts or substantiate their prediction. Retain the attribution pending clarification, or correct it if the user authorizes factual revision and the evidence supports the correction.

The empty revolutionary framing can go. The material prediction remains visible for review. Do not silently change "beta testers" to "most beta testers" or claim a measured speedup.
