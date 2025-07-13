# WOFOST-EW: Enhanced WOFOST Simulation Model for Extreme Weather

---

## Authors  
**Jinhui Zheng**, **Le Yu**, **Zhenrong Du**, **Liujun Xiao**, **Xiaomeng Huang**, and **Liangzhi You**

---

**WOFOST-EW** is an improved version of the [WOFOST](https://www.wur.nl/en/Research-Results/Research-Institutes/Environmental-Research/Facilities-Tools/Software-models-and-databases/WOFOST.htm) (World Food Studies Simulation Model) that improves crop growth simulations under extreme weather conditions. The primary enhancement is in the **Phenology** component (`PCSE-WOFOST-EW/crop/phenology.py`), where an **extreme weather function** has been added. This function combines an **Extreme Weather Index** with an **LSTM deep learning algorithm** for better prediction accuracy. Additionally, the **SCE-UA algorithm** is used to calibrate model parameters.

---

## Resources

### WOFOST Model
The base model is part of the **Python Crop Simulation Environment** (PCSE):
- [PCSE Documentation](https://pcse.readthedocs.io/en/stable/)
- [PCSE GitHub repository by Allard de Wit](https://github.com/ajwdewit/pcse.git)

### SCE-UA Algorithm
For parameter calibration, the **SCE-UA algorithm** implementation is referenced in Spotpy:
- [Spotpy Documentation](https://spotpy.readthedocs.io/en/latest/)

### LSTM Implementation
The **LSTM algorithm** is implemented using the **Keras** library:
- [Keras Documentation](https://keras.io/)

---

## Publications

This version of the WOFOST model has been used in the publication:  

> **"Improving wheat phenology and yield forecasting with a deep learning-enhanced WOFOST model under extreme weather conditions"**  
> Zheng et al. (to be submitted to *Geoscientific Model Development*)

Reference and information will be added later.
