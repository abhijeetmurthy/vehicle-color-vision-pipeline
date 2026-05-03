# Vehicle Color Vision Pipeline

Enterprise-style computer vision pipeline for detecting vehicles and aggregating dominant colors.

## Structure
- `Removal.py`: preprocessing step.
- `encoder.py`: feature/color encoding.
- `mapper.py`: map stage.
- `reducer.py`: reduce stage.
- `configs/`, `scripts/`, `docs/`: operational scaffolding.

## Quickstart
```bash
./scripts/bootstrap.sh
./scripts/run_pipeline.sh
```

## Example Data
- Existing Bangalore traffic image dataset remains the reference example input.
