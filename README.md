# Calculate Tax Like Tally

Custom ERPNext app that overrides Sales Invoice tax calculation to match Tally Prime's GST calculation logic with proper rounding.

## Features

- **Tally-compatible rounding**: Item-wise tax amounts use round-half-up (0.5 rounds up)
- **Correct CGST/SGST cumulative totals**: Matches Tally's cumulative calculation exactly
- **Proper grand total rounding**: Final amount rounds to nearest rupee with Tally logic
- **Production-ready**: Runs after ERPNext's standard calculation, ensuring values persist

## How It Works

This app uses Frappe's `override_doctype_class` hook to replace the standard Sales Invoice controller with a custom class that applies Tally-compatible tax calculations after ERPNext completes its standard calculation.

## Installation

### Local Bench Installation

