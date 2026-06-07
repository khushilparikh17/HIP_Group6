# Sleep-EDF EEG Band Power Data Collection and Analysis Summary

**File:** `sleep_stage_bandpower_cleaned_summary.xlsx`

## 1. NeuroPype Processing Overview

<img width="892" height="853" alt="image" src="https://github.com/user-attachments/assets/be813190-2bbd-4cd3-82ef-c724aaa6d47b" />


This project used **NeuroPype** to process Sleep-EDF EEG and hypnogram data. The PSG `.edf` files were imported into NeuroPype, and the EEG data were replayed as a simulated real-time stream using the **Stream Data** function. This was necessary because the original EDF recordings are offline files, while the analysis pipeline was designed to observe dynamic band-power changes over time.

The EEG signal was filtered to retain the sleep-relevant frequency range of approximately **0.5–30 Hz**. The filtered signal was then segmented using a **30-second moving window**, corresponding to the standard sleep-stage epoch length used in sleep analysis. Each 30-second window was transformed from the time domain into the frequency domain using a Fast Fourier Transform. The magnitude of the FFT output was taken using absolute value, and then squared to obtain a power-like spectral representation. Finally, NeuroPype calculated band power values for the main EEG frequency bands: **delta, theta, alpha, and beta**.

The output of this pipeline was visualized using a **bar plot** and exported as CSV files. The bar plot was used as a visual confirmation of dynamic changes in band power, while the CSV files were used as the main quantitative data source for analysis.

---

## 2. Data Selection and Information Collected

Three Sleep-EDF subjects were selected for analysis:

- Subject 02
- Subject 21
- Subject 52

For each subject, both the PSG EEG file and the hypnogram marker file were used. The hypnogram marker files provided the onset time of each sleep stage, such as Wake, Stage 1, Stage 2, Stage 3, Stage 4, and REM. These marker times were used to determine where to start streaming the EEG data for each sleep stage.

Only the **Fpz-Cz EEG channel** was used for band power extraction. This channel was selected to keep the analysis consistent across all subjects and to reduce complexity. Although another EEG channel, **Pz-Oz**, was available, it was not included in the main analysis so that all comparisons were based on one consistent EEG derivation.

The original Sleep-EDF hypnogram labels include both **Sleep stage 3** and **Sleep stage 4**. In this analysis, these two stages were combined into a single **N3/4** category. This was done because both stages represent deep sleep or slow-wave sleep, and combining them provides a more stable estimate of deep-sleep band power. This also matches the common modern interpretation of deep NREM sleep as N3.

For each subject and each sleep stage, CSV data were collected for:

- W / Wake
- N1
- N2
- N3/4
- REM

The main variables used in the analysis were:

- **Ch0 = Delta**
- **Ch1 = Theta**
- **Ch2 = Alpha**
- **Ch3 = Beta**

Ch4 was retained in the CSV files but was not used as a main analysis band because the EEG signal had already been band-pass filtered to 0.5–30 Hz.

Because the timestamps after the moving-window and FFT steps were reset to `0.0`, the analysis used the known stream start time and stage marker duration to determine which rows belonged to each sleep stage. Rows that were estimated to occur after the next sleep-stage marker were excluded. For example, Subject 02 N1 had a short available duration, so rows after the estimated stage boundary were excluded from analysis. The cleaned data and summary tables were organized into an Excel workbook and subject-specific CSV files.

Example CSV files:

- [02_N1 | Excel](https://365nthu-my.sharepoint.com/personal/114034702_office365_nthu_edu_tw/_layouts/15/Doc.aspx?sourcedoc=%7B14279267-ED99-43AB-B5C5-15049C0682DA%7D&file=02_N1.csv&action=default&mobileredirect=true)
- [02_N2 | Excel](https://365nthu-my.sharepoint.com/personal/114034702_office365_nthu_edu_tw/_layouts/15/Doc.aspx?sourcedoc=%7B7AD78ACD-6A2C-4EAF-AF0E-C4B056F2B225%7D&file=02_N2.csv&action=default&mobileredirect=true)
- [02_N3_4 | Excel](https://365nthu-my.sharepoint.com/personal/114034702_office365_nthu_edu_tw/_layouts/15/Doc.aspx?sourcedoc=%7B56EACC1C-A099-4995-8EB6-DD3585C1B116%7D&file=02_N3_4.csv&action=default&mobileredirect=true)

---

## 3. Data Results and Interpretation

The cleaned and averaged results showed that the EEG band power differed across sleep stages. Across the three subjects, the average band power values were:

| Sleep stage | Delta | Theta | Alpha | Beta |
|---|---:|---:|---:|---:|
| W | 62.13 | 63.77 | 62.59 | 61.11 |
| N1 | 57.11 | 59.72 | 57.83 | 55.38 |
| N2 | 62.37 | 62.26 | 59.39 | 56.55 |
| N3/4 | 67.35 | 66.85 | 63.86 | 60.29 |
| REM | 62.55 | 63.43 | 59.75 | 56.02 |

<img width="1172" height="393" alt="image" src="https://github.com/user-attachments/assets/3cd56818-e407-4f1c-bc2b-40e5f77ece65" />

<img width="2048" height="2083" alt="image" src="https://github.com/user-attachments/assets/d73f115c-066a-4083-a8aa-996804433d3b" />


These results show that **N3/4 had the highest delta and theta power**, which is consistent with the expected characteristics of deep sleep and slow-wave activity. N1 showed the lowest overall band power, which is also reasonable because N1 is a lighter and more transitional sleep stage. N2 showed intermediate values between N1 and N3/4, which fits the expected progression from light sleep to deeper sleep.

The Wake stage showed relatively high alpha and beta power compared with N1 and N2. This is reasonable because wakefulness can contain stronger alpha activity and higher-frequency activity related to alertness, movement, or arousal. REM showed values lower than N3/4, especially in delta power, which supports the distinction between REM sleep and deep slow-wave sleep.

The individual-subject plots also showed some variability across subjects, but the overall pattern remained interpretable. Subject 21 showed a particularly clear pattern, with N3/4 having the strongest delta power and N1 showing lower band power. Subject 52 also showed strong N3/4 delta activity, although REM and Wake values were relatively high. Subject 02 showed higher values in N2 and N3/4 compared with N1, supporting the general stage-related trend.

Overall, the results suggest that the NeuroPype pipeline successfully captured meaningful differences in EEG band power across sleep stages. The clearest finding was the increase in low-frequency power, especially delta power, during N3/4. This supports the expected physiological interpretation that deep sleep is characterized by stronger slow-wave activity. The results also show that band power analysis can be used to differentiate lighter sleep, deeper sleep, REM sleep, and wakefulness, although absolute power values should be interpreted carefully because they may be affected by channel selection, windowing, stream timing, and individual subject variability.
