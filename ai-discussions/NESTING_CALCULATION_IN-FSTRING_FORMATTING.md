User: In line 377 (as an example), I am trying to nest calculations within an f-string. Currently I want to make an expression that rounds that entire result by ':2f' at the end, and not just rounding the '1000000' operand.

GitHub Copilot: I'll check line 377 of your file to see the current expression: 

Read [](file:///Users/ethanayestaran/GitHubRepositories/School/Computing/U4-Practical-Programming-Set-Assignment/Prototype.py#370-370), lines 370 to 385

I can see the issue. In line 377, you have the multiplication `*1000000:.2f`, which means the format specifier only applies to the `1000000` value. 

To apply the rounding to the **entire result** of the calculation, wrap the full expression in parentheses:

```python
{(linear_search(items, target, hidden=True, request="time")*1000000):.2f}
```

The parentheses ensure the format specifier applies to the complete expression `linear_search(...)*1000000`, not just the operand.

This applies to all four similar lines you have (lines 377–380). Would you like me to update all of them with the correct syntax?You've used 84% of your session rate limit. Your session rate limit will reset on 25 April at 1:44. [Learn More](https://aka.ms/github-copilot-rate-limit-error)

User: Thank you!

GitHub Copilot: You're welcome! Good luck with your assignment. 🎯You've used 85% of your session rate limit. Your session rate limit will reset on 25 April at 1:44. [Learn More](https://aka.ms/github-copilot-rate-limit-error)