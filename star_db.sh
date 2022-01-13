
# config
C_NAME="our_dke_db"
DB_ROOT_PW=";lakdsjl;akjdlkajsdl;jfasd"


# before <container name>
before(){
    echo "before..."
    docker stop "$1"
    docker rm "$1"
    echo ""
}

# start db
start_db(){
    echo "start db..."
    docker run \
        --detach \
        --name "$1" \
        --env MARIADB_USER=example-user \
        --env MARIADB_PASSWORD=my_cool_secret \
        --env MARIADB_ROOT_PASSWORD=$2  \
        mariadb:latest
    echo ""
}


test(){
    echo "do some test..."
    sudo apt install -y mysql-client
    sleep 10
    mysql -u root -h "172.17.0.2" -p$1 -e "show databases;"
    echo ""
}

before "${C_NAME}"
start_db "${C_NAME}" "${DB_ROOT_PW}"
test "${DB_ROOT_PW}"