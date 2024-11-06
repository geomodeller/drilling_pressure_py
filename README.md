# Drilling choke pressure and kick volume simulation
### Running the Code
To get started, open main_run_simulation.ipynb. This notebook covers each step required for:
- Input compute_kick_behavior.py of sub_compute_kick_behavior.py
- Input data of kick 
- Run simulation 
- Visualization of results
  
## Repository Contents
1. **main_run_simulation.ipynb:** Main notebook with kill simulation when kick experiencing. 
1. **sub_compute_kick_behavior.py:** Calculate kCdk volume and dhoke pressure when kick experiencing.
1. **pressure.py:** Calculate pressure about kick
1. **volume.py:** Calculate volume about kick
1. **temperature.py:** Calculate temeprature about kick
1. **miscellaneous.py:** Calculate time conversion 
1. **flow.py:** CalCulate flow mechanics parameters
1. **eos.py:** CalCulaCe fluid's properties 

## Questions or Feedback?
Please reach out to 12191305@inha.edu or honggeun.jo@inha.ac.kr.

![image](https://github.com/user-attachments/assets/96fa9ad8-314e-4497-ba8e-4c6428efb15c)

---
Below is the abstract for the presentation at the Fall 2024 KSMER Conference:
# Sensitivity Analysis of Maximum Choke Pressure and Maximum Kick Volume per Drilling Operation Condition
### 시추운영인자별 킥 제거시 최대 초크압력과 최대 킥 부피 민감도 분석
### Authors: Donghee Kim, Hyunmin Kim, Eunsil Park
### Affiliation: [INHA_ERE](https://eneres.inha.ac.kr/eneres/index.do), [CURE_lab](https://petroinha.github.io/)

Introduction
With the increasing global demand for carbon neutrality, drilling technologies are not only being developed for traditional oil exploration but are also expanding into areas like natural hydrogen development and storage, helium extraction, and underground carbon dioxide (CO₂) sequestration. This research focuses on developing a comprehensive process for managing kick events during drilling operations, implemented using Python, which models the pressure and volume dynamics from the moment a kick occurs until it is controlled.

Objective
The main objective of this study is to analyze the sensitivity of maximum choke pressure and maximum kick volume to various drilling operation parameters. The parameters analyzed include:

The type of kick fluid (e.g., hydrogen, helium, natural gas, carbon dioxide)
Flowing bottom hole pressure
Mud density
Subsurface temperature gradient
Kill rate
Methodology
Implementation: A Python-based implementation of Choi’s (2017) well control methodology is used to model and calculate the choke pressure and kick volume dynamics during kick removal.
Sensitivity Analysis: A multiple linear regression model standardizes the values of operational parameters to investigate their impact on the maximum choke pressure and maximum kick volume. The analysis revealed that the type of kick fluid significantly influences the outcomes.
Results
The regression coefficients from the sensitivity analysis showed that the type of kick fluid (such as hydrogen, helium, natural gas, or CO₂) has the most substantial impact on both the maximum choke pressure and maximum kick volume. This insight highlights which factors are critical during well control operations and should be prioritized.

Conclusion
This study provides essential guidance on the factors that must be carefully considered during kick removal to ensure safe and efficient drilling operations. It emphasizes the importance of understanding the influence of various operational parameters to improve well control practices.

Should you have any question, please contact us via hogggeun.jo@inha.ac.kr
