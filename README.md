# Human Information Processing
Group 6
鍾明諦（114034702), 褚軒麟 (114034803), Khushil Parikh (X1145048)

**EEG Sleep Signal Analysis**

Using NeuroPype Pipeline Designer 2024.1.0

*Dataset: Sleep-EDF Database Expanded (PhysioNet, DOI: 10.13026/C2X676)
— SC4002E0, SC4212E0, SC4522E0*

Prof. Chun-Hsiang Michael Chuang

# 1. Introduction 

## 1.1 Project Title

EEG-Based Sleep Stage Band Power Analysis Using NeuroPype: A Sleep-EDF
Pipeline Approach

## 1.2 Background and Motivation

Sleep is a fundamental physiological process associated with cognitive
restoration, memory consolidation, and changes in information
processing. Electroencephalography (EEG) provides a non-invasive way to
observe sleep-related brain dynamics because different sleep stages show
different spectral patterns.

This project uses the Sleep-EDF dataset and a NeuroPype pipeline to
convert offline polysomnographic EDF recordings into stream-like EEG
data, extract frequency-domain band power features, and compare spectral
activity across Wake, N1, N2, N3/4, and REM sleep stages.

The main analysis focuses on the Fpz-Cz EEG channel because it is useful
for observing slow-wave activity during deep sleep. An additional Pz-Oz
comparison was also included for Subject 21 to examine posterior alpha
activity, which is expected to be more visible over parietal-occipital
regions.

## 1.3 Project Objectives

- Construct an end-to-end NeuroPype pipeline for Sleep-EDF EEG
  processing.
- Use hypnogram markers to collect EEG segments corresponding to W,
N1, N2, N3/4, and REM stages.
- Extract delta, theta, alpha, and beta band power features from
30-second EEG windows.
- Compare sleep-stage-related spectral patterns across three subjects
using Fpz-Cz.
- Use Subject 21 Pz-Oz data as a supplementary comparison to evaluate
posterior alpha activity and spatial channel effects.

# 2. Data Description 

## 2.1 Dataset

The data were obtained from the Sleep-EDF Database Expanded (*DOI:
10.13026/C2X676)*. Each selected recording contains polysomnographic EEG
data and a corresponding hypnogram annotation file. The PSG file
provides the EEG signal, while the hypnogram provides manually scored
sleep-stage markers used to identify the start positions for
stage-specific data collection.

## 2.2 Selected Recordings and Sleep Stages

| **Item**               | **Description**                                                               |
|------------------------|-------------------------------------------------------------------------------|
| Subjects               | Subject 02, Subject 21, and Subject 52                                        |
| Main EEG channel       | Fpz-Cz                                                                        |
| Supplementary channel  | Pz-Oz for Subject 21 channel comparison                                       |
| Sleep stages           | Wake (W), N1, N2, N3/4, and REM                                               |
| Epoch/window length    | 30 seconds                                                                    |
| Main exported features | Delta, theta, alpha, beta, and an additional Ch4 output retained in CSV files |

## 2.3 Channel Selection

Fpz-Cz was used as the main channel for the three-subject sleep-stage
comparison. This choice keeps the analysis consistent across subjects
and supports interpretation of slow-wave activity during deep sleep.
Pz-Oz was additionally processed for Subject 21 to test whether
posterior alpha activity is more clearly represented in a
parietal-occipital derivation.

## 2.4 N3/N4 Combination

Sleep stage 3 and sleep stage 4 were combined into a single N3/4
category because both represent deep NREM sleep dominated by slow-wave
activity. Combining these stages provides a more stable deep-sleep
estimate and aligns the analysis with the modern interpretation of
slow-wave sleep as N3-like deep sleep.

## 2.5 Collected Information

For each subject and sleep stage, NeuroPype exported CSV files
containing channel-wise band power values over time. The cleaned data
were then combined into stage-wise tables, and the average band power
for delta, theta, alpha, and beta was calculated for quantitative
comparison and visualization.

# 3. Data Preprocessing 

## 3.1 Channel Selection and Import

The PSG EDF files contain seven channels recorded at mixed sampling
rates (100 Hz for EEG/EOG; 1 Hz for respiratory, EMG, and temperature
channels). NeuroPype's Import File node raises a ValueError when
channels with different sampling rates are loaded simultaneously. To
resolve this, the four 1 Hz channels were excluded via the Exclude
channels parameter:

