#!/bin/bash
#variables used on the excecution
dockerimage=pythonmonitoring
dockertag=latest
status="config.txt"
#We check the value of the .env file and see if the directory is already setup or not.
if [ ! -f $status ] 
then
    #Proceed to setup the directory project
    echo "Project has not been setup on this directory..."
    #clone of the github repo
    git clone https://github.com/JohannesSeq/SRE-Demo.git
    #Setup of the file
    cd Bash/
    statusval="setup" > config.txt
    echo "Project has been clonned and the setup has been completed!"
    cd ..
    ls
else
    #Update the files and setup the k8s cluster up and running
    echo "Project has been setup... Proceeding with the excecution."
    cd ..
    git pull
    ls
fi
echo "Excecution ended!"

#finish of the script
#change directory to the root assuming that you are running the script on the Bash folder
#cd ..

#bringing the repository to the latest version
#git pull
