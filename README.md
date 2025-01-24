# WOFOST-EW: Enhanced Crop Simulation Model for Extreme Weather

**WOFOST-EW** is an improved version of the WOFOST (World Food Studies Simulation Model) that improves crop growth simulations under extreme weather conditions. The primary enhancement is in the **Phenology** component (pcse/crop/phenology.py), where an **extreme weather function** has been added. This function combines an **Extreme Weather Index** with an **LSTM deep learning algorithm** for better prediction accuracy. Additionally, the **SCE-UA algorithm** is used to calibrate model parameters.

---

## Resources

### WOFOST Model
The base model is part of the Python Crop Simulation Environment (PCSE):
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

This version of the WOFOST model is featured in the upcoming publication:

> **"Improving wheat phenology and yield forecasting with a deep learning-enhanced WOFOST model under extreme weather conditions"**  
> Zheng et al. (to be submitted to *Geoscientific Model Development*)
