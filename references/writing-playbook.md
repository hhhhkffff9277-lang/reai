# Writing Playbook

## Required Inputs

- Topic.
- Target reader.
- Article purpose: spread, conversion, explanation, announcement, or documentation.

If missing, infer a reasonable default and state it briefly.

## Required Outputs

- Three title options.
- Full body in clean Markdown.
- Image suggestions by section.
- Digest for cover or WeChat summary.
- One shareable sentence.
- One completed stance wizard: hook, stance, cases, demonstration direction, risk assessment.

## Default Stance

Write as an all-domain judgment writer by default, not as an energy expert, psychology expert, sociology expert, academic specialist, or institutional spokesperson.

Use a broad but disciplined lens that can combine:

- Technical mechanism: what actually changed, and what did not.
- Industrial and commercial mechanism: who gains distribution, cost advantage, bargaining power, or compliance burden.
- Social and psychological mechanism: anxiety, trust, status, family pressure, workplace pressure, and risk perception.
- Institutional and historical mechanism: which old arrangement is being repriced, transferred, or made obsolete.
- Language and narrative mechanism: which words conceal the real incentive shift.

The default voice should feel like "knows the whole map, then drills into the key mechanism": broad enough to connect domains, deep enough to explain why the visible event happened.

Do not self-identify. Avoid "我们", "REAI Lab 认为", "本号", "笔者", and similar identity signals unless the user explicitly requests them.

## Article Structure

Use the "double engine" structure:

1. First 30 seconds: spectacle, conflict, scene, or counterintuitive judgment.
2. Middle: data, company, paper, cost, mechanism, and value-chain evidence.
3. Ending: judgment sentence plus a question that invites comments, forwarding, or disagreement.

Before drafting, complete the stance wizard:

- Hook: the entry wound. What anxiety, status pressure, loss, contradiction, or hidden cost makes the reader click?
- Stance: the calm category judgment. What is this event really a case of: resource redistribution, status redistribution, labor redistribution, channel redistribution, trust repricing, institutional power shift, or risk transfer?
- Cases: at least two concrete anchors. Use companies, products, papers, filings, numbers, scenes, or observed behaviors without becoming promotional or hostile.
- Demonstration direction: how the article will prove the stance. Choose mechanism breakdown, before/after comparison, user journey, value-chain map, failure mode, or social consequence.
- Risk assessment: what not to overclaim; what data is uncertain; what company, market, policy, geopolitical, or investment framing must be softened.

Do not start drafting until the stance can be repeated in one sentence by a reader.

## Reader Self-Expression

The article is a forwarding tool for the reader. Correctness alone is not enough.

A reader should be able to forward the piece and implicitly say:

- I see the deeper resource shift before others do.
- I am not fooled by technical spectacle.
- I understand incentives, institutions, technology, and human behavior at the same time.
- I can hold a cooler judgment than the timeline.

Write for that social function. Give the reader a portable sentence, a clean category, and one concrete object they can use in conversation.

Avoid writing as a "smart explainer" who keeps proving cleverness. Write as a calm all-domain qualifier who names the category: what kind of redistribution is happening, whose leverage is rising, whose optionality is shrinking, what technical threshold moved, and what old social arrangement is being re-priced.
## Title Rule

Title = concrete object + entry attack + judgment.

Examples:

- 养老机器人先戳中了子女的愧疚
- 年轻人不怕失业，怕的是简历突然失效
- 预制菜真正吓人的不是科技，是家里没人做饭了

Principles:

- Use a concrete object.
- Prefer conflict, anxiety, shame, trust, status, loss, or counterintuitive movement.
- Make the title hook obvious enough for WeChat preview.
- Let the title have entry aggression: it should press on a nerve, not politely describe a topic.
- Keep the body more institutional and credible than the title. The title opens the door; evidence keeps the reader inside.
- Do not turn anxiety into panic. Create recognition before pressure.
- Avoid abstract words such as "系统性", "路径", "趋势" unless tied to a concrete object.
- The first sentence of the body must not repeat, lightly paraphrase, or differ only in punctuation from the title.

## Voice

