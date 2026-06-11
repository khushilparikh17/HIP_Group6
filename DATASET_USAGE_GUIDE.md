# Dataset Usage Guide

This document explains how to use the dataset files, marker files, and exported EEG band power results for the Sleep-EDF EEG band power analysis project.

This guide is intended to help users reproduce the data collection workflow in NeuroPype and understand how the dataset folders and result files are organized.

---

## 1. Project Data Overview

This project uses EEG data from three Sleep-EDF subjects:

```text
Subject 02
Subject 21
Subject 52
```

Each subject has two EDF files:

1. **PSG EDF file**  
   Contains the physiological recording, including EEG signals.

2. **Hypnogram EDF file**  
   Contains sleep-stage annotations and marker information.

The PSG file and hypnogram file should be loaded into different NeuroPype import nodes.

---

## 2. Recommended Folder Structure

The dataset package is organized into three main folders:

```text
Project_Folder/
│
├── Datasets (3 subject)/
│   ├── SC4002E0-PSG.edf
│   ├── SC4002EC-Hypnogram.edf
│   ├── SC4021E0-PSG.edf
│   ├── SC4021EH-Hypnogram.edf
│   ├── SC4052E0-PSG.edf
│   └── SC4052EC-Hypnogram.edf
│
├── Markers/
│   ├── 02_markers.csv
│   ├── 21_markers.csv
│   └── 52_markers.csv
│
└── Results/
    ├── Fpz-Cz Channel/
    │   ├── 02_W.csv
    │   ├── 02_N1.csv
    │   ├── 02_N2.csv
    │   ├── 02_N3_4.csv
    │   ├── 02_REM.csv
    │   ├── 21_W.csv
    │   ├── 21_N1.csv
    │   ├── 21_N2.csv
    │   ├── 21_N3_4.csv
    │   ├── 21_REM.csv
    │   ├── 52_W.csv
    │   ├── 52_N1.csv
    │   ├── 52_N2.csv
    │   ├── 52_N3_4.csv
    │   └── 52_REM.csv
    │
    └── Pz-Oz/
        ├── 21_W_Pz_Oz.csv
        ├── 21_N1_Pz_Oz.csv
        ├── 21_N2_Pz_Oz.csv
        ├── 21_N3_4_Pz_Oz.csv
        └── 21_REM_Pz_Oz.csv
```

---

## 3. EDF File Usage in NeuroPype

The NeuroPype pipeline uses two separate EDF import nodes.

### 3.1 Main EEG Import Node

The **PSG EDF file** should be loaded into the main EEG import node.

Example PSG files:

```text
SC4002E0-PSG.edf
SC4021E0-PSG.edf
SC4052E0-PSG.edf
```

This import node provides the EEG signal that is passed through the main processing pipeline:

```text
Stream Data
→ Select Range
→ FFT Band-Pass Filter
→ Moving Window
→ FFT
→ Absolute Value
→ Power
→ Power Bands
→ Bar Plot
→ Record to CSV
```

### 3.2 Marker / Hypnogram Import Node

The **hypnogram EDF file** should be loaded into a separate EDF import node for marker extraction.

Example hypnogram files:

```text
SC4002EC-Hypnogram.edf
SC4021EH-Hypnogram.edf
SC4052EC-Hypnogram.edf
```

This import node is used only to extract sleep-stage marker information. The marker output should be exported as a CSV file and used to determine suitable start positions for EEG streaming.

---

## 4. Recommended Workflow for Marker Extraction

Before collecting EEG band power data, it is recommended to first export the sleep-stage markers as CSV files.

### Step 1. Load the Hypnogram File

Load the selected subject’s hypnogram EDF file into the marker import node.

### Step 2. Export Markers as CSV

Run the marker branch of the NeuroPype pipeline and export the marker stream into the `Markers/` folder.

Example marker CSV outputs:

```text
02_markers.csv
21_markers.csv
52_markers.csv
```

Before switching to a different subject, remember to update the marker CSV output path.

### Step 3. Select Suitable Sleep-Stage Time Points

Open the exported marker CSV file and inspect the sleep-stage transition times.

Select a stable segment for each target sleep stage:

```text
Wake (W)
N1
N2
N3/4
REM
```

It is recommended to avoid timestamps that are too close to sleep-stage transitions.

### Step 4. Update Stream Data Start Position

After selecting a suitable timestamp, update the **Start pos** parameter in the **Stream Data** node.

Example:

```text
Stream Data → Start pos = selected sleep-stage marker time
```

This ensures that the streamed EEG segment starts from the intended sleep stage.

---

## 5. EEG Channel Selection

Two EEG channels were used in this project:

```text
Fpz-Cz
Pz-Oz
```

### 5.1 Fpz-Cz Channel

The Fpz-Cz channel was used as the main channel for the three-subject sleep-stage comparison.

This channel was selected because it is useful for observing slow-wave activity during deep sleep.

To collect Fpz-Cz data, set the Select Range node to:

