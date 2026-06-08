A/B Integration: Stubs and Measurement

- Capture assignment: ensure each user receives a treatment flag and the assigned variant is persisted in a log or event stream.
- Expose a webhook/endpoint in api_app.py to receive experiment assignment metadata and impressions.
- Measurement: use the offline experiment data to compute ATT/ATE using uplift methods (see docs/case_study.md).
- Recommendations: store assignments in a single table or parquet file keyed by user_id with timestamps; join to outcome window for analysis.
