# sawayaka-analysis

Analyze how Sawayaka's lines, which is a famous casual restaurant chain in Japan, are affected by shop location, surrounding population, and time of day.

## Requirements

```console
poetry install
```

## Data preparation

Run app/collect.py to prepare data.
It will collect waiting line length and estimated waiting time, etc. for each shop using the reservation site's API and store the response to Amazon S3.
Later, you can download the files and run analysis.
