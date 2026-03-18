# NASA POWER to DSSAT Weather Data Converter

This repository contains a Python script developed to automate the download of daily climate data from the NASA POWER API and convert it directly into the `.WTH` file format, which is the standard required by the **DSSAT** (Decision Support System for Agrotechnology Transfer) crop modeling system.


## 📋 Prerequisites

To run this script, you will need Python 3.x installed on your machine. The project's external dependencies can be installed via `pip`:


```bash
pip install pandas requests
```

# How to use
1. Clone this repository or download the main Python file.

```python
pip install nasapower-dssat==0.1
```

2. Open the script in your preferred IDE and navigate to the bottom of the code, in the main() function.
3. Change the configuration variables to match your study area:

```python
latitude = -13.54        # Your latitude (in decimal degrees)
longitude = -58.82       # Your longitude (in decimal degrees)
start_date = '19950101'  # Start date in YYYYMMDD format
end_date = '20241231'    # End date in YYYYMMDD format
site_code = 'BRMT'       # Site code for DSSAT (4 characters)
elevation = 370          # Site elevation in meters
```
4. Adjust the dates within the get_daily_nasa_power_data function calls if you need a different period than the one configured in the example.

## Output

After a successful run, the script will automatically create a directory named ./output/ in the same folder as the main file. The weather file will be generated there, following the DSSAT naming convention (e.g., WBRMT01.WTH).

Additionally, the terminal will display a statistical summary of the collected time series, allowing for a quick check of data integrity.