#!/usr/bin/bash

printf "$(tput bold)hy, $(tput setaf 6)$USERNAME$(tput sgr0)"
function safe_c() {
    if pgrep python; 
    then 
        pkill python
        printf "\n$(tput bold)$(tput setaf 1)Python Exit....." 
    fi
    printf "\n\n$(tput bold)$(tput setaf 1)Bye Bye 👋$(tput bel)\n"
}

trap safe_c SIGINT

python backend/manage.py runserver 0.0.0.0:8000 &
cd frontend && npm start