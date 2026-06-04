Human Information Processing

**EEG Sleep Signal Analysis**

Using NeuroPype Pipeline Designer 2024.1.0

*Dataset: Sleep-EDF Database (PhysioNet) — SC4001E0 & SC4002E0*

Prof. Chun-Hsiang Michael Chuang

# 1. Introduction

## 1.1 Project Title

EEG-Based Sleep Stage Characterisation Using Spectral Power Analysis: A
NeuroPype Pipeline Approach

## 1.2 Background and Motivation

Sleep is a fundamental physiological process essential for cognitive
function, memory consolidation, and overall health.
Electroencephalography (EEG) is the gold-standard non-invasive technique
for monitoring brain electrical activity during sleep, enabling the
classification of distinct sleep stages including Wake (W), NREM Stages
1–4, and REM sleep.

Each sleep stage is characterised by distinct EEG spectral signatures:
Delta waves (0.5–4 Hz) dominate NREM slow-wave sleep (Stages 3–4), Theta
waves (4–8 Hz) are prominent during NREM Stage 1 and REM sleep, Alpha
waves (8–13 Hz) characterise relaxed wakefulness, and Beta/Gamma
activity (13–45 Hz) reflects arousal and active cognition.

Traditional manual sleep scoring (polysomnography, PSG) requires trained
technicians and is time-consuming. Automated EEG signal processing
pipelines offer a scalable, objective alternative for sleep stage
characterisation and neurophysiological research.

## 1.3 Project Objectives

This project aims to: (1) construct a NeuroPype-based EEG processing
pipeline for PSG data; (2) identify and characterise sleep-stage-related
EEG spectral features; (3) compare EEG band power distributions across
different sleep stages and between two recording nights; and (4)
demonstrate the limitations of bandpass filtering for artifact removal
in wake-state EEG.

# 2. Data Description

## 2.1 Dataset

Data were obtained from the Sleep-EDF Database Expanded (PhysioNet, DOI:
10.13026/C2X676), a publicly available repository of whole-night
polysomnographic recordings. The Sleep Cassette (SC) subset was used,
comprising home recordings by healthy subjects using a portable Medilog
9000 cassette recorder.

## 2.2 Selected Recordings

| **Parameter**   | **SC4001E0 (Night 1)**      | **SC4002E0 (Night 2)**      |
|-----------------|-----------------------------|-----------------------------|
| Subject ID      | SC4001                      | SC4002                      |
| Gender / Age    | Female, 33 years            | Female, 33 years            |
| Recording Date  | 24-Apr-1989                 | 25-Apr-1989                 |
| Recording Start | 16:13                       | 14:50                       |
| Total Duration  | ~22.1 hours (2,650 records) | ~23.6 hours (2,830 records) |
| Epoch Length    | 30 seconds (AASM standard)  | 30 seconds (AASM standard)  |

## 2.3 Hardware and Signal Specifications

| **Parameter**                | **Specification**                                                                        |
|------------------------------|------------------------------------------------------------------------------------------|
| Recording Device             | Oxford Medilog 9000 portable cassette recorder                                           |
| EEG Channels                 | Fpz-Cz and Pz-Oz (bipolar, 10-20 system)                                                 |
| Additional Channels          | EOG (horizontal), Submental EMG, Oro-nasal respiration, Rectal temperature, Event marker |
| EEG Sampling Rate            | 100 Hz                                                                                   |
| Other Channels Sampling Rate | 1 Hz                                                                                     |
| Amplitude Resolution         | ~208 μV range (Fpz-Cz), ~200 μV range (Pz-Oz)                                            |
| File Format                  | European Data Format (EDF)                                                               |
| Sleep Scoring Standard       | Rechtschaffen & Kales (R&K) 1968 manual                                                  |

## 2.4 Software

| **Software**                | **Details**                                        |
|-----------------------------|----------------------------------------------------|
| NeuroPype Pipeline Designer | Version 2024.1.0 (Intheon / Orange 3)              |
| Python                      | CPython 3.11.11 (embedded in NeuroPype)            |
| Signal Processing           | Welch PSD, IIR Butterworth filter (built-in nodes) |
| Hypnogram Parsing           | Custom Python script (PhysioNet EDF+ format)       |

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
<img width="468" height="388" alt="image" src="https://github.com/user-attachments/assets/77315454-677c-47e9-b905-d1f3a78a6ee6" />


![Figure](media/image1.png)

Time Series Plot — Before Filtering (Raw EEG, Wake epoch, SC4001, 51240–51300s)
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
Artifact Subspace Reconstruction (ASR).

*📌 Insert Figure: Time Series Plot — After Filtering (IIR 0.5–45 Hz,
Wake epoch, SC4001, 51240–51300
s)*

