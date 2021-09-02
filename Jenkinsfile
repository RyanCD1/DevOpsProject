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
		sh 'cd frontend && python3 -m pytest --cov application > frontend-test-report.xml'
		sh 'pip3 install -r backend/requirements.txt'
		sh 'cd backend && python3 -m pytest --cov application > backend-test-report.xml'
	    }
	}
	
	stage ('Build') {
	    steps {
		script{
                    if (env.rollback == 'false'){
                        frontimage = docker.build("rdon11/project-frontend")
			backimage = docker.build("rdon11/project-backend")
                    }
                }
	    }
	}
	stage ('Push') {
	    steps {
		script {
		    if (env.rollback == 'false'){
                	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id'){
                            frontimage.push("latest")
			    backimage.push("latest")
		    }
		}
	    }
	}
    }
	stage ('Deploy') {
	    steps {
		sh 'docker-compose up -d --build'
	    }
	}
    }

    post {
        always {
	    archiveArtifacts artifacts: 'frontend/**/*.xml, backend/**/*.xml', fingerprint: true
        }
    }
}
