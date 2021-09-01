pipeline {
    agent any
    environment {
	DOCKER_LOGIN = credentials('dockerhub_id')
	install = 'true'
	DATABASE_URI = credentials('DATABASE_URI')
	SECRET_KEY = credentials('SECRET_KEY')
    }
    stages {
	stage ('Install Requirements') {
	    steps {
		script {
		    if (env.install== 'false'){
			sh 'bash installation-reqs.sh'
		}
	    }
	}
    }
	stage ('Testing') {
	    steps {
		sh 'sudo apt-get update'
		sh 'sudo apt-get install python3-venv python3-pip -y'
		sh 'cd frontend'
		sh 'pip3 install -r requirements.txt'
		sh 'python3 -m pytest --cov application'
		sh 'cd ..'
		sh 'cd backend'
		sh 'pip3 install -r requirements.txt'
		sh 'python3 -m pytest --cov application'
		sh 'cd ..'
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