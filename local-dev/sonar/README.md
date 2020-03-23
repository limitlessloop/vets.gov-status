# SonarQube
[SonarQube](https://www.sonarqube.org/) is a static analysis tool for source code. This directory contains a docker-compose file which can be used to bring up a local instance of SonarQube.

## Setup

### To Start...
To fire up your sonar environment, navigate to the `local-dev/sonar` directory and execute one of the following:

```
# Each of these commands starts the SonarQube environment, just in different ways.

# - Outputs the logs directly to your console
$ docker-compose up

# - Starts the environment in a separate process, so you don't have the running process in your console.
$ docker-compose up -d

# - Starts the environment in a separate process, and rebuilds the image
$ docker-compose up -d --build 
```

### To Bring Down...
There are different methods to bring down your sonarqube environment, but which one you execute depends on what you want to do. Choose one of the following based on your goals...

```
# Stops the containers
$ docker-compose down

# Stops the containers and removes all associated images. You'd want to do this if you want to do a fresh build of your containers, or made a change locally and want to test it.
$ docker-compose down --rmi all

# Your sonarqube environment is set up to persist your scans. If you want to get rid of that scanning history, execute the following...
$ docker-compose down -v

# Note that you can get clean out the volumes and the associated images with the following...
$ docker-compose down --rmi all -v
```

## Reporting on your code
To use SonarQube, make sure it is running (per instructions above), then invoke

```
$ ./run-tests.sh && mvn sonar:sonar
```

From the base directory of the repo. This will make sure the latest test case results are imported and kick off the analysis. You can then log into Sonar, using admin credentials admin/admin. The results will be persisted so you can compare over time. Sonar is useful for detecting code smells and duplicated code that you may want to address.

