# Coded Meemoo CV
Curriculum vitae in code version

The purpose of this project is to visualize my curriculum vitae with Python, Javascript, Typescript and HTML on a local http server.
The only thing the user has to do, is to run one script (meemoo_sv.sh) to put everything in motion.
A little explanation about the process I followed:
1. I use a json file (brondata.json) as the source of the data I want to share
2. I create and populate an in memory database (SQLite3) based on brondata.json
3. I query data from this in memory database, return it in a pandas DataFrame. Eventually I store it again in json files (hobby.json, opleiding.json, werkervaring.json). These files will be generated along the way.
4. I generate a html file (index.html)
5. To handle the clicks on the html page in the browser I made a Typescript file which will be compiled into Javascript.
6. Finally I setup a local http server to view my CV
7. A bash script put all of the listed items above together.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Some thoughts](#some-thoughts)

## Prerequisites
1. Make sure you have a python interpreter installed on your system. The Python version used voor this project is Python 3.11.9. To check your python version use:
```bash
 python --version
```
or 
```bash
 python3 --version
```
2. Create and activate a virtual environment
3. Clone the repository:
```bash
 git clone https://github.com/KristienDauwe/meemoo_cv.git
```
4. Install the requirements.txt
```bash
 pip install -r requirements.txt
```
5. Make sure Node.js is installed on your system. Visit https://nodejs.org/en to download it.
6. Install the Typescript compiler as following:
```bash
npm install -g typescript
```
7. In ./meemoo_cv/ make the following script executable: meemoo_cv.sh

## Usage
1. Execute the meemoo_cv.sh script with this command:
```bash
./meemo_cv.sh
```
2. The script will check if Python is installed properly and give some messages about running the python code and compiling the Typescript file.
3. A local http server is being set up.
- The default portnumber used is 8000 ... BUT
- The script checks if this port is already being used (for other important stuff) so if this is the case, you will be prompted to enter a different port number!
4. Finally you will see a message (My curriculum vitae is ...).
5. Click on the link and you will be redirected to your browser. 
6. IMPORTANT NOTE: The local http server keeps running until you terminate it. This can be done by terminating the script:
- Hit Control+C
- The local server will be shut down and cleaned up

## Some thoughts
I must admit, this was a very fun project to make. I hope you enjoy it as much as I did! Happy coding!
