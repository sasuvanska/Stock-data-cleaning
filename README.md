# Financial Market Data Engineering & Cleaning Pipeline

A deterministic, point-in-time-safe ETL and validation pipeline for daily equity market data (OHLCV). Designed to transform raw, unadjusted market feeds into institutional-grade time series ready for quantitative research and backtesting without look-ahead bias or data-induced artifacts.

## Overview & Motivation

Standard statistical and machine learning models break down when trained on raw public market feeds due to unadjusted corporate actions, calendar misalignments, stale quotes, and isolated price spikes ("bad ticks"). Rather than relying on black-box pre-adjusted prices or naive row deletion (`dropna()`), this pipeline implements explicit financial data engineering principles:

* **Zero Look-Ahead Bias:** All rolling statistical filters and imputation steps strictly isolate past observations (`t-1` and prior) from current-day evaluations.
* **First-Principles Corporate Action Adjustments:** Reconstructs split-adjusted and total-return price series directly from raw unadjusted quotes, dividend distributions, and split ratios—using vendor `Adj Close` strictly as an automated unit-test benchmark.
* **Statistical Outlier Discrimination:** Distinguishes genuine fat-tailed market shocks (earnings surprises, macro crashes) from single-day feed errors using a 60-day rolling Median Absolute Deviation (MAD) filter paired with next-day mean-reversion diagnostics.

---

## Pipeline Architecture

The pipeline separates data ingestion from transformation and validation into a modular two-stage architecture:

```text
data/raw/ (Parquet)  ──▶  [1. Calendar & Schema Alignment]
                              │
                              ▼
                          [2. OHLCV Integrity & Stale Quote Checks]
                              │
                              ▼
                          [3. Corporate Action Factor Chaining]
                              │
                              ▼
                          [4. Rolling MAD & Bad Tick Filtering]
                              │
                              ▼
data/processed/      ◀──  [5. Clean Time Series]
