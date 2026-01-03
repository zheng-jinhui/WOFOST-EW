<img width="977" height="952" alt="WOFOST-EW-logo" src="https://github.com/user-attachments/assets/4501828b-151e-4ced-b364-dc88774e75b7" />

# WOFOST-EW v1: Enhanced WOFOST for Extreme Weather

---

### Authors  
**Jinhui Zheng**, **Le Yu**, **Zhenrong Du**, **Liujun Xiao**, **Xiaomeng Huang**, **Liangzhi You**, and **Zhe Guo**

---

**WOFOST-EW v1** is an improved version of the [WOFOST](https://www.wur.nl/en/Research-Results/Research-Institutes/Environmental-Research/Facilities-Tools/Software-models-and-databases/WOFOST.htm) (World Food Studies Simulation Model) that improves crop growth simulations under extreme weather conditions. The model incorporates an **Extreme Weather Function** that integrates **Extreme Weather Indices** with an **LSTM deep learning algorithm** to improve prediction accuracy. In addition, the **SCE-UA optimization algorithm** is applied to achieve more efficient parameter calibration.

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

> [Zheng, J., Yu, L., Du, Z., Xiao, L., and Huang, X.: Modeling wheat development under extreme weather with WOFOST-EW v1, Geosci. Model Dev., 18, 8379–8400, https://doi.org/10.5194/gmd-18-8379-2025, 2025.](https://doi.org/10.5194/gmd-18-8379-2025)
