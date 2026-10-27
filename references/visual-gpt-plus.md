# Visual Generation Workflow

## Default

Generate actual image files only when the user explicitly requests images. A text-only article or local package request does not itself authorize image generation. When actual images are requested, do not substitute prompt text for the assets.

Use `gpt-image-2` through the built-in non-API image generation tool available in the current Codex/ChatGPT environment. If no such tool is available, report that image generation is blocked and stop before publishing, because a WeChat draft with missing images is not the requested output.

If web image search is available, use it as a supporting step before generation: search for candidate images whose elements match the article's scene, object, and social emotion. Prefer the best-matching visual reference or public/official image when usable. If search is restricted, skip automatically and continue with generation.

Quality failures are handled by reducing visual complexity and regenerating with the built-in image tool, not by local rendering. For a quality issue, simplify the asset until the model can plausibly produce it: fewer labels, fewer rows, larger spacing, less exact text, one idea per image, and exact values moved into the article body or caption when needed.

## Visual Priority

Prefer, in order:

1. Project site photos supplied by the user.
2. Web-searched official or highly relevant images, when rights and source are acceptable.
3. Company official images.
4. Video frames.
5. Paper figures.
6. Generated images.

Every image must serve the article's judgment. Avoid blurry screenshots, broken PDF fragments, vague atmosphere, and images with no information point.

## Standard Image Set

When explicitly requested, the project's editorial asset preset is:

- `images/cover.png`: 900x383 WeChat cover image.
- `images/inline-01.png`, `images/inline-02.png`, etc.: paragraph-width inline images, usually close to 900px wide.
- `images/table-01.png`, `images/table-02.png`, etc.: image-based tables when the article needs comparisons, matrices, parameters, or factual checklists.

Types:

- Data chart.
- Structure diagram.
- Realistic site/factory/equipment image.
- Process infographic.
- Image-based editorial table.

## Internal Prompt Shape

Keep prompts internal during one-step publishing unless the user asks to inspect them. Use this structure when calling the image tool:

```text
Model: gpt-image-2
Use case: editorial WeChat cover or inline image
Asset type: <cover / inline image / image-based table / data chart / structure diagram / realistic equipment scene / process infographic>
Topic: <topic>
Core judgment: <one-sentence judgment>
Placement: <cover or section name>
Information point: <what the image must explain>
Scene or structure: <concrete visual description>
Style: mandatory editorial reference to The New York Times, The Economist, and Bloomberg visual languages; restrained, sharp, high-end, institutional, data-aware, never stock-like
Composition: <900x383 cover or paragraph-width inline>, clean focal point, public-account friendly
Constraints: no text overlays unless exact short Chinese labels are required, no logo, no watermark, no fake UI, no impossible machinery
Recovery plan: if any text/table/chart detail is unreadable, simplify the content and regenerate through the built-in image tool only
```

## Generation Reliability Harness

Before calling the image tool:

1. Write a one-sentence information point for the image.
2. Remove decorative or secondary content that does not serve that information point.
3. Keep text to short labels only. Put exact numbers, source notes, caveats, and long explanations in the article body or caption.
4. For tables, keep each generated table image small: no dense footnotes, no crowded cells, and no more columns or rows than can remain readable on mobile. Split large tables into multiple `table-0N.png` assets.
5. For diagrams, keep three to five nodes and avoid long arrows, tiny labels, and multi-layer nested structures.
6. If a generated result fails readability, revise the spec to be simpler and regenerate or edit through the built-in image capability.
7. Do not use local Python, PIL, matplotlib, SVG, canvas, browser screenshots, or other programmatic rendering to create final image assets.

## Cover Guidance

- The project's cover preset is 900x383; this is an editorial convention, not a verified universal platform rule.
- The cover must communicate the article's main judgment by itself. It should not merely show an industry-related object.
- Use credible, concrete industrial/research/social scenes rather than generic technology glow.
- Every generated image must visibly reference mainstream editorial styles associated with The New York Times, The Economist, and Bloomberg: strong composition, restrained palette, intelligent metaphor, high contrast, clear hierarchy, institutional polish.
- Keep the subject readable at thumbnail size.
- Avoid long text in the generated image. Short, exact Chinese text may be used only when it helps the cover state the judgment. Put the full title in WeChat, not inside the bitmap, unless the user explicitly asks for text.

## Inline Guidance

- Keep inline image width aligned with or close to the paragraph width. Prefer around 900px wide when generating raster assets.
- Use landscape or gentle portrait ratios only when the section needs them; avoid tiny square images that feel detached from the text flow.
- For diagrams, use no more than three to five main nodes.
- For data visuals, prefer conceptual charts when exact data is not verified.
- For equipment or factory scenes, keep details plausible and do not imply a specific company unless sourced.
- If generated images include unwanted text, regenerate or edit through the built-in image generation capability before publishing.

## Table Image Guidance

- Do not place complex Markdown pipe tables in final WeChat articles.
- For comparisons, parameter matrices, conclusion grids, and factual checklists, generate a table image such as `table-01.png`.
- Keep table images editorial and readable: clear title, aligned columns, high contrast, restrained colors, and enough padding for mobile reading.
- Use short Chinese labels. If the table contains exact numbers, verify them before image generation and keep sources in the article notes or surrounding text.
- If the planned table is too dense for built-in image generation, simplify it before generation: split it, reduce columns, turn rows into grouped comparison cards, or move exact details into body text/captions.
- Insert table images with a short caption in Markdown. Do not rely on WeChat preserving HTML table layout.

## File Handling

After generation:

1. Save the final image files under the article output directory.
2. Treat the images shown or selected in the conversation as the canonical assets. Copy those files into the output folder; do not overwrite them with locally redrawn diagrams, simplified substitutes, or lower-quality placeholders for convenience.
3. Only substitute a generated asset when it is unusable for publication, such as broken text, obvious artifacts, bad crop, or unreadable table content. Regenerate or edit it only through the built-in image generation capability. Do not use deterministic local drawing, layout, rendering, SVG, canvas, PIL, matplotlib, or similar local workflows as a table/image fallback.
4. Use stable filenames: `cover.png`, `inline-01.png`, `inline-02.png`, `table-01.png`, `table-02.png`.
5. Insert local image paths into `article.md` at the correct section.
6. Ensure the cover is 900x383 before publishing. If the generated asset has the wrong dimensions, regenerate or edit it through the built-in image generation capability.
7. Ensure inline images align with or are close to paragraph width in the final WeChat layout.
