from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANDATORY = [
    "## 1. What is it?", "## 2. Why does it matter?", "## 3. How does it work?",
    "## 4. Example", "## 5. Production Use Case", "## 6. Common Problems",
    "## 7. Trade-offs", "## 8. Interview Questions", "## 9. Senior-level Questions",
    "## 10. Short Answers", "## 11. Follow-up Questions", "## 12. Key Takeaways",
]
EXEMPT_DIRS = {"00-interview-roadmap", "22-mock-interview", "23-cheatsheets"}
errors: list[str] = []
files = sorted(ROOT.rglob("*.md"))
python_blocks = 0
mermaid_blocks = 0

if not files:
    errors.append("No Markdown files found")

for path in files:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if not text.strip():
        errors.append(f"Empty file: {rel}")
    if re.search(r"\b(?:TODO|TBD|FIXME)\b", text, flags=re.I):
        errors.append(f"Placeholder marker: {rel}")
    if path.name != "README.md" and rel.parts[0] not in EXEMPT_DIRS:
        missing = [heading for heading in MANDATORY if heading not in text]
        if missing:
            errors.append(f"Missing mandatory sections in {rel}: {', '.join(missing)}")
        counts = {kind: len(re.findall(rf"\*\*{kind}\d+\.\*\*", text)) for kind in ("B", "L", "S", "F")}
        expected = {"B": 10, "L": 10, "S": 5, "F": 5}
        for kind, minimum in expected.items():
            if counts[kind] < minimum:
                errors.append(f"Too few {kind} questions in {rel}: {counts[kind]} < {minimum}")
    if text.count("```mermaid") > text.count("```") // 2:
        errors.append(f"Unbalanced Mermaid fence: {rel}")

    for number, code in enumerate(re.findall(r"```python\n(.*?)\n```", text, flags=re.S), 1):
        python_blocks += 1
        try:
            ast.parse(code)
        except SyntaxError as exc:
            errors.append(f"Invalid Python block {number} in {rel}: {exc}")

    for number, diagram in enumerate(re.findall(r"```mermaid\n(.*?)\n```", text, flags=re.S), 1):
        mermaid_blocks += 1
        first_line = next((line.strip() for line in diagram.splitlines() if line.strip()), "")
        if not re.match(r"^(?:flowchart|sequenceDiagram|graph|stateDiagram|erDiagram|gantt|timeline)\b", first_line):
            errors.append(f"Unknown Mermaid diagram type {number} in {rel}: {first_line}")

    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"Broken link in {rel}: {target}")

design_requirements = [
    "### Requirements", "### Functional Requirements", "### Non-functional Requirements",
    "### Scale Estimation", "### API", "### Data Model", "### High-level Architecture",
    "### Database", "### Cache", "### Message Queue", "### Storage", "### Scaling",
    "### Failure Handling", "### Security", "### Observability", "### Bottlenecks",
    "### Future Improvements", "```mermaid",
]
design_files = sorted((ROOT / "11-system-design").glob("design-*.md"))
if len(design_files) < 10:
    errors.append(f"Need at least 10 design files, found {len(design_files)}")
for path in design_files:
    text = path.read_text(encoding="utf-8")
    missing = [item for item in design_requirements if item not in text]
    if missing:
        errors.append(f"Incomplete system design {path.name}: {', '.join(missing)}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Total markdown files: {len(files)}")
print(f"System design exercises: {len(design_files)}")
print(f"Python fenced blocks parsed: {python_blocks}")
print(f"Mermaid blocks structurally checked: {mermaid_blocks}")
print("Empty files: 0")
print("Broken local Markdown links: 0")
print("Placeholder markers: 0")
