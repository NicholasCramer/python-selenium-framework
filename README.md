# python-selenium-framework

 This project is a basic framework setup for running Selenium WebDriver tests in Python with the Pytest unit testing framework.
 This framwork will also be integrated with Jenkins CI tool

 ## Set up instructions

### Jenkins CI setup:

Step 1: Set up local user and allow to run as a service
- Navigate to Local Security Policy
- Under Security Settings -> Local Policies -> User Rights Assignment select Log on as a service
  <img width="590" alt="Step1_EnableServiceLogon" src="https://github.com/NicholasCramer/python-selenium-framework/assets/73135495/a939a3ff-c7ce-4386-b11a-b69070dd51d2">
- Click Add User or Group, enter the name of the account you would like to allow to logon as a service and click Check Names to verify the correct account. Then click ok top add the user to the group.

Step 2: Install Java Development Kit (JDK)
- Note: By Fall 2024, Jenkins will require JDK 17 or 21
- I used the OpenJDK distribution from Adoptium called Eclipse Temurin found here: https://adoptium.net/
- During installation, in addition to the other selected default features, select Set JAVA_HOME variable
  <img width="387" alt="Step2_InstallJDK" src="https://github.com/NicholasCramer/python-selenium-framework/assets/73135495/f64e7cff-10fd-4873-9c61-f7051ee04448">
- Proceed with installation


Step 3: Set the Path for the Environmental Variable for JDK
- Edit your system environment variables
  - Under system variables, find JAVA_HOME and edit the value so there is no trailing /
    <img width="454" alt="Step3_ModifyEnvironmentalVariables" src="https://github.com/NicholasCramer/python-selenium-framework/assets/73135495/ef808966-d699-41fe-9db0-6a242a905a90">  
    click OK
  - Under System variables, find Path and click edit. Update the path reference for your JDK to %JAVA_HOME%\bin  
    Before:  
    <img width="440" alt="Step3_PathReference" src="https://github.com/NicholasCramer/python-selenium-framework/assets/73135495/21a8c9ff-d6c2-42ba-813b-ac3febd320f3">  
    After:  
    <img width="437" alt="Step3_PathReference_JavaHome" src="https://github.com/NicholasCramer/python-selenium-framework/assets/73135495/9056d089-f8d0-4b51-8a08-712133d33eb3">  
    Click OK and exit System Variables.

 - Run command prompt as administrator and run the following commands to verify installation of the JDK and update of system variables:
  - java -version
  - echo %JAVA_HOME%
  - echo %PATH%

Step 4: Download and Install Jenkins
- Run Jenkins installer and provide service logon credentials of the account from Step 1
- Provide port number you want the service to run on
- Provide the path to the JDK
- Select Install

The Jenkins service can be stopped and started via command line with the following commands:
- net stop jenkins
- net start jenkins

Step 5: Create Jenkins Job


```

### Step 2: 
