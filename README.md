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

This code was developed on macOS (M3 chip):
- node.js v20.13.1
- python 3.11.9
- npm 10.5.2

And I ran it on a virtual machine (VMWare Fusion Pro) with a Linux distribution (Ubuntu-22.04.4) where I run into some issues compiling the typescript:
This was solved when I installed Node.js using nvm:
```bash
# first install curl
sudo apt install curl

# installs nvm (Node Version Manager) afterwards close your terminal and open it again
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash


# download and install Node.js
nvm install 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.13.1`

# verifies the right NPM version is in the environment
npm -v # should print `10.5.2`
```

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Some thoughts](#some-thoughts)

## Prerequisites
1. Make sure Node.js is installed on your system. Visit https://nodejs.org/en to download it.
2. Make sure you have a python interpreter installed on your system.  To check your python version use:
```bash
 python --version
```
or 
```bash
 python3 --version
```
3. Make sure you have git installed on your system.
```bash
 sudo apt install git
```
4. Create and activate a virtual environment
5. Clone the repository:
```bash
 git clone https://github.com/KristienDauwe/meemoo_cv.git
```
6. Install the requirements.txt
```bash
 pip install -r requirements.txt
```
7. Install the Typescript compiler as following:
```bash
 npm install -g typescript
```
8. Make sure meemo_cv.sh is executable

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
