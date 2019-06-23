#RoboAdvisor
This app is used for checking daily stock prices and determine whether or not user should buy the stock. 
The app monitors the low and high values of the stock for the last 100 days. If the stock price falls below the median of all the low values, the app will prompt user to buy the stock. If it's higher than the median of the lower prices, the app will prompt the user to not buy stock. 


## Environment Setup
```bash
cd ~/roboadvisor/app
conda create -n roboadvisor-env python=3.7 # (first time only)
conda activate roboadvisor-env
```

```bash
pip install -r requirements
pip install pytest
```

##Usage

```bash
python roboAdvisor.py
```