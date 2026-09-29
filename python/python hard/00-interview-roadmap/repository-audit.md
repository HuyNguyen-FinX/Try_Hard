# Repository Depth Audit

## Audit baseline before this expansion

- Markdown files audited: **270**.
- P0/P1 technical files sampled systematically: **103**.
- P0/P1 files under 800 words: **0**, nhưng chiều dài chủ yếu đến từ question template.
- P0/P1 files without Mermaid: **92**.
- System Design labs with fewer than five diagrams: **11/11**.
- Main issue: definition/checklist có nhưng internals, data flow, failure propagation, debugging và architecture evolution chưa đủ sâu.

## Audit after expansion

- Total Markdown files: **273** (bao gồm audit này).
- Deep-dive files with Mental Model/Internals/Flow/Failure/Debugging: **161**.
- Mermaid diagrams: **228** trước khi cộng audit (audit không thêm diagram).
- P0 files under 800 words: **0**.
- P0 files without Mermaid: **0**.
- System Design labs: **11**, diagram count mỗi bài: **6–6**.

## Checks performed

- Mandatory 12-section structure và question counts.
- P0 depth sections: Mental Model, Internals, flow diagram, failure, debugging, misconceptions, when-not-to-use, interview chain, exercises, cross-links.
- System Design: high-level, sequence, data/source-of-truth, scaling, failure/recovery, observability, evolution, security và walkthrough.
- Local Markdown links, empty files, placeholder marker, exact duplicate file, Python fenced-code syntax và Mermaid structure/render.

## Remaining shallow files

Không còn P0 file dưới 800 words.

## Remaining P0 files without diagrams

Không còn P0 file thiếu Mermaid diagram.

Audit script tái chạy tại [`scripts/validate.py`](../scripts/validate.py). Báo cáo này mô tả structural/depth coverage; technical accuracy vẫn phải được kiểm theo version-specific official references trong [Technical References](../24-references/README.md).
