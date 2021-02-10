#!/usr/bin/bash

printf "***************************$(tput bold)hy, $(tput setaf 6)$USERNAME$(tput sgr0)****************************"
function safe_c() {
    cd ~/Projects/ePustakalay
    if pgrep python;
    then
        pkill python
        printf "$(tput bold)$(tput setaf 9)Python Exit.....\n"
	printf "$(tput bold)$(tput setaf 10)Bye Bye $USERNAME 👋$(tput bel)\n"
    fi
}
trap safe_c SIGINT
trap safe_c EXIT
.venv/bin/python backend/manage.py runserver 0.0.0.0:8000 &
cd frontend && npm start