| **Channel**    | **Fs (Hz)** | **Action**            |
|----------------|-------------|-----------------------|
| EEG Fpz-Cz     | 100         | Retained for analysis |
| EEG Pz-Oz      | 100         | Retained for analysis |
| EOG horizontal | 100         | Retained (imported)   |
| Resp oro-nasal | 1           | Excluded              |
| EMG submental  | 1           | Excluded              |
| Temp rectal    | 1           | Excluded              |
| Event marker   | 1           | Excluded              |

## 3.2 Artifact Identification

Visual inspection was conducted on the Wake epoch (Stage W) at
51,240–51,300 seconds (approximately 854 minutes into the recording), as
confirmed by the SC4001EC Hypnogram annotation file. This epoch was
selected because wake-state EEG is expected to contain ocular artifacts
from eye blinks and eye movements.

The raw Fpz-Cz signal displayed multiple large-amplitude deflections
(estimated ±200–400 μV), consistent with electrooculographic (EOG)
artifacts propagating to the frontal electrode. The Pz-Oz channel showed
substantially lower amplitude, as expected given its greater distance
from the eyes.

<img width="754" height="625" alt="image1" src="https://github.com/user-attachments/assets/bf5392c1-1287-4c2c-a379-146d91112617" />


Figure 1. Time Series Plot — **Before Filtering** (Raw EEG, Wake epoch,
SC4001, 51240–51300 s)

## 3.3 Bandpass Filtering

An IIR Butterworth bandpass filter (0.5–45 Hz) was applied to remove DC
drift and high-frequency noise while preserving physiologically relevant
EEG components. The filter was implemented using NeuroPype's IIR Filter
node with the following parameters:

| **Parameter**         | **Value**                                                     |
|-----------------------|---------------------------------------------------------------|
| Filter type           | IIR (Infinite Impulse Response)                               |
| Filter design         | Butterworth                                                   |
| Filter mode           | Bandpass                                                      |
| Low cutoff frequency  | 0.5 Hz (removes DC drift and slow baseline wander)            |
| High cutoff frequency | 45 Hz (removes high-frequency noise and line harmonics)       |
| Notch filter          | Not applied (50 Hz European power line within bandpass range) |

## 3.4 Before vs After Filtering

Comparison of the raw and filtered EEG during the wake epoch revealed
that the bandpass filter successfully attenuated high-frequency muscle
noise and baseline drift. However, large-amplitude ocular artifacts
persisted in the filtered signal, as eye movement signals occupy the
0.5–10 Hz frequency range — within the filter passband. Complete
artifact removal would require Independent Component Analysis (ICA) or
Artifact Subspace Reconstruction

<img width="751" height="621" alt="image2" src="https://github.com/user-attachments/assets/92c4c1f1-9fd0-4645-89dc-cb869ceaf10f" />


Figure 2. Time Series Plot — After Filtering (IIR 0.5–45 Hz, Wake epoch,
SC4001, 51240–51300 s)

<img width="1051" height="870" alt="image3" src="https://github.com/user-attachments/assets/08ab1a64-79b5-43b7-938a-c3962714a286" />


Figure 3. Power Spectral Density (PSD) Plot — Before Filtering

<img width="1061" height="876" alt="image4" src="https://github.com/user-attachments/assets/678f48c9-fc10-40a2-85e1-57b305117569" />


Figure 4. Power Spectral Density (PSD) Plot — After Filtering

# 4. NeuroPype Architecture Implementation

## 4.1 Pipeline & Dataset Repository

### Demo Video

A short demonstration video of the NeuroPype pipeline is available here:

[Watch the pipeline demo](./Demo.mp4)

### NeuroPype Pipeline File

The complete NeuroPype pipeline used for the analysis can be accessed here:

[Download/open sleep.pyp](./sleep.pyp)


### Band Power Summary Excel File

The processed EEG band power summary workbook is available here:

[Open/download the band power summary](./bandpower_summary.xlsx)

## 4.2 Visual Pipeline Graph

<img width="488" height="409" alt="image5" src="https://github.com/user-attachments/assets/deaeaf47-9c42-46c5-834b-74ea80313868" />


*Figure 5. NeuroPype EEG band power pipeline overview.*

## 4.3 Pipeline Architecture & Workflow

The PSG files were imported into NeuroPype, and the EEG data were
replayed as a simulated real-time stream using the Stream Data function.
This was necessary because the original EDF recordings are offline
files, while the pipeline was designed to observe dynamic band-power
changes over time.

The EEG signal was filtered to retain the sleep-relevant frequency range
of approximately 0.5–30 Hz. The filtered signal was then segmented using
a 30-second moving window, corresponding to the standard sleep-stage
epoch length used in sleep analysis.

