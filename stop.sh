printf "\n*************TEARING DOWN CONTAINER AND IMAGE*************\n"

docker compose down --rmi all

printf "\n*************END OF SHELL RUN**************\n"