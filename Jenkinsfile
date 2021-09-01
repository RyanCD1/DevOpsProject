pipeline {
    agent agent1
    environment {
	DATABASE_URI = Credentials('DATABASE_URI')
	SECRET_KEY = Credentials('SECRET_KEY')
    }
    stages {
	stage ('Install Requirements') {
	    steps {
		sh './installation-reqs.sh'
	    }
    }
	stage ('Testing') {
	    steps {
		sudo apt-get update
		sudo apt-get install python3-venv python3-pip -y
		cd frontend
		pip3 install -r requirements.txt
		python3 -m pytest --cov=application
		cd ..
		cd backend
		pip3 install -r requirements.txt
		python3 -m pytest --cov=application
		cd ..
	    }
	}
	stage ('Build') {
	    steps {
		sh 'docker-compose build'
	    }
	}
	stage ('Push') {
	    steps {
		sh 'docker-compose push'
	    }
	}
	stage ('Deploy') {
	    steps {
		sh 'docker stack deploy --compose-file docker-compose.yaml DevOpsProject'
	    }
	}
    }
}