Each 30-second window was transformed from the time domain into the
frequency domain using a Fast Fourier Transform. The magnitude of the
FFT output was taken using absolute value, and then squared to obtain a
power-like spectral representation. Finally, NeuroPype calculated band
power values for the main EEG frequency bands: delta, theta, alpha, and
beta.

The output of this pipeline was visualized using a bar plot and exported
as CSV files. The bar plot provided a visual confirmation of dynamic
changes in band power, while the CSV files were used as the main
quantitative data source for analysis.

## 4.4 Parameter Justification

| **Node**            | **Parameter**                                                                                            | **Explanation**                                                                                                                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDF Import          | Exclude channels: \['EOG horizontal', 'Resp oro-nasal', 'EMG submental', 'Temp rectal', 'Event marker'\] | Unnecessary physiological signals and additional channels were excluded so the analysis focused on EEG band power across sleep stages.                                                                  |
| Stream Data         | Start position: adjusted based on hypnogram markers                                                      | The start position was manually aligned with each sleep-stage marker so that each exported segment corresponded to W, N1, N2, N3/4, or REM.                                                             |
| Select Range        | Selection range: \['Fpz-Cz'\] or \['Pz-Oz'\]                                                             | Fpz-Cz was used as the main analysis channel for consistent sleep-stage comparison. Pz-Oz was additionally used to examine posterior alpha activity.                                                    |
| FFT Filter          | Band-pass filter: \[0.5, 30\] Hz                                                                         | The 0.5–30 Hz range retained the main sleep-related EEG rhythms while reducing slow drift and high-frequency noise.                                                                                     |
| Moving Window       | Window length: 30 seconds                                                                                | A 30-second window matches the standard sleep-staging epoch length, making the spectral calculation physiologically meaningful.                                                                         |
| Band Power Spectral | Delta \[0.5, 4\], Theta \[4, 8\], Alpha \[8, 13\], Beta \[13, 30\]                                       | Standard EEG frequency bands were used to support valid sleep-stage interpretation. These ranges differ from HW3 because this project follows conventional neuroscience and sleep-analysis definitions. |

# 5. End-to-End Analysis Pipeline Demo Video

A demonstration video was prepared to summarize the end-to-end NeuroPype
pipeline. The video walks through the major processing stages required
for the project: signal input/streaming, preprocessing and filtering,
artifact handling, feature extraction, and final computational output.

| **Pipeline Stage**         | **Demo Content**                                                                                                                       |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Signal Input / Streaming   | Import the PSG EDF file and hypnogram file, then use Stream Data with stage-specific start positions.                                  |
| Preprocessing & Filtering  | Select the EEG channel, apply the 0.5–30 Hz filter, and use a 30-second moving window.                                                 |
| Artifact Handling          | Exclude non-EEG signals and reduce out-of-band noise through filtering; ICA-based artifact removal was not applied.                    |
| Feature Extraction         | Apply FFT, convert spectral magnitude into power, and extract delta, theta, alpha, and beta band power.                                |
| Final Computational Output | Display dynamic band power changes using the bar plot and export band power values as CSV files for later averaging and visualization. |

Final output: The NeuroPype pipeline exported CSV files containing band
power values. During streaming, the bar plot showed dynamic band power
changes over time. The CSV values were then used to calculate stage-wise
averages and generate summary plots, including the average band power
chart and the channel comparison figure.

# 6. Analytical Results & Interpretation 

## 6.1 Detailed Results Presentation

The processed EEG band power data were summarized across three subjects
(02, 21, and 52) and averaged within each sleep stage using the Fpz-Cz
channel. The results are presented below.

Table 1. Average EEG band power across sleep stages (Fpz-Cz channel)

| **Sleep stage** | **Delta** | **Theta** | **Alpha** | **Beta** |
|-----------------|-----------|-----------|-----------|----------|
| W               | 62.13     | 63.77     | 62.59     | 61.11    |
| N1              | 57.11     | 59.72     | 57.83     | 55.38    |
| N2              | 62.37     | 62.26     | 59.39     | 56.55    |
| N3/4            | 67.35     | 66.85     | 63.86     | 60.29    |
| REM             | 62.55     | 63.43     | 59.75     | 56.02    |

From the group-level comparison, a clear trend was observed:

- N1 showed the lowest overall band power.
- N2 lay between N1 and N3/4.
- N3/4 exhibited the highest delta and theta power.
- REM and Wake showed relatively higher high-frequency components
compared with lighter NREM stages.

<img width="2014" height="2048" alt="image6" src="https://github.com/user-attachments/assets/4d76d834-b55f-41cf-b0e8-fd60817d5651" />


