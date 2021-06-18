function start() {
    if [[ "$OSTYPE" == "msys"* ]]; then
        python -m pip install -r requirements.txt
        python main.py
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        python3 -m pip install -r requirements.txt
        python3 main.py
    fi
}

if [[ "$1" == "--debug" ]]; then
    start
else
    garbage_variable_to_hide_output=$(start)
fi
