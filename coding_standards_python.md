# Python Coding Standards
Unless otherwise stated, code must comply with [PEP 8](https://www.python.org/dev/peps/pep-0008/). Our Python repositories generally enforce this with tools such as pycodestyle.

Python repositories may supplement these coding standards with guidelines specific to their project.

## Line Length
Limit lines to a maximum of 99 characters. While it is encouraged to wrap comments and docstrings at 72 characters, it is not strictly enforced. 

## Type Annotations
The use of type annotations is strongly encouraged, especially in new code. For some repositories, such as autograder-sandbox, type annotations are required and enforced using mypy's strict mode. In other cases, such as autograder-server, the heavy use of libraries such as Django limits mypy's effectiveness. For that repository, we intend to incrementally add type annotations.

## Misc
- Avoid acronyms or initialisms other than the ones listed below:
    - "pk" = "primary key"
    - "ag" = "autograder"
    - "hg" = "handgrading"
    - "pg" = "postgres"
- Avoid arbitrary abbreviations. Shortening long, frequently used words can be ok,
especially in more local contexts. 
    - e.g. "conf" or "config" instead of "configuration" is ok
    - e.g. "fdbk" instead of "feedback" is ok
- Don't use \ to wrap lines (except in `with`-statements). Use parentheses instead.
- Use a single leading underscore for non-public names.
- When a closing brace, bracket, or parenthesis is on its own line, align
it with the first character of the line that starts the multiline construct:
```
my_list = [
    'spam',
    'egg',
    'waluigi,
]
```
- When using a hanging indent for a multiline `if` condition, indent an extra level:
```
if (spam_spam_wonderful_spam
        and egg and waluigi):
    print('waaaaluigi')
```
- Put line breaks before binary operators:
```
# Source: https://www.python.org/dev/peps/pep-0008/#id20
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```
