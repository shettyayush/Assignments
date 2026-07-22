# Telecom CDR & Billing Insights CLI

Processes a daily Call Detail Record (CDR) CSV, joins it with subscriber master data, rates valid calls, flags anomalies, and writes an indented JSON report.

## Run

From this directory:

```powershell
python main.py --subscribers subscribers.json --cdrs cdrs.csv --output report.json
```

Optional arguments:

```powershell
python main.py --fraud-threshold-sec 3600
```

The program logs malformed CDR rows and skips them. If more than 10% of input CDR rows are malformed, it logs a critical error, writes no partial report, and exits with status `1`.

Rates are per minute: domestic `1.5`, roaming `8.0`, and international `12.0`. Unknown call types use the domestic rate, as specified in the workbook's rating exercise.
