User: In the analysis fie, I have outputs from the main program. The first four are variables retrieved from an algorithm that is executed earlier in the main program. It would make sense if none of these four variables changed from the initial assignment of 0, but why does only the first one work?

GitHub Copilot: ## Why only the first variable updates

In `Prototype.py`, the `filter_scraper` function uses the global `file` object:

- `file = open("hotdogs.txt", "r")`
- `def filter_scraper(...):`
- `    for line in file:`

That means the file is read sequentially each time `filter_scraper` is called.

### What happens

- `v_hotdogs = filter_scraper(4, search_query, hotdog_data, hidden=True)` reads `file` from the start and consumes the whole file.
- After that call, the file pointer is at the end-of-file.
- The next calls:
  - `m_hotdogs = filter_scraper(5, ...)`
  - `onions = filter_scraper(6, ...)`
  - `ketchup = filter_scraper(7, ...)`
  all iterate the same `file`, but now there is nothing left to read.
- So they return empty lists, and their totals stay at `0`.

### Why the first one “works”

Only the first call sees the actual file contents because it is the first time the file is iterated. Later calls see an already-exhausted file handle.

### Additional bug to note

`filter_scraper` has a `data` parameter, but it never uses it:

```python
def filter_scraper(target_filter, vendor_name, data, hidden):
    ...
    for line in file:
```

So even though you pass `hotdog_data`, the function ignores it. That makes the logic fragile.

### Fix idea

Either:

- reopen/reset the file inside `filter_scraper` each time, or
- use `data` and iterate over `hotdog_data` instead of `file`

For example:

```python
def filter_scraper(target_filter, vendor_name, data, hidden):
    items = []
    for line in data:
        ...
```

That will make all four variables calculate correctly.

User: Thank you for the correction!

GitHub Copilot: You're welcome! If you want, I can also help clean up the rest of `Prototype.py` so the data flow is more reliable.