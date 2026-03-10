import json
from pathlib import Path


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_required_fields(data, required_fields, label):
    missing = [field for field in required_fields if field not in data]
    if missing:
        print(f"[FAIL] {label} missing fields: {', '.join(missing)}")
        return False
    print(f"[OK] {label} contains required fields.")
    return True


def main():
    base = Path(__file__).resolve().parent.parent / "registry"

    student_file = base / "student-record-example.json"
    course_file = base / "course-record-example.json"

    student_required = [
        "student_id",
        "name",
        "pathway",
        "status",
        "watch_hours_completed",
        "books_completed",
        "reflections_completed",
        "projects_completed",
        "last_updated",
    ]

    course_required = [
        "course_id",
        "title",
        "pathway",
        "playlist_hours_required",
        "books_required",
        "reflections_required",
        "final_assessment_required",
        "level",
        "status",
    ]

    student_data = load_json(student_file)
    course_data = load_json(course_file)

    ok_student = validate_required_fields(student_data, student_required, "student record")
    ok_course = validate_required_fields(course_data, course_required, "course record")

    if ok_student and ok_course:
        print("Validation complete: registry examples passed.")
    else:
        raise SystemExit("Validation failed.")


if __name__ == "__main__":
    main()