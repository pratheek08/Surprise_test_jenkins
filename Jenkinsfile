pipeline {
    agent any

    stages {
        // Stage 1: Clone Repository from GitHub
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/pratheek08/Surprise_test_jenkins', branch: 'main'
            }
        }

        // Stage 2: Create Virtual Environment and Install Dependencies
        stage('Install Dependencies') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
                
                // Install dependencies inside the virtual environment
                sh './venv/bin/pip install -r requirements.txt'
                
                // Ensure setuptools is installed in the virtual environment
                sh './venv/bin/pip install setuptools'
            }
        }

        // Stage 3: Run Tests (optional)
        stage('Run Tests') {
            when {
                expression {
                    return fileExists('tests')
                }
            }
            steps {
                // Run tests inside the virtual environment
                sh './venv/bin/pytest tests/'
            }
        }

        // Stage 4: Build Artifact (Python package)
        stage('Build Artifact') {
            steps {
                // Make sure setuptools is explicitly used before building
                sh './venv/bin/pip install setuptools'
                
                // Build the Python package using setup.py
                sh './venv/bin/python setup.py sdist'
            }
        }

        // Stage 5: Archive Build Artifacts
        stage('Archive Artifact') {
            steps {
                // Archive the generated artifact (e.g., .tar.gz)
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
}
