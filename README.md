#PROJECT NAME
## Log-Analysis-project-:
Log analysis is the part of udacity.[FULL-STACK-NANO-DEGREE](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### What is LogAnalysis-:
log analysis is an art and science seeking to make sense out of computer-generated records. The process of creating such records.

### What happening in the project 
* We import the pacakage `psycopg2` 
* Module to connect to the database.

### Output of this project
* what are the most popular three articles in the project 
* what are the most popular article authers of all time
* On which days did more than 1% of requests lead to errors
 
 ### Requirements for Log-Analysis

 1. python3  
 2. Git-Bash
 3. Virtual-Box
 4. Vagrant 
 5. PostgreSQL  
 6. Any Editor 

### There are some links to download for above softwares
 
 | Softwares | Links |
 | ------------ | ----- |
 | Python3 | [https://www.python.org/downloads/] |
 | Git-Bash | [https://git-scm.com/downloads] |
 | Virtual-Box | [https://www.virtualbox.org/wiki/Downloads] |
 | Vagrant | [https://www.vagrantup.com/downloads.html] |
 | PostgreSQL | [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads] |
 | Sublime text | [https://www.sublimetext.com/3] |

 

## How to run Project

 * Go to `vagrant` folrder and run `cmd` or `gitbash.`

###### Launch the vagrant. 

```sh

vagrant up

vagrant ssh

```
###### Download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Download the project zip file and unzip the file now copy unzip file inside.
* Extract the file.
* Past the download file near the database folder.

###### Change the directory into vagrant folder.

```sh
cd /vagrant
```

###### Check the files.

```sh
ll or ls
```
###### Write your folder name.

```sh
cd folder name
```

###### Check the files.

```sh
ll or ls
```

###### Load the data in local database.

```sh
psql -d news -f newsdata.sql
```

###### Run python file.

```sh
python filename.py
```
###### BY-: REVANTH MANDAVA.