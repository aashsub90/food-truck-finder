# food-truck-finder

A command line tool to fetch all food trucks open in San Francisco at a given time

- Pre-requisite: **Python 3+** located in /usr/local/bin

## Instructions

1. Clone repository or download the zip file

Clone command: git clone https://github.com/aashsub90/food-truck-finder.git

2. Unzip food-truck-finder.zip or food-truck-finder-master.zip (if downloaded from github)

3. Run setup.sh to create a virtualenv, env.sh file and the log folder:

- Execute: ./setup.sh

5. Source environment:

- Execute: source env.sh

- Execute: source food-truck-env/bin/activate

5. Run command to get food trucks open at SF

- Execute: food-truck-finder

6. Logs can be found in logs/food_truck_finder.log

### Sample:

(food-truck-env)~/Projects/food-truck-finder > **_food-truck-finder_**

Food trucks open in San Francisco at 15:41 2019-12-31:

Name Address

---

Athena SF Gyro 699 08TH ST

Authentic India 1355 MARKET ST

Bay Area Dots, LLC 567 BAY ST

Bay Area Dots, LLC 900 BEACH ST

Bay Area Mobile Catering, Inc. dba. Taqueria Angelica's 1455 MARKET ST

Bay Area Mobile Catering, Inc. dba. Taqueria Angelica's 1301 CESAR CHAVEZ ST

Buenafe 901 16TH ST

CARDONA'S FOOD TRUCK 1800 MISSION ST

Casey's Pizza, LLC 1 POST ST

CC Acquisition LLC 525 MARKET ST

Hit 'N' or 'n' to receive more results: n

Additional parameters can be provided to search for trucks open on a specific date and time:

(food-truck-env)~/Projects/food-truck-finder > **_food-truck-finder --date 2020-01-01 --time 13:00_**

Food trucks open in San Francisco at 13:00 2020-01-01:

Name Address

---

Anas Goodies Catering 951 INDIANA ST

Anas Goodies Catering 640 TENNESSEE ST

Anas Goodies Catering 500 FRANCISCO ST

Anas Goodies Catering 2030 03RD ST

Anas Goodies Catering 1255 22ND ST

Anas Goodies Catering 601 MARIPOSA ST

Anas Goodies Catering 700 PENNSYLVANIA AVE

Anas Goodies Catering 1082 PENNSYLVANIA AVE

Athena SF Gyro 10 SOUTH VAN NESS AVE

Athena SF Gyro 699 08TH ST

Hit 'N' or 'n' to receive more results: n

Obtain usage: **_food-truck-finder -h_**
