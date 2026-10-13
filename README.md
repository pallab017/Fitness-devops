# ACEest Fitness & Gym --- DevOps Assignment

A Flask-based fitness application used to demonstrate application
testing, containerisation, and Continuous Integration (CI) with GitHub
Actions and Jenkins.

## Project overview

The project packages a small Python web application with automated tests
and a Docker image. The CI workflow runs code checks and tests, builds
the Docker image, and runs the tests inside the container.

## Technology stack

-   **Python 3.9**
-   **Flask** --- web application framework
-   **pytest** --- automated tests
-   **flake8** --- selected Python lint checks
-   **Docker** --- container image and runtime
-   **GitHub Actions** --- repository-triggered CI workflow
-   **Jenkins** --- CI pipeline execution

## Repository structure

``` text
Fitness-devops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
└── test_app.py
```

## Prerequisites

For local execution, install Python 3.9 or a compatible Python version
supported by the dependencies. To build and run the container, install
Docker Desktop or Docker Engine. Git is required to clone the
repository.

## Run the application locally

1.  Clone the repository and enter the project directory:

    ``` bash
    git clone https://github.com/pallab017/Fitness-devops.git
    cd Fitness-devops
    ```

2.  Create and activate a virtual environment.

    **Linux/macOS:**

    ``` bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    **Windows PowerShell:**

    ``` powershell
    py -3.9 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

3.  Install the application dependencies:

    ``` bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  Start the application:

    ``` bash
    python app.py
    ```

5.  Open the local address shown by Flask in your browser. The project
    is configured to use port `5000` in the Docker container; if running
    locally, use the host and port printed by the application.

Stop the application with `Ctrl+C`.

## Manual testing

Run the following commands from the project root with the virtual
environment activated:

``` bash
pip install pytest
python -m pytest -v
```

The test suite is stored in `test_app.py`. A successful test run reports
the individual test cases as passed and ends with a summary similar to
`6 passed` for the current suite.

You can also check the application endpoints in a browser or with `curl`
while the app is running. The project has been checked with the
following endpoints:

``` bash
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/programs
```

If your local app uses a different host or port, adjust the URLs
accordingly. The endpoint checks depend on the routes implemented in
`app.py`.

## Docker: build and run

Build the image from the repository root:

``` bash
docker build -t aceest-fitness:1.0 .
```

Run the container and publish container port `5000` on local port
`5000`:

``` bash
docker run --rm -p 5000:5000 aceest-fitness:1.0
```

In a separate terminal, verify the health and programs endpoints:

``` bash
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/programs
```

To run the automated tests inside the built image:

``` bash
docker run --rm --entrypoint python aceest-fitness:1.0 -m pytest -v
```

The Dockerfile copies both `app.py` and `test_app.py` into the image so
the test suite is available for this container test command.

## GitHub Actions integration

Workflow file: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

The workflow is configured to run on pushes and pull requests targeting
the `main` branch. The pipeline performs these steps:

1.  Checks out the repository.
2.  Sets up Python 3.9.
3.  Installs the application requirements and the CI tools (`pytest` and
    `flake8`).
4.  Runs selected `flake8` error checks against `app.py` and
    `test_app.py`.
5.  Runs the pytest suite.
6.  Builds the Docker image.
7.  Runs pytest inside the Docker image.

To review execution results, open the repository's **Actions** tab:

[View GitHub Actions
runs](https://github.com/pallab017/Fitness-devops/actions)

A green successful run indicates that the configured workflow steps
completed successfully for that commit.

## Jenkins integration

Jenkins was used to execute the project CI pipeline, including the
automated test stage. The recorded successful run showed the pytest
tests passing and the build finishing with `Finished: SUCCESS`.

**Configuration note:** the repository structure currently contains no
`Jenkinsfile`. Therefore, describe the Jenkins pipeline as configured in
the Jenkins UI unless a `Jenkinsfile` is added to the repository. A
Jenkins UI pipeline configuration is not automatically
version-controlled with this project.

Typical pipeline stages for this project are:

1.  Check out the source code from GitHub.
2.  Prepare the Python environment and install dependencies.
3.  Run automated tests with `python -m pytest -v`.
4.  Build the Docker image, if Docker is available to the Jenkins agent.
5.  Report the build result in the Jenkins console.

Only list stages as part of your actual Jenkins configuration if they
are present in the job. To make the pipeline reproducible from the
repository, consider adding a `Jenkinsfile` and configuring Jenkins to
use **Pipeline script from SCM**.

## Troubleshooting

-   **`pytest` is not found:** activate the virtual environment and run
    `python -m pip install pytest`, then use `python -m pytest -v`.
-   **Port 5000 is already in use:** stop the other process or publish a
    different host port, for example `-p 5001:5000`, then browse to
    `http://127.0.0.1:5001`.
-   **Docker command fails:** confirm Docker is installed and its daemon
    is running.
-   **Tests fail in CI:** open the failed GitHub Actions run and inspect
    the first failing step and its console output.
-   **Jenkins cannot run Docker commands:** confirm Docker is installed
    and accessible to the Jenkins agent account, and that the job is
    configured with the required permissions.

## Evidence and links

-   **GitHub repository:** https://github.com/pallab017/Fitness-devops
-   **GitHub Actions workflow:**
    https://github.com/pallab017/Fitness-devops/blob/main/.github/workflows/ci.yml
-   **GitHub Actions run history:**
    https://github.com/pallab017/Fitness-devops/actions

## Summary

This project demonstrates a basic DevOps workflow for a Flask
application: source control in GitHub, automated tests with pytest,
selected lint checks with flake8, containerisation with Docker, and CI
execution through GitHub Actions and Jenkins.
