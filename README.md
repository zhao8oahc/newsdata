# Newsdata Reporting Tool #
This project meant to create a reporting tool that prints out reports of three questions below based on the data in the [new database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), which using a Python program under the `psycopg2` module to connect to the database. 

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Install ##
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html).
2. Download [VM configuration](https://github.com/udacity/fullstack-nanodegree-vm) , [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
3. Clone this repository into vagrant folder, and unzip `newsdata.zip` into newsdata folder.
4. Enter the `vagrant` directory in the terminal and run the command `vagrant up` to install. After `vagrant up` is finished running, run `vagrant ssh` to log into the VM.
5. `cd` into the `/vagrant` directory and use the command `psql -d news -f newsdata.sql` to load the data.

##Report##
1. `cd` into newsdata folder
2. Add views by typing `psql -d news -f create_views.sql*` in the VM.
3. Run `python newsdata.py` to generate report texts.

##Reference##
[chints87/newsdata](https://github.com/chints87/newsdat)