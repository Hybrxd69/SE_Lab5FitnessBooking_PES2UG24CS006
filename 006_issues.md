
# Static Code Analysis: Issues and Fixes

The original program was reviewed for correctness, maintainability,
style, and security. The following issues were identified and addressed.

| Issue | Type | Line(s) in Original File | Description | Fix Approach |
|---|---|---|---|---|
| Incorrect capacity check | Correctness | 9 | The original comparison allowed a booking beyond the configured capacity. | Changed the check to reject bookings when the current roster reaches capacity. |
| Mutable default argument | Correctness | 7 | The default attendance list was shared between function calls. | Replaced the mutable default with `None` and used an explicit attendance list. |
| Broad exception handler | Maintainability | 19-20 | A bare `except` could hide unrelated errors. | Caught only `KeyError` and `ValueError`. |
| Unsafe shell command | Security | 30 | `os.system` constructed a shell command for deleting files. | Used `pathlib` to locate and remove matching JSON exports. |
| Unmanaged file handle | Reliability | 27-28 | The JSON export file was opened without a context manager. | Used `Path.open` inside a `with` statement. |
| Invalid class and capacity handling | Correctness | 23-25, 40-43 | Unknown classes and negative capacities could lead to invalid booking behavior. | Added class validation and rejected invalid capacities. |
| Inconsistent naming | Style | 22 | `addMembers` did not follow the standard Python snake_case naming convention. | Renamed the function to `add_members`. |
| Unsafe import behavior | Maintainability | Final line | The original program ran the demonstration whenever imported. | Added the `if __name__ == "__main__":` guard. |

## Validation

The updated application was checked with Pylint, Bandit, and Flake8.
The corresponding reports are included with the submission.
