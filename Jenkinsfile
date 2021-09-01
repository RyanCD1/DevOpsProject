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
		sh 'pip3 install -r frontend/requirements.txt'
		sh 'cd frontend'
		sh 'cd tests'
		sh 'python3 -m pytest --cov application'
		sh 'cd ..'
		sh 'cd ..'
		sh 'pip3 install -r backend/requirements.txt'
		sh 'cd backend'
		sh 'cd tests'
		sh 'python3 -m pytest --cov application'
		sh 'cd ..'
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
