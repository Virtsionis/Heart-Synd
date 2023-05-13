# Heart-SynD

## Introduction
**Heart-SynD** is an alternated version of **SynD**, a framework for synthetic data generation for Non Intrusive Load Monitoring applications. The original version of SynD was created by Christoph Klemenjak in 2020. More details can be found in the original [Git repo](https://github.com/klemenjak/SynD) and the [corresponding publication](https://www.nature.com/articles/s41597-020-0434-6#citeas).

**Heart-SynD** contains the following key improvements comparing to **SynD**:
- Updated versions of the dependencies in order to run on machines with Python 3.7+
- Updated signature readers making easy for the user to add more appliance signatures
- A slightly modified generation mechanism that allows appliance end uses to be generated in a more random manner regarding the time of day

## Installation

In order install and to use Heart-Synd we recommend the use of a Anaconda. The provided Heart-SynD.yml file contains the necessary dependencies. With the following command the appropriate environment is created: 

Install the depedencies:

'''
conda env create -f Heart-SynD.yml
'''

Activate the environment:

'''
conda activate Heart-SynD
'''

## Usage

### Settings 

In order to create a new installation the user should declare the home appliances, the sampling frequency, the number of days and the output format of the file. All these settings can be edited in the **setting.json**:

```
{"appliances":["wm", "dw", "fridge", "iron", "minioven", "TV", "router", "lamp", "monitor", "hair dryer", "watercooker", "heater"],
 "nr_days":20, "sampling_interval":6 , "add_noise:": true, "output_format":  "CSV", "ID":100, "SEED":78}
 ```
Where the parameters are the following: 

- appliances: The appliances that the created household will contain. 
- days: Number of days of the synthetic data
- output_format: CSV or H5 file as an export of the created household
- sampling_interval: The sampling interval of the created data in (sec) 
- add_noise: Noise creation (Binary)
- ID: ID of the created household
- SEED: Set a SEED for the current experiment      


### Data folder

This can be thought as the input folder where all the traces of the electrical appliances are contained. Both Austrian (taken from the original SynD implementation) and Greek traces are included. 

**Austrian traces**: coffeemachine, dishwasher, fan, fridge, gaming PC, hairdryer, heater, hot_air_gun, iron, lamp, laptop, microwave, mini_oven, monitor, printer, radio, router, TV, washingmachine, watercooker, 

**Greek traces**:  ac, AC_Heart, DR_HEART, dryer, dw, DW_Heart, FR_Heart, wm, WM_Heart

### Target folder

This contains the results of each execution.

### Execution

Simply execute the following commands in terminal after creating the desired settings:

```
cd dataset_generator
python3 main
```





