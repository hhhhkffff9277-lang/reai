---
name: reai
description: Research, draft, revise, and review evidence-backed WeChat long-form analysis. Use for REAI articles, topic discovery, editorial image planning, and explicitly requested article draft packages. For native image-led posts, use a dedicated image-note workflow.
---

# REAI

## Purpose and boundaries

Turn a concrete topic into an article with a clear judgment, traceable evidence, and a sentence readers can retell. Explain how technology or events change costs, labor, access, trust, responsibility, or bargaining power.

Write and edit in the current reasoning session. Do not call external text or image generation APIs. Generate new images only when the user explicitly requests them, using Image 2 / the host's built-in image generation. Do not render final image assets with Python, PIL, matplotlib, SVG, canvas, or browser screenshots.

Follow the user's requested voice and scope. First-person experience must come from the user, never an invented personal story. A request for text alone does not authorize image generation or WeChat upload.

## Workflow

1. Identify topic, reader, purpose, source material, and requested delivery. Infer routine choices; ask only for material missing information.
2. For changing facts, research before drafting. See [research](references/research.md). Prefer primary sources; cross-check precise numerical claims independently. Mark single-source uncertainty and omit unsupported figures.
3. Read [writing playbook](references/writing-playbook.md). Establish the hook, stance, concrete cases, demonstration direction, and risk boundaries. Make the central judgment repeatable in one sentence.
4. Draft concrete scenes, evidence, mechanisms, and implications. Use cross-domain judgment when useful without pretending to be an expert or spokesperson.
5. Match the title's hook to the evidence. Avoid generic AI prose, company cheerleading, unsupported alarm, and investment recommendations.
6. Plan images when relevant. When actual images were requested, read [visual guidance](references/visual-gpt-plus.md), generate through the built-in tool, and preserve the selected generated files.
7. Read [quality gate](references/quality.md); fix material weaknesses before delivery.
8. Only when the user explicitly requests a WeChat draft, read [publishing](references/publishing.md). Validate the complete package before making any network request. Create a draft, never a public send.

## Output

For writing: title alternatives, digest, Markdown body, stance notes, requested image plan/assets, and review notes. Keep internal uncertainty and review notes outside the published body unless relevant to readers.

For a local article package:
- article.md
- title.txt
- digest.txt
- redteam_notes.md
- images/ containing only supplied or explicitly requested real assets

For upload: report the returned draft identifier and local folder; distinguish draft creation from public publication. If an optional tool or account is unavailable, complete independent work and state the missing part.

## WeChat body invariants

- Do not repeat the platform title as an in-body H1 or first sentence.
- Use short paragraphs and clear heading levels; number main sections when helpful.
- Use a final 参考资料 section for published sources.
- Do not leave image prompts or missing-file placeholders in a publishable body.
- For dense comparisons, simplify into readable prose or explicitly requested image-based tables; do not generate images merely to satisfy a template.

## Supporting references

- [Atomic knowledge](references/knowledge.md): reusable rules and how to update them when requested.
- [Example output](references/example-output.md): illustrative structure, not a factual case or required persona.

## Optional tools

The scripts only convert text, validate files, and upload an explicitly authorized draft. They do not write articles or generate images. Use repository-relative paths; no author-specific server, account, credential store, or external project is required.

Read the repository README for installation, usage, sharing permissions, and the Issues feedback route. Respect the user's existing authorization; do not require repeated approvals for the same authorized draft task.
