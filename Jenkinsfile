pipeline {
    agent any
    environment {
	DOCKER_LOGIN = credentials('dockerhub_id')
	install = 'true'
	rollback = 'false'
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
		sh 'cd frontend && python3 -m pytest --cov application'
		sh 'pip3 install -r backend/requirements.txt'
		sh 'cd backend && python3 -m pytest --cov application'
	    }
	}
	stage ('Build') {
	    steps {
		script{
                    if (env.rollback == 'false'){
                        image = docker.build("[rdon11/DevOpsProject")
                    }
                }
	    }
	}
	stage ('Push') {
	    steps {
		script {
		    if (env.rollback == 'false'){
                	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id'){
                            image.push("latest")
		    }
		}
	    }
	}
    }
	stage ('Deploy') {
	    steps {
		sh 'docker stack deploy --compose-file docker-compose.yaml project-stack'
	    }
	}
    }
}
