# YouTube Engagement & Dislike Analysis

An exploratory data analysis project connecting video engagement metrics with Python, SQL and a linear regression baseline. The analysis examines publishing patterns, channel activity, and relationships between views, likes, dislikes and comments.

**Stack:** Python · pandas · NumPy · Matplotlib · Seaborn · scikit-learn · SQLite  
**Status:** Academic analysis export. The original input CSV is required to reproduce results.

[Read the analysis](Analysing%20Youtube%20Dislike%20Dataset.py) · [Dependencies](Requirements.txt) · [Author](https://github.com/Aswin9629)

## What the project demonstrates

- Inspecting schema, missing values, summary statistics and unique video/channel counts.
- Cleaning missing records and extracting publishing month from timestamps.
- Comparing channels by video count and identifying engagement extremes.
- Exploring correlations through scatter plots and a heatmap.
- Writing a dataset to SQLite and querying the resulting table.
- Fitting a linear regression baseline to estimate `view_count` from `likes`, `dislikes` and `comment_count`.

## Reproduce the workflow

1. Obtain the original `youtube_dislike_dataset[1].csv` and place it in the repository root. The CSV is not included in this repository.
2. Install the listed dependencies:
   ```bash
   python -m pip install -r Requirements.txt
   ```
3. Run the exported analysis:
   ```bash
   python "Analysing Youtube Dislike Dataset.py"
   ```

Required fields include `video_id`, `channel_id`, `channel_title`, `title`, `published_at`, `view_count`, `likes`, `dislikes` and `comment_count`. Interactive plots open in sequence; standalone expressions from the original notebook will not display in a terminal.

## Evaluation and interpretation

The first regression experiment uses an 80/20 split with `random_state=42` and reports **mean squared error** and **R²**. These are regression metrics, not classification accuracy.

Engagement variables are observed alongside views. This is an association/prediction exercise, not a demonstration of forecasting future views or a causal effect of dislikes.

The exported script later reloads the raw CSV for SQLite and a second modeling section. That section needs the same missing-value validation as the first. Its final `test_with_new_samples(df)` call includes training records and must not be reported as an independent test score. No numeric performance claim is made here without reproducible output.

## Outputs

- Channel and monthly publishing summaries.
- Engagement scatter plots and correlation heatmap.
- A local `youtube_dislike_dataset[1].db` database with a `youtube` table.
- Console regression metrics.

## Next development steps

Keep preprocessing consistent across every modeling section, sort timestamps before time-based plotting, evaluate on a genuinely unseen dataset, and package the analysis into a reproducible notebook or command-line workflow.

## Author

**Aswin S** · [GitHub](https://github.com/Aswin9629)
