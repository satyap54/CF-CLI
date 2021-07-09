


# CodeForces CLI
Aimed at fetching information on CodeForces from the comfort of terminal.

A cli-tool made using python which is capable of setting reminder for the next CodeForces Round in your Google Calendar. You can also submit solution files from terminal. Currently, I'm trying to add more features that may come handy during a live contest.


## Getting Started

### Installation

* Enable Google Calendar API by going here : https://developers.google.com/calendar/quickstart/python
This will generate a "credentials.json".
* Place your "credentials.json" inside "assets" of project directory.


### Run
```
git clone <this-repo>
```
```
cd CF-Contest_Reminder-master/
```

I recommended to create a python virtualenv to install all the necessary modules.
```
pip install -r requirements.txt
```
```
pip install --editable .
```
```
cf --help
```
* Place your codeforces handle and password in config.py in order to submit code.

### Screenshot
![enter image description here](https://github.com/satyap54/CF-Contest_Reminder/blob/master/assets/CF-Cli-v2.png?raw=true)

![enter image description here](https://github.com/satyap54/CF-CLI/blob/master/assets/Screenshot%20from%202021-06-25%2001-00-29.png)
## To Do

 - contest_data method in cli.py
 - config file for storing hashed password