<img width="468" height="388" alt="image" src="https://github.com/user-attachments/assets/ef8b28dc-733a-4697-8930-c392c1459885" />


*📌 Insert Figure: Spectrum Plot — Before vs After PSD comparison*

*Before*<br>
<img width="343" height="284" alt="image" src="https://github.com/user-attachments/assets/3c8933ba-af8d-48fb-81b8-3b242b4b2835" />

*After PSD*<br>
<img width="343" height="284" alt="image" src="https://github.com/user-attachments/assets/09d08f2f-6cc9-4707-b5b7-b546d5fdef4a" />


![Figure](media/image4.png)

# 4. NeuroPype Pipeline

## 4.1 Pipeline Architecture

The NeuroPype Pipeline Designer 2024.1.0 pipeline was constructed to
process PSG EDF recordings and extract EEG spectral band power features.
The pipeline comprises six functional stages:

*📌 Insert Figure: NeuroPype Pipeline Screenshot (full canvas)*

## 4.2 Node Configuration

| **Node**               | **Key Parameter** | **Value**                 | **Rationale**                 |
|------------------------|-------------------|---------------------------|-------------------------------|
| Import File            | Exclude channels  | Resp, EMG, Temp, Event    | Resolve mixed Fs error        |
| Import File            | Import time range | Adjustable \[start, end\] | Select specific epochs        |
| IIR Filter             | Frequencies       | \[0.5, 45\]               | Standard EEG passband         |
| IIR Filter             | Filter design     | Butterworth               | Maximally flat passband       |
| Power Spectrum (Welch) | Sub-window length | 400 samples (4 sec)       | Frequency resolution: 0.25 Hz |
| Power Spectrum (Welch) | Overlap           | 200 samples (50%)         | Variance reduction            |
| Power Spectrum (Welch) | Window function   | Hann                      | Reduce spectral leakage       |
| Power Bands            | Delta             | \[0.5, 4\] Hz             | AASM slow-wave definition     |
| Power Bands            | Theta             | \[4, 8\] Hz               | AASM Theta definition         |
| Power Bands            | Alpha             | \[8, 13\] Hz              | AASM Alpha definition         |
| Power Bands            | Beta              | \[13, 30\] Hz             | AASM Beta definition          |
| Power Bands            | Gamma             | \[30, 45\] Hz             | High-frequency activity       |
| Power Bands            | Unit              | relativePSD               | Normalised band proportion    |
| Spectrum Plot          | X axis range      | \[0, 50\] Hz              | EEG-relevant frequency range  |
| Bar Plot               | Y axis range      | \[0, 0.1\]                | Relative power display        |

## 4.3 Pipeline Challenges and Solutions

| **Challenge**                      | **Cause**                                      | **Solution**                               |
|------------------------------------|------------------------------------------------|--------------------------------------------|
| ValueError: mixed sampling rates   | PSG has 100 Hz and 1 Hz channels               | Exclude 1 Hz channels in Import File       |
| OSError: file already opened       | Two Import File nodes or previous session lock | Restart NeuroPype; use single Import node  |
| Select Range error: invalid syntax | Channel names need list format                 | Use \["EEG Fpz-Cz", "EEG Pz-Oz"\] format   |
| Segmentation: no marker stream     | PSG has no event markers for segmentation      | Remove Segmentation; use Welch sub-windows |
| Bar Plot: values near zero         | dB unit compresses differences                 | Switch Power Bands unit to relativePSD     |

*📌 Insert Figure: NeuroPype node parameter screenshots (Import File,
IIR Filter, Power Spectrum, Power Bands, Bar Plot)*

# 5. Demo Video

A demonstration video (\< 2 minutes) was recorded showcasing the
end-to-end NeuroPype pipeline functionality. The video covers the
following segments:

| **Time**  | **Segment**       | **Content**                                                                           |
|-----------|-------------------|---------------------------------------------------------------------------------------|
| 0:00–0:20 | Pipeline Overview | NeuroPype canvas showing full pipeline from Import File to Bar Plot                   |
| 0:20–0:35 | Data Import       | Import File node settings: filename, exclude channels, time range                     |
| 0:35–0:50 | Preprocessing     | IIR Filter parameters; Time Series Plot showing raw vs filtered waveform              |
| 0:50–1:10 | Spectral Analysis | Power Spectrum (Welch) settings; Spectrum Plot output showing PSD curve               |
| 1:10–1:30 | Band Power        | Power Bands node settings; Bar Plot showing Delta/Theta/Alpha/Beta/Gamma              |
| 1:30–2:00 | Stage Comparison  | Switching Import time range between deep sleep and light/REM epochs; Bar Plot changes |

