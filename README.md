# SDG4 Survey Template Automation
Independent, illustrative Python demonstration prepared for a consultancy application. Not an official UNESCO/UIS system. All data are synthetic; the schema and validation rules are illustrative, not official SDG 4 specifications.

## Run locally
Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python generate_samples.py
python main.py
python -m unittest test_pipeline
```

## Workflow
The pipeline reads Excel files from `sample_data/`, checks the Survey worksheet headers, writes version metadata to copies in `outputs/updated_templates/`, validates nonnegative integer counts, survey year, enrolment totals and duplicate country/year keys, and consolidates accepted rows. Original files remain unchanged. Rejected rows are excluded and reported with source filename and row number. Duplicate keys are rejected rather than silently resolved.

## Example results
Four synthetic submissions: two accepted, two rejected (inconsistent enrolment total and missing count). See `outputs/consolidated.xlsx` and `outputs/validation_report.csv`.

## Limitations
This is a small prototype, not a production system. Actual UIS templates, indicator definitions, missing-value conventions, validation rules and acceptance tests would be required before deployment. Template updates currently demonstrate metadata versioning only. The script does not recalculate Excel formulas or guarantee preservation of advanced Excel features. The included test covers the supplied demonstration dataset.