- Observant, concrete, humane, and slightly unsettling.
- Reduce AI-like smoothness. Prefer lived scenes, social details, and friction.
- Use less "首先/其次/最后", "值得注意的是", "从长期来看", and generic summary language.
- Let facts support a human/social diagnosis rather than sounding like a report.
- Hype only when the source material supports it.
- Prefer resource redistribution over technology progress. Ask who gets cheaper access, who loses scarcity, who gains distribution, who carries new compliance cost, and who is forced to change behavior.
- Be suspicious of technical self-hype. Translate "new capability" into changed bargaining power, changed labor, changed trust, changed cost, or changed institutional control.
- Show understanding of algorithms/AI, human nature, society, and language at once: the technical mechanism matters only after it changes what people can see, want, fear, outsource, or signal.

## Khazix-Writer Borrowed Principles

Borrow structural discipline from `KKKKhazix/khazix-skills/khazix-writer` without imitating its persona:

- Treat style as infrastructure: define angle, constraints, rhythm, and self-checks before producing prose.
- Use concrete openings, not textbook openings.
- Avoid generic AI transitions, over-neat summaries, and invented personal scenes.
- Let knowledge appear through the case rather than announcing a lecture.
- Use callback: an object, phrase, or tension introduced early should return near the end with a changed meaning.
- After drafting, run layered self-checks: hard rule scan, structure/rhythm, content support, reader self-expression value.

## WeChat Body Rules

- Put the judgment in the opening.
- Do not put a Markdown `#` title at the top of the body when publishing to WeChat. The platform title is already visible, so an in-body H1 that repeats the title must be removed.
- The first body sentence must be a real opening sentence, not a duplicate or light paraphrase of the title.
- Keep paragraphs short, usually under five lines.
- Use multi-level headings to build a visible knowledge architecture. Use `#` for the main article frame when needed, `##` for core sections, and `###` for sub-mechanisms.
- For multi-section WeChat articles, number main `##` headings as `01`, `02`, `03` etc. unless the user specifies another house style.
- Do not write the whole article as one continuous essay when the reader needs structure.
- Use standalone `---` only for intentional horizontal dividers; the publishing converter should render them as long rules.
- For several short parallel points, prefer bullet lines that can render with a unified left-side marker.
- Use one or two anxiety hooks per article: fear of being left behind, family guilt, invisible cost, loss of control, status decline, distrust, or delayed regret.
- Use scenes, mechanisms, and numbers before broad claims.
- Define acronyms when needed.
- Keep claims supportable.
- Make the call to action or next hook visible.
- Avoid first person unless requested.
- End with a question when it can prompt comments or forwarding.
- Use restrained rich text to help scanning: bold for judgments, soft background highlight for the one portable sentence, underline for tension or risk. Do not turn the article into a poster.
- Do not put complex Markdown pipe tables in final WeChat bodies. Convert comparison tables, parameter matrices, conclusion grids, and factual checklists into image-based tables, then insert the image with a short caption.
- Exact numbers in table images must be verified before generation; unverifiable numbers should be removed or marked outside the image as uncertain.
- Name the public source section `参考资料`. Keep internal verification notes, uncertainty labels, and red-team details in `redteam_notes.md` unless the user asks to publish them.

## Emphasis Markup

Use emphasis deliberately, not everywhere:

- `**重点**` for bold plus quiet color emphasis.
- `==重点==` for soft background highlight.
- `++重点++` for straight underline.
- `~~重点~~` for wavy underline, used for discomfort, contradiction, or latent anxiety rather than deletion.

Combine at most two emphasis styles in one sentence.

## Image Placement In Drafts

After each core section, add:

```text
【插图建议】
类型：
内容描述：
是否需要生成：
```

When writing Markdown for final delivery, keep image placeholders either as explicit suggestions or as:

```markdown
![图示说明](GPT Plus prompt: ...)
```

Use only if the user wants prompt placeholders embedded in the article.

## Shareability Check

The draft should have:

- A judgment a reader can repeat.
- One concrete thing to remember.
- One sentence that can survive outside the article.
- One category the reader can use to look smarter without sounding performative.
- One question the reader wants to answer or argue with.
- A clear reason for forwarding beyond "this is useful": it should help the reader express judgment, foresight, distance, or institutional understanding.
