pipeline{
  agent any
  environment {
    PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Users\\yue.qi\\AppData\\Local\\Programs\\Python\\Python37"
	  
    }
    stages{
        stage('One'){
	        steps{
		      echo 'hi, this is stage one:get code'
		      git credentialsId: 'a57ead2d-11d7-40ec-bdc2-d1e158a5564e', url: 'https://github.com/vicky6789111/UnittestV1.0'
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
					echo "Running the auto test1"
					 bat 'cd C:/Users/yue.qi/.jenkins/workspace/PiplineTest'
					 bat 'python all_test_suite.py'
 
					}
				}
				stage("auto test2"){
				steps{
				         echo "Running the auto test2"
					 bat 'cd C:/Users/yue.qi/.jenkins/workspace/PiplineTest'
					 bat 'python all_test_suite.py'
				 }
				}
			    }
		  }
  }
}