*📌 Insert Video: demo_video.mp4 (\< 2 minutes, screen recording of
NeuroPype pipeline execution)*

# 6. Results & Interpretation

## 6.1 Band Power: Deep Sleep vs Light Sleep/REM

*📌 Insert Figure: Bar Plot — Deep Sleep epoch (SC4001, 583 min, Delta
~96%)*

![Figure](media/image5.png)

*📌 Insert Figure: Bar Plot — Light/REM candidate epoch (SC4001, 509
min, Theta ~58%)*

![Figure](media/image6.png)

| **Epoch**            | **Delta %** | **Theta %** | **Alpha %** | **Interpretation**             |
|----------------------|-------------|-------------|-------------|--------------------------------|
| Deep Sleep (583 min) | 96.1%       | 3.7%        | 0.8%        | NREM N3/N4: slow-wave sleep    |
| Light/REM (509 min)  | 25.3%       | 58.0%       | 12.9%       | REM: Theta-dominant, low Delta |
| Wake (854 min)\*     | High        | Mixed       | Mixed       | Artifacts + mixed frequencies  |

\* Wake epoch characterised by large-amplitude ocular artifacts rather
than clean spectral features.

## 6.2 PSD Curve Analysis

The Spectrum Plot revealed a characteristic 1/f power spectrum for both
channels, with power decreasing as a function of frequency. During deep
sleep epochs, the Delta peak (0.5–2 Hz) was markedly elevated, with
Fpz-Cz peak PSD reaching approximately 230 μV²/Hz (SC4001) and 295
μV²/Hz (SC4002). During light sleep/REM candidate epochs, the Delta peak
was attenuated and the Theta range (4–8 Hz) showed relatively increased
power.

*📌 Insert Figure: Spectrum Plot — SC4001 full-night average PSD (Fpz-Cz
and Pz-Oz)*

![Figure](media/image7.png)

*📌 Insert Figure: Spectrum Plot — SC4002 full-night average PSD (Fpz-Cz
and Pz-Oz)*

![Figure](media/image8.png)

## 6.3 Inter-Night Comparison (SC4001 vs SC4002)

| **Metric**                 | **SC4001 (Night 1)** | **SC4002 (Night 2)**       |
|----------------------------|----------------------|----------------------------|
| Recording duration         | 22.1 hours           | 23.6 hours                 |
| Peak Delta PSD (Fpz-Cz)    | ~230 μV²/Hz          | ~295 μV²/Hz                |
| Deepest Delta epoch        | 97.1% (583 min)      | 97.1% (846 min)            |
| REM candidate (Theta peak) | 58.0% at 509 min     | 49.5% at 429 min           |
| Overall sleep quality      | Moderate slow-wave   | Higher slow-wave intensity |

## 6.4 Neurophysiological Interpretation

The results are consistent with established sleep neurophysiology. Delta
wave dominance (0.5–4 Hz) during NREM slow-wave sleep reflects
synchronised, large-amplitude cortical oscillations generated by
thalamocortical circuits. The observed Delta power exceeding 95% of
total band power during deep sleep epochs is consistent with NREM Stage
3/4 characterisation per the Rechtschaffen & Kales manual used for
hypnogram annotation.

The REM candidate epochs (elevated Theta, suppressed Delta) are
consistent with the REM sleep signature of desynchronised, low-amplitude
EEG with prominent Theta rhythms generated in the hippocampus and
transmitted to frontal regions. The Hypnogram-confirmed first REM onset
at 599.5 minutes in SC4001 closely follows the identified light/REM
candidate at 509 minutes, supporting the validity of the spectral
approach.

The consistently higher Delta power at Fpz-Cz compared to Pz-Oz reflects
the well-established frontal predominance of slow-wave activity,
attributable to the greater density of prefrontal slow-wave generating
cortex. The comparatively higher Alpha and Theta power at Pz-Oz during
lighter sleep stages is consistent with the posterior distribution of
Alpha rhythm generators in occipital cortex.

Night 2 (SC4002) showed greater Delta power magnitude than Night 1
(SC4001), which may reflect homeostatic sleep pressure accumulated
across the day, leading to deeper and more intense slow-wave sleep on
the second night of recording.

## 6.5 Limitations

This analysis has several limitations. First, sleep staging was inferred
from spectral features rather than confirmed automated scoring,
introducing potential misclassification. Second, bandpass filtering
proved insufficient to remove ocular artifacts from wake epochs;
ICA-based artifact rejection would improve data quality. Third, the
absence of a clear wake-to-sleep transition at recording onset prevented
analysis of sleep onset latency. Future work should incorporate the
Hypnogram annotations for ground-truth stage labelling and apply
advanced preprocessing including ICA to enable cleaner spectral
comparisons across all five sleep stages.
