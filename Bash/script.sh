echo "starting update"
#variables used on the excecution
dockerimage=pythonmonitoring
dockertag=latest
#change directory to the root
cd ..
#bringing the repository to the latest version
git pull
#docker build
