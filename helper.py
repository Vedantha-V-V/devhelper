#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


STEP_PATTERN = re.compile(r"^##\s*Step\s+(\d+)\s*[:\-]?\s*(.*)$", re.IGNORECASE)


def parse_steps(markdown_text: str) -> dict[int, str]:
	lines = markdown_text.splitlines()
	steps: dict[int, str] = {}
	current_step = None
	buffer: list[str] = []

	for line in lines:
		match = STEP_PATTERN.match(line.strip())
		if match:
			if current_step is not None:
				steps[current_step] = "\n".join(buffer).strip()

			current_step = int(match.group(1))
			buffer = [line]
			continue

		if current_step is not None:
			buffer.append(line)

	if current_step is not None:
		steps[current_step] = "\n".join(buffer).strip()

	return steps


def get_lab_file(lab_number: int) -> Path:
	base_dir = Path(__file__).resolve().parent
	return base_dir / "lab" / f"Lab{lab_number}.md"


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Print a specific step from a lab markdown file.",
	)
	parser.add_argument("--lab", type=int, required=True, help="Lab number, for example: 1")
	parser.add_argument("--step", type=int, required=True, help="Step number, for example: 2")
	args = parser.parse_args()

	lab_path = get_lab_file(args.lab)
	if not lab_path.exists():
		raise SystemExit(f"Lab file not found: {lab_path}")

	markdown_text = lab_path.read_text(encoding="utf-8")
	steps = parse_steps(markdown_text)

	if args.step not in steps:
		available = ", ".join(str(number) for number in sorted(steps.keys())) or "none"
		raise SystemExit(f"Step {args.step} not found in Lab {args.lab}. Available steps: {available}")

	print(steps[args.step])


if __name__ == "__main__":
	main()