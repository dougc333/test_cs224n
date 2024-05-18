#!/bin/zsh
echo "export  doesnt work, FLASK_APP is set in ~/.zshenv"
printf "export FLASK_APP=microblog.py not working"
printf "use python-dotenv and remove the .zshenv fle for a local .flaskenv file"