```text
['Fpz-Cz']
```

### 5.2 Pz-Oz Channel

The Pz-Oz channel was additionally processed for Subject 21.

This channel was used to examine posterior alpha activity, especially during Wake and N1.

To collect Pz-Oz data, set the Select Range node to:

```text
['Pz-Oz']
```

---

## 6. Exporting Band Power Results

The final output of the NeuroPype pipeline is exported as CSV files.

During streaming, the bar plot provides a dynamic visualization of band power changes over time. The CSV output stores numerical band power values for later averaging, cleaning, and plotting.

### Recommended Output Folders

When collecting data from different EEG channels, it is recommended to change the CSV output folder to keep the results organized.

For Fpz-Cz:

```text
Results/Fpz-Cz Channel/
```

For Pz-Oz:

```text
Results/Pz-Oz/
```

Changing the output folder when collecting data from different channels makes the results easier to classify and prevents accidental file overwriting.

---

## 7. Result File Naming Convention

The current result files follow this naming convention:

```text
subject_stage.csv
```

Examples:

```text
21_N3_4.csv
02_W.csv
52_REM.csv
```

For Pz-Oz channel results, the channel name is added to the filename:

```text
subject_stage_Pz_Oz.csv
```

Examples:

```text
21_W_Pz_Oz.csv
21_N1_Pz_Oz.csv
21_N3_4_Pz_Oz.csv
```

The sleep-stage labels used in the filenames are:

```text
W
N1
N2
N3_4
REM
```

`N3_4` represents the combined deep sleep category. N3 and N4 were combined because both stages represent deep slow-wave sleep.

---

## 8. General NeuroPype Processing Pipeline

The overall NeuroPype processing workflow is:

```text
PSG EDF Input
→ Stream Data
→ Select EEG Channel
→ 0.5–30 Hz Filtering
→ 30-second Moving Window
→ FFT
→ Absolute Value
→ Power Calculation
→ Band Power Extraction
→ Bar Plot Visualization
→ CSV Export
```

The extracted band power values include:

```text
Delta: 0.5–4 Hz
Theta: 4–8 Hz
Alpha: 8–13 Hz
Beta: 13–30 Hz
```

The exported CSV files were later cleaned and combined for stage-wise average band power analysis.

---

## 9. Output CSV Format

Each exported CSV file contains band power values over time.

Typical columns:

```text
Ch0
Ch1
Ch2
Ch3
Ch4
timestamp
```

In this project, the main interpreted channels were:

```text
Ch0 = Delta
Ch1 = Theta
Ch2 = Alpha
Ch3 = Beta
```

`Ch4` was retained in the exported files but was not used as a main analysis band.

---

## 10. Reproducing the Analysis

To reproduce the data collection process:

1. Open the NeuroPype pipeline file.
2. Load the PSG EDF file into the main EEG import node.
3. Load the corresponding hypnogram EDF file into the marker import node.
4. Export the marker CSV file first.
5. Inspect the marker CSV and choose a stable sleep-stage time point.
6. Update the Stream Data `Start pos`.
7. Select the target EEG channel in the Select Range node.
8. Update the CSV output folder.
9. Run the pipeline.
10. Export the band power CSV file.
11. Repeat the process for each sleep stage and subject.

---

## 11. Example Workflow for Subject 21

### Example: Collecting N3/4 Data from Fpz-Cz

```text
1. Load SC4021E0-PSG.edf into the main EEG import node.
2. Load SC4021EH-Hypnogram.edf into the marker import node.
3. Export 21_markers.csv.
4. Select a stable N3/4 marker time.
5. Set Stream Data Start pos to the selected N3/4 time.
6. Set Select Range to ['Fpz-Cz'].
7. Set CSV output folder to Results/Fpz-Cz Channel/.
8. Run the pipeline and export 21_N3_4.csv.
```

### Example: Collecting N3/4 Data from Pz-Oz

```text
1. Use the same PSG and hypnogram files.
2. Use the same selected N3/4 start position.
3. Change Select Range to ['Pz-Oz'].
4. Set CSV output folder to Results/Pz-Oz/.
5. Run the pipeline and export 21_N3_4_Pz_Oz.csv.
```

---

## 12. Important Notes

- Always update the marker CSV output path before exporting markers for a different subject.
- Always update the band power CSV output path before collecting a different channel or sleep stage.
- Avoid selecting start positions too close to sleep-stage transitions.
- Keep Fpz-Cz and Pz-Oz results in separate folders for easier analysis.
- Use consistent file naming to make later averaging and plotting easier.

---

## 13. Project Outputs

The exported CSV files can be used to calculate:

```text
Stage-wise mean band power
Subject-wise band power comparison
Channel comparison between Fpz-Cz and Pz-Oz
Average band power plots
```

The final analysis in this project used the cleaned CSV files to generate:

```text
Average band power by sleep stage
Individual subject results
Subject 21 Fpz-Cz vs Pz-Oz comparison
```
