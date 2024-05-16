# meemoo_cv
Curriculum vitae in code version

The purpose of this project is to visualize my curriculum vitae with Python, Javascript, Typescript and HTML.
I use a json file with meta(data) to create a database in memory. 
Next step is to extract the data and create other json files (hobby.json, werkervaring.json, opleiding.json) to store it for later use (in javascript) after I generate the HTML file (index.file).
This whole process happens with Python code. 
In the next step there will be an initialisation of a local http server in your browser.
When you navigate to this localhost you can open the meemo_cv/src directory to find the index.html file. 
Click on it... and with a little bit of luck it opens!
Javascript is used to visualize the json data in table format.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## Prerequisites
1. Activate a virtual environment
2. Make sure you have a python interpreter installed on your system. The version used voor this project is Python 3.11.9 To check your python version use:
```bash
 python --version
```
3. Clone the repository:
```bash
 git clone https://github.com/KristienDauwe/meemoo_cv.git
```
4. Install the requirements.txt
```bash
 pip install -r requirements.txt
```
5. Make sure Node.js is installed and if necessary install the Typescript compiler as following
```bash
npm install -g typescript
```
6. In /meemoo_cv/ make the following script executable: meemoo_cv.sh

## Usage


