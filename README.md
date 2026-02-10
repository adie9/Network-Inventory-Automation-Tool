# Network Inventory Automation Tool

## Overview

This project is a Python script that retrieves network device information from a REST API and displays it in a structured table using Pandas.

## Technologies Used

- Python (Requests, JSON, Pandas)
- [mockAPI](https://mockapi.io/)

## What the Script Does

- Retrieves device inventory from REST API endpoint
- Checks whether API request is succesful
- Parses JSON data into Pandas DataFrame
- Displays a clean and readable table of devices and their information
- Outputs data to JSON file

## Sample Data Format

```
[
  {
    "hostname": "switch-01",
    "ip": "10.0.0.5",
    "model": "Cisco 2960"
  },
  {
    "hostname": "router-01",
    "ip": "10.0.0.1",
    "model": "Cisco ISR 4321"
  },
  {
    "hostname": "switch-02",
    "ip": "10.0.0.6",
    "model": "Cisco 2960X"
  },
  {
    "hostname": "switch-03",
    "ip": "10.0.0.7",
    "model": "Cisco Catalyst 9200"
  },
  {
    "hostname": "router-02",
    "ip": "10.0.0.2",
    "model": "Cisco ISR 4451"
  }
]
```

## Sample Output

```
hostname        ip                model
0  switch-01  10.0.0.5           Cisco 2960
1  router-01  10.0.0.1       Cisco ISR 4321
2  switch-02  10.0.0.6          Cisco 2960X
3  switch-03  10.0.0.7  Cisco Catalyst 9200
4  router-02  10.0.0.2       Cisco ISR 4451
```

## Planned Improvements

- Baseline to current state comparison
- CLI menu for user interaction
- Increased data size
- Integration with Cisco Meraki API
