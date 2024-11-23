# Sample-Jenkins
Deploying Python app with Jenkins.
This project demonstrates setting up a basic Continuous Integration (CI) pipeline to build and test a simple Python application.

## Set Up Jenkins Pipeline:
1- Log in to Jenkins and click on "New Item".

2- Enter a name for your project (e.g., Sample Python CI) and select "Pipeline".

3- Configure the pipeline:
  Choose pipeline script and write the content of "pipeline_script" in that.

4- Save and Click build to trigger pipeline.

## What to Expect:

1 - Clone Repository: Jenkins pulls the Python project from GitHub.

2 - Install Dependencies: Jenkins installs pytest from the requirements.txt file.

3 - Run Tests: Jenkins runs the unit tests in test_app.py and generates a report.

4 - Post-Processing: The test results (report.xml) are published in Jenkins for review.

## As a result:
Once the build is complete, go to "Build History" and click on the latest build.
Check the "Test Results" to see the status of the tests.
Jenkins will display whether the pipeline succeeded or failed.

