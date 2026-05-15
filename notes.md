# Chapter 2 — Linked Lists (Ruby)

## Vim autoread setup (Chapter 2 setup)

While setting up the Ruby chapter workflow, we confirmed that `autoread`
was already configured in `~/dotfiles-local/vimrc.local`. To make external
file changes (e.g. from Claude) reload faster in Vim, we added
`set updatetime=250` — this reduces the delay before `CursorHold` fires,
which is what triggers the file check. The tradeoff is slightly more
frequent swap file writes, which is negligible on modern hardware.

## AI-generated specs can miss the spirit of a problem (Problem 2.3)

Problem 2.3 asks to delete "a node in the middle" — meaning any non-first,
non-last node. The AI-generated specs interpreted this as "the middle node"
(the center) and only tested deletion at the exact midpoint. The test cases
weren't generic enough to match the actual problem description, which covers
any interior node. This was the first notable case of AI misunderstanding
leading to under-specified tests that would pass a subtly wrong implementation.

Takeaway: when reviewing AI-generated specs, check that the test cases cover
the full range implied by the problem description, not just the most obvious
interpretation.

## This very notes file (Chapter 2 setup)

Created `notes.md` to record interesting interactions and learnings from
the session. The first note documented a vim config change. The second note
is this one, which is about creating the file that contains the first note
and this note. We have achieved full self-reference. Descartes would be
proud.
