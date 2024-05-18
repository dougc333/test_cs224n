

to install psycopg2 for psql on mac. We dont need native install of posgresql because we are using docker
but we need the command line tool psql. To install psql we need psycopg2. When homebrew installs psycopg2 it
installs and runs as a service postgresql. You have to manually find the pid and shut this off using brew service stop. 


brew install libpq --build-from-source
brew install openssl

export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib -L/opt/homebrew/opt/libpq/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include -I/opt/homebrew/opt/libpq/include"

pip3 install psycopg2
CAREFUL: after installing this brew installs postgres and starts an insance of the db. 
>brew services postgres stop

make sure .zshrc env variable PATH includes /opt/homebrew/bin
start postgres docker container
% docker run --name basic-postgres --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=asdf -e PGDATA=/var/lib/postgresql/data/pgdata -v /tmp:/var/lib/postgresql/data -p 5432:5432 -it postgres:14.1-alpine
% docker exec -ti basic-postgres psql -U postgres
verify the table is created: 
postgres=# \dt
            List of relations
 Schema |    Name     | Type  |  Owner   
--------+-------------+-------+----------
 public | order_lines | table | postgres
(1 row)

This verifies the table was created with sqlalchemy


use psycopg to connect to database first
ODBC stype library

 /opt/homebrew/bin/brew services start postgres 

