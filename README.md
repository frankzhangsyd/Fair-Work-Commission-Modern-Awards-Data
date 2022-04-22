# Fair-Work-Commission-Modern-Awards-Data
Python script to retrieve data from Australian Fair Work Commission Modern Awards API with package [pyfwc](https://github.com/frankzhangsyd/pyfwc)

Usage
-----

You can :
1. download data from the [data folder](https://github.com/frankzhangsyd/Fair-Work-Commission-Modern-Awards-Data/tree/main/data) (latest data as `2022-04-22`)
OR
2. execute script by yourself (recommended)

To execute script:
1. Make sure you have python version >=3.7.4 and installed [pyfwc](https://github.com/frankzhangsyd/pyfwc) (You can install it by `pip install pyfwc`)
2. Register on the Fair Work Commission Modern Awards API website (https://uatdeveloper.fwc.gov.au/) and obtain a subscription key.
3. Download the `main.py` file and replace the subscription key with yours.
4. Execute the script by running `python main.py` in the terminal and it will create `data` folder in the same directory as the `main.py` script.

*NB: Although fair work commission doesn't mention any limits of API as today (2022 Apr), I still apply a 10-seconds delay between query for each award. You can adjust the delay in script. Please be gentle to the API*