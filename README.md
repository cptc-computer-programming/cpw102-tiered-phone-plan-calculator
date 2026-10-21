# Tiered Phone Plan Calculator

The phone provider is introducing premium membership and new overage rates. Extend your completed [Phone Data Bill Calculator lab](https://github.com/cptc-computer-programming/cpw102-phone-bill-calculator) so customers can understand their bill under the new pricing policy.

Before beginning, follow [GITHUB_SETUP.md](GITHUB_SETUP.md).

## Learning Goals

- Extend an existing program while preserving behavior that still applies.
- Use `if-elif-else` and nested decisions to select a rate.
- Convert a text response into a Boolean value.
- Use function parameters and returned values in calculations and decisions.
- Combine conditions with logical operators.
- Test boundaries and compare results when one input changes.

## Start from Your Lab

> [!IMPORTANT]
> Copy your completed lab program from `03_execution/data_bill.py` into this repository's `data_bill.py`. The supplied file is blank.

- Retain your data usage and base-cost inputs, Boolean-returning data limit check, and within-limit, moderate, and high usage messages.
- Continue using the data limit function's result in a decision.
- Replace the fixed overage rate with the new pricing rules below.

## New Pricing Policy

The plan still includes 10 GB. Ask whether the customer has premium membership in addition to their data usage and base plan cost.

| Total data used | Regular overage rate | Premium overage rate |
| --- | --- | --- |
| 10 GB or less | No overage charge | No overage charge |
| More than 10 GB, up to and including 20 GB | $2 per GB over the data limit | $1 per GB over the data limit |
| More than 20 GB | $3 per GB over the data limit | $2 per GB over the data limit |

> [!IMPORTANT]
> The selected rate applies to **all GB beyond the 10 GB data limit**, not just the portion in a particular tier. For example, a regular customer using 25 GB pays for 15 overage GB at $3 each.

> [!NOTE]
> Keep the lab's usage categories: up to 5 extra GB is moderate; more than 5 extra GB is high. These message categories are separate from the pricing tiers.

Recommend considering premium membership only when a regular customer exceeds the data limit. Do not add a membership fee or discount beyond the rates shown above.

## Implementation Requirements

- Use an `if-elif-else` structure to handle the three usage tiers.
- Use a nested decision within a pricing tier to select the regular or premium rate.
- Store premium membership as a Boolean variable. Accept `yes` or `no` regardless of capitalization or surrounding spaces.
- Define and call a function that accepts data usage and premium status and returns the applicable overage rate. Return zero when there is no overage. This function should return a number rather than print it.
- Keep and use your Boolean-returning data limit function from the lab.
- Use logical operators to combine membership and overage status in the recommendation decision.
- Store the selected rate and overage amount in variables, then calculate the overage cost and total bill after selecting the rate.

You choose the function and variable names, prompts, and output layout.

## Input Assumptions

Data usage and base cost will be numeric. The membership response will be `yes` or `no`, possibly with different capitalization or surrounding spaces. You do not need to validate other input or prompt repeatedly.

## Output

Display the usage message, GB over the data limit, overage cost, and total monthly bill. Display the applicable rate when there is overage and the premium recommendation when its conditions are met. Show money amounts to two decimal places.

### Example: Within the Data Limit

```text
Enter data used (GB): 8
Enter base monthly plan cost: 40
Do you have premium membership? (yes or no): no

You are within your data limit.
GB over limit: 0.0
Overage cost: $0.00
Total bill: $40.00
```

### Example: Regular Customer with High Usage

```text
Enter data used (GB): 25
Enter base monthly plan cost: 40
Do you have premium membership? (yes or no): no

You are 15.0 GB over your limit.
High extra usage.
Overage rate: $3.00 per GB
Overage cost: $45.00
Total bill: $85.00
Consider premium membership to reduce your overage rate.
```

Your wording and spacing do not need to match the examples exactly.

## Testing

Run your program from the repository folder:

```text
python data_bill.py
```

Reuse the lab cases for 10 GB with a $40 base cost, 15 GB with a $40 base cost, and 15.5 GB with a $50 base cost. Use `no` for premium membership and recalculate the expected bills under the new policy. Also test:

| Data used (GB) | Base cost | Premium response | Focus |
| --- | --- | --- | --- |
| 20 | 40 | `no` | Upper boundary of the middle pricing tier |
| 20 | 40 | `yes` | Membership comparison at the same boundary |
| 20.5 | 40 | `no` | Just above the pricing boundary |
| 20.5 | 40 | `yes` | Premium rate above the boundary |

Repeat a premium case using ` YES `, including the spaces. Determine expected results before running each case. Check the bill, usage category, and whether a recommendation should appear.

Include the inputs, expected results, and actual results for these checks in your pull request description. No automated test file is supplied.

## Submission

1. Commit and push your work to `development`.
2. Open a pull request from `development` into `main`.
3. In its description, include your test results and briefly explain what you retained from the lab, what you changed, and why the pricing tiers use `if-elif-else` instead of independent `if` statements.
4. **Leave the pull request open** for review.
5. Submit the **pull request URL** in Canvas.

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for detailed instructions.
