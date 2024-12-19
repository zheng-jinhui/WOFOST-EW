# WOFOST-EW

WOFOST-EW is an improved version of the WOFOST (World Food Studies Simulation Model), with a primary modification in the Phenology component. An extreme weather function has been added, integrating the extreme weather index and the LSTM deep learning algorithm to enhance the model's crop simulations under extreme weather conditions. Additionally, we used the SCE-UA algorithm to calibrate the model parameters.

## Model and Algorithm Sources

- The WOFOST model used is from the Python Crop Simulation Environment (PCSE), available at:  
  [PCSE Documentation](https://pcse.readthedocs.io/en/stable/)  
  or  
  [PCSE GitHub Repository](https://github.com/ajwdewit/pcse.git).

- The SCE-UA algorithm can be referenced at:  
  [Spotpy Documentation](https://spotpy.readthedocs.io/en/latest/).

- The LSTM is implemented using the “Keras” library provided by Python.

## Publications

This version of the WOFOST model has been used in the publication:  
**"Improving wheat phenology and yield forecasting with a deep learning-enhanced WOFOST model under extreme weather conditions"**  
by Zheng et al., to be submitted to *Geoscientific Model Development*.  
Reference and information will be added later.
