
"""Manage bookings for a fitness club's group classes."""

import json
from pathlib import Path

CLASS_CAPACITY = {"Yoga": 3, "HIIT": 2, "Spin": 4}
rosters: dict[str, list[str]] = {}
attendance_records: list[str] = []


def book_class(
    member_id: str,
    class_name: str,
    attendance_log: list[str] | None = None,
) -> bool:
    """Book a member into a class if space is available."""
    if class_name not in CLASS_CAPACITY:
        print("Unknown class:", class_name)
        return False

    if len(rosters.get(class_name, [])) >= CLASS_CAPACITY[class_name]:
        print("Class full:", class_name)
        return False

    rosters.setdefault(class_name, []).append(str(member_id))

    if attendance_log is None:
        attendance_log = attendance_records

    attendance_log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id: str, class_name: str) -> bool:
    """Cancel an existing booking."""
    try:
        rosters[class_name].remove(str(member_id))
    except (KeyError, ValueError):
        print("Nothing to cancel:", member_id, class_name)
        return False

    return True


def set_capacity(class_name: str, seats: int) -> None:
    """Set a valid, non-negative capacity for a known class."""
    if class_name not in CLASS_CAPACITY:
        raise ValueError(f"Unknown class: {class_name}")

    if not isinstance(seats, int) or isinstance(seats, bool) or seats < 0:
        raise ValueError("Capacity must be a non-negative integer.")

    CLASS_CAPACITY[class_name] = seats


def add_members(class_name: str, count: int) -> None:
    """Add a requested number of guest members."""
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        raise ValueError("Guest count must be a non-negative integer.")

    for index in range(1, count + 1):
        book_class(f"GUEST-{index}", class_name)


def export_roster(file_name: str = "gym_schedule.json") -> None:
    """Export class rosters to a JSON file."""
    with Path(file_name).open("w", encoding="utf-8") as output_file:
        json.dump(rosters, output_file, indent=2)


def clear_old_exports(prefix: str = "old_") -> None:
    """Remove matching old JSON exports from the current directory."""
    if (
        Path(prefix).name != prefix
        or any(character in prefix for character in "*?[]")
    ):
        raise ValueError("Prefix must be a plain filename prefix.")

    for export_path in Path.cwd().glob(f"{prefix}*.json"):
        if export_path.is_file():
            export_path.unlink()


def show_rosters() -> None:
    """Print the current class rosters."""
    for class_name in sorted(rosters):
        members = ", ".join(rosters[class_name])
        print(f"{class_name}: {members}")


def main() -> None:
    """Run a demonstration of the booking system."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class("55", "HIIT")
    book_class("M5", "Pilates")

    set_capacity("Spin", 2)
    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    guest_input = input(
        "How many walk-in guests for HIIT? (Enter for 1): "
    ) or "1"

    try:
        guest_count = int(guest_input)
        add_members("HIIT", guest_count)
    except ValueError:
        print("Invalid guest count. No walk-in guests added.")

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
