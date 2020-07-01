pipeline{
  agent any
    stages{
        stage('One'){
	        steps{
		      echo 'hi, this is stage one'
		  }}
	    stage('two'){
	        steps{
		      input('hi, this is stage two,do you want proceed?')
		  }
		  }
	    stage('three'){
		    when {
			    not{
				    branch "master"
				}}
	        steps{
		      echo 'hi, this is stage three'
		  }
		  }
		stage('four'){
		    parallel {
			    stage('auto test1'){
				    steps {
					echo "Running the auto test"
					}
				}
				stage("auto test2"){
				agent{
				   docker{
				      reuseNod false
					  image 'ubuntu'
				   }
				}
				steps{
				   echo 'running auto test2'
				 }
				}
			    }
		  }
  }
}
