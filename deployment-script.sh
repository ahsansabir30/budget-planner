if [ -d devops-project ]; then
    cd devops-project && pull origin dev
else
    git clone --single-branch --branch dev https://github.com/ahsansabir30/devops-project.git devops-project
    cd devops-project 
fi

sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
