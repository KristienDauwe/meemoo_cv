#!/bin/bash

# Function to check if a port is in use
is_port_in_use() {
    local port=$1
    if lsof -i:$port &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to prompt user for a new port if the default is in use
prompt_for_port() {
    local port
    while true; do
        read -p "Enter a port number to use: " port
        if ! [[ "$port" =~ ^[0-9]+$ ]]; then
            echo "Invalid input. Please enter a numeric port number."
        elif is_port_in_use $port; then
            echo "Port $port is already in use. Please choose another port."
        else
            echo $port
            return
        fi
    done
}

# Default port
PORT=8000

# Check if the default port is in use
if is_port_in_use $PORT; then
    echo "Port $PORT is already in use."
    PORT=$(prompt_for_port)
fi

echo "Using port $PORT"

# Check if python interpreter is installed
if command -v python &> /dev/null; then
    echo "Python is installed."
else
    echo "Python is not installed."
fi

if command -v python3 &> /dev/null; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed."
fi

# Run main.py to create in-memory database, fill it with data, extract it again, store it, and create index.html
if python ./src/main.py; then
    echo "Python code ran successfully"
else
    echo "Failed to run Python code"
    exit 1
fi

# Compile the TypeScript file and create the JavaScript file for use in the HTML
if tsc ./src/interactie.ts; then
    echo "interactie.ts compiled to interactie.js"
else
    echo "Failed to compile interactie.ts"
    exit 1
fi

# Start local HTTP server on the selected port
if python -m http.server $PORT & then
    SERVER_PID=$!
    echo "Local HTTP server started on port $PORT"
    echo "My curriculum vitae is being served at: http://localhost:$PORT/src/index.html"
else
    echo "Failed to start local HTTP server"
    exit 1
fi

# Function to handle script termination and cleanup
cleanup() {
    echo "Stopping local HTTP server..."
    kill $SERVER_PID
}

# Register cleanup function to be called on script exit
trap cleanup EXIT

# Wait indefinitely to keep the script running
wait