*Figure 6. Individual subject band power results across sleep stages.*

## 6.2 Differences Between Fpz-Cz and Pz-Oz Channels

For Subject 21, EEG band power was compared between the Fpz-Cz and Pz-Oz
channels across W, N1, N2, N3/4, and REM. The comparison was organized
by frequency band to show how spatial channel selection influences
spectral power distribution.

<img width="2704" height="1497" alt="image7" src="https://github.com/user-attachments/assets/390073e8-1562-4d04-abb0-0cc06866151f" />


Fpz-Cz showed strong delta activity during N3/4 and remained useful for
interpreting slow-wave activity and sleep depth. Pz-Oz showed stronger
alpha activity, especially during Wake and N1, supporting the
expectation that posterior EEG channels are more sensitive to alpha
rhythm.

## 6.3 Neurophysiological Interpretation

### (1) Wakefulness – Posterior Alpha and Wake-Related Activity

In the Fpz-Cz channel, Wake showed relatively high overall band power,
including alpha and beta activity. After adding the Pz-Oz comparison,
the wakefulness interpretation became clearer because Pz-Oz showed
stronger alpha power during Wake. This suggests that the most
characteristic wake-related spectral feature is posterior alpha
activity, which is more clearly captured by the Pz-Oz channel.

This reflects alpha activity associated with relaxed wakefulness and
posterior cortical rhythm, beta activity associated with
higher-frequency cortical activation and alertness, and a channel effect
in which Pz-Oz provides clearer evidence of posterior alpha activity
during wakefulness.

### (2) Light Sleep (N1, N2) – Transitional Processing States

The light sleep stages showed a gradual transition from wake-like
activity toward more stable NREM sleep. In the Fpz-Cz results, N1 showed
relatively low overall band power, supporting its role as a transitional
stage between wakefulness and sleep. With the addition of Pz-Oz, this
transition became more detailed: N1 still showed strong posterior alpha
activity, suggesting that N1 retains some wake-like features and
represents a light, unstable sleep stage.

N2 represents a more stable sleep state than N1. The decrease in
posterior alpha from Wake/N1 to N2 suggests a reduction of wake-like
sensory processing, while the relative increase in theta reflects a
transition toward sleep-related internal regulation.

### (3) Deep Sleep (N3/4) – Dominance of Slow-Wave Activity

N3/4 remains the stage most strongly associated with slow-wave activity,
especially in Fpz-Cz. However, Pz-Oz also captures strong low-frequency
activity, showing that the deep sleep pattern is present across channels
while still being influenced by electrode location.

This is consistent with slow-wave sleep, where large populations of
cortical neurons fire synchronously, producing high-amplitude,
low-frequency oscillations. These slow waves reflect reduced sensory
responsiveness and decreased information processing, corresponding to a
state of deep restorative sleep.

### (4) REM Sleep – Distinct from Deep Sleep

REM remains clearly distinct from deep sleep because both Fpz-Cz and
Pz-Oz show lower delta power in REM than in N3/4. The Pz-Oz data further
show that REM contains moderate mixed-frequency activity rather than
posterior alpha dominance or strong slow-wave synchronization.

This supports the idea that REM sleep is not a deep slow-wave state.
Instead, it is a paradoxical sleep stage with brain activity resembling
wakefulness. REM involves internal processing such as dreaming, where
the brain is active but disconnected from external sensory input.

### (5) Pz-Oz Better Highlights Posterior Alpha Activity

The strongest channel-dependent difference was alpha power. Pz-Oz alpha
was higher than Fpz-Cz alpha in every stage.

<img width="2704" height="1691" alt="image8" src="https://github.com/user-attachments/assets/b4565fbe-e99a-4d24-a0be-832ad40bd4eb" />


This finding supports the interpretation that Pz-Oz is more sensitive to
posterior alpha rhythm, particularly during wakefulness and the light
sleep transition stage N1. The comparison further indicates that EEG
band power is not only sleep-stage dependent, but also spatially
dependent. Overall, Fpz-Cz appears more suitable for interpreting
slow-wave activity during deep sleep, whereas Pz-Oz provides
complementary information about posterior alpha activity during
wakefulness and light sleep.

## 6.4 Overall Interpretation

Overall, the combined Fpz-Cz and Pz-Oz results show that the NeuroPype
pipeline successfully captured both sleep-stage-dependent spectral
changes and spatially dependent EEG characteristics. N3/4 showed strong
low-frequency activity consistent with deep sleep, while Pz-Oz clarified
posterior alpha activity during Wake and N1. These findings support the
use of EEG band power as an interpretable feature set for sleep-stage
analysis.
