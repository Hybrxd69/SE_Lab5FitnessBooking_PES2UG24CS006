
# Reflection: Static Code Analysis

## 1. Why is static code analysis useful?

Static code analysis identifies potential defects, security weaknesses,
and style problems without requiring the program to execute every path.
It helps developers discover issues early and maintain more readable code.

## 2. What issues were found in the original program?

The original program contained an incorrect class-capacity comparison,
a mutable default argument, a broad exception handler, unmanaged file
handling, and an unsafe shell command. It also lacked proper validation
for class names and capacity values.

## 3. How were the issues fixed?

The capacity check was corrected, input validation was added, and the
mutable default argument was removed. Exception handling was narrowed,
file operations were managed with a context manager, and file deletion
was implemented with pathlib instead of a shell command.

## 4. What did the analysis tools contribute?

Pylint helped assess code quality and maintainability. Bandit checked
for common security weaknesses, while Flake8 identified style violations.
Running the tools again after changes helped verify the improvements
and identify any remaining issues.
