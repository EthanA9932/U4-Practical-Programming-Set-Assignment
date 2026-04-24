User: In Line 95, the data is expected to be of 6 digits long, with the first four being between a year range of 2000 to 2026 inclusive, and the week range of 01 to 52 inclusive. Is there a way to compress all of these checks into one line of code within the if argument?

GitHub Copilot: Reviewing the relevant section around the year/week validation so I can provide a concise single-line check.

Read [](file:///Users/ethanayestaran/GitHubRepositories/School/Computing/U4-Practical-Programming-Set-Assignment/Prototype.py#70-70), lines 70 to 105

Yes — you can compress it into one `if` using string checks plus integer ranges, for example:

```python
if len(i[2]) == 6 \
   and i[2].isdigit() \
   and 2000 <= int(i[2][:4]) <= 2026 \
   and 1 <= int(i[2][4:]) <= 52:
    year_week_check = True
else:
    year_week_check = False
```

That does all of these in one condition:
- six characters
- all digits
- year between `2000` and `2026`
- week between `01` and `52`

> Note: since `hotdog_data` comes from `line.strip().split(",")`, `i[2]` is a string, so `isinstance(i[2], int)` is not appropriate here.

User: Thank you!

GitHub Copilot: You're welcome!