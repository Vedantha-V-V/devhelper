import html
import importlib
import re
from pathlib import Path

from flask import Flask, abort, render_template


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab"
LAB_FILE_PATTERN = re.compile(r"^Lab(\d+)\.md$", re.IGNORECASE)
COURSE_ALIASES = {
    "docker": "docker",
    "nextgendb": "nextgendb"
}


def extract_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def extract_preview(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        return stripped[:180]
    return "No content added yet."


def normalize_course(course: str) -> str | None:
    return COURSE_ALIASES.get(course.lower())


def display_course_name(course: str) -> str:
    if course == "nextgendb":
        return "NextGen DB"
    return course.capitalize()


def render_markdown(markdown_text: str) -> str:
    if not markdown_text.strip():
        return "<p>This file is empty.</p>"

    try:
        markdown_module = importlib.import_module("markdown")
    except ModuleNotFoundError:
        escaped = html.escape(markdown_text)
        return (
            "<div class='notice'>Install <code>markdown</code> for rich rendering: "
            "<code>pip install markdown</code>.</div>"
            f"<pre>{escaped}</pre>"
        )

    return markdown_module.markdown(
        markdown_text,
        extensions=["fenced_code", "tables", "sane_lists"],
    )


def load_labs() -> list[dict]:
    labs = []
    if not LAB_DIR.exists():
        return labs

    for path in sorted(LAB_DIR.glob("*/*.md")):
        raw = path.read_text(encoding="utf-8")
        course_slug = path.parent.name
        match = LAB_FILE_PATTERN.match(path.name)

        if match:
            lab_id = match.group(1)
            default_title = f"Lab {lab_id}"
        else:
            lab_id = path.stem.lower().replace("_", "-")
            default_title = path.stem.replace("_", " ")

        labs.append(
            {
                "id": lab_id,
                "course": course_slug,
                "course_label": display_course_name(course_slug),
                "file_name": path.name,
                "title": extract_title(raw, default_title),
                "preview": extract_preview(raw),
                "raw": raw,
                "html": render_markdown(raw),
            }
        )

    return labs


@app.route("/")
def home():
    return render_template("index.html", labs=load_labs())


@app.route("/courses/<course>")
def course_home(course: str):
    normalized_course = normalize_course(course)
    if normalized_course is None:
        abort(404)

    labs = [lab for lab in load_labs() if lab["course"] == normalized_course]
    return render_template("index.html", labs=labs)


@app.route("/courses/<course>/labs/<lab_id>")
def lab_detail(course: str, lab_id: str):
    normalized_course = normalize_course(course)
    if normalized_course is None:
        abort(404)

    labs = load_labs()
    selected = next(
        (lab for lab in labs if lab["course"] == normalized_course and lab["id"] == lab_id),
        None,
    )
    if selected is None:
        abort(404)
    return render_template("article.html", lab=selected)


@app.route("/labs/<lab_id>")
def legacy_lab_detail(lab_id: str):
    labs = load_labs()
    selected = next((lab for lab in labs if lab["id"] == lab_id), None)
    if selected is None:
        abort(404)
    return render_template("article.html", lab=selected)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

