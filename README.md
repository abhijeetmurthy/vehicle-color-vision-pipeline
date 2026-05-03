# Vehicle Color Vision Pipeline

Generic computer-vision pipeline for vehicle detection/cropping and dominant color extraction.

## Pipeline Stages

1. Ingest: load traffic images.
2. Detect: isolate vehicles from scene backgrounds.
3. Extract: run clustering to get dominant color per vehicle.
4. Aggregate: map raw colors to canonical labels.
5. Report: count and rank dominant colors across the dataset.

## Repository Layout

- `Removal.py`: preprocessing/background handling.
- `encoder.py`: feature/color encoding helpers.
- `mapper.py`: map stage for color grouping.
- `reducer.py`: reduce stage for final color counts.

## Example Dataset Usage

Use your existing Bangalore traffic image set as example inputs for this pipeline.

## Run

Run scripts in pipeline order (`Removal.py` -> `encoder.py` -> `mapper.py` -> `reducer.py`) according to your local setup.
