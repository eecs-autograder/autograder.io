# Autograder.io
Autograder.io is an open-source automated grading system that lets programming instructors focus on writing high-quality test cases without worrying about the details of how to run them. Autograder.io is primarily developed and maintained at the Computer Science department of the University of Michigan, where it supports 4600 students per semester spread across a dozen courses.

Autograder.io offers:
- State-of-the-art security using Docker containers as a foundation.
- Insulating sensitive instructor files from student code and preventing information leakage.
- A sophisticated, highly customizable feedback system.
- Students can work and submit in groups.
- Elegant displaying of test results, including output diffs.
- Flexible grading policy and deadline options.

This repository contains the central [UI documentation](https://eecs-autograder.github.io/autograder.io/) and [issue tracker](https://github.com/eecs-autograder/autograder.io/issues) for Autograder.io.

## For Users
**Note to students**: If you have a question about your project code or why you see different results on your local machine vs. the autograder, please contact your course staff. Please do not email the Autograder.io team, as the Honor Code prohibits us from offering such assistance.

If you are a new user, please read our [getting started guide]() for basic information on setting up your course and first project.

If you have a question about an existing feature, please see our list of [common topics]() and our [UI documentation](https://eecs-autograder.github.io/autograder.io/). If you can't find your answer there, please contact us at help@autograder.io.

### Reporting Bugs and Requesting Features
Before reporting a bug or requesting a feature, please search our [central issue tracker](https://github.com/eecs-autograder/autograder.io/issues) to see if a matching issue already exists. If not, you can either contact us at help@autograder.io or create a new issue in the central issue tracker. When using the issue tracker, please __DO NOT DISCLOSE PRIVATE STUDENT DATA__. Similarly, if you find a security issue, contact us directly rather than posting in the issue tracker.

In your issue description, please include:
- The output from your browser's JavaScript console (see https://webmasters.stackexchange.com/questions/8525/how-do-i-open-the-javascript-console-in-different-browsers).
- A list steps you took to arrive at the problem.
- A brief description of what you expected to happen.
- A screenshot and brief description showing what actually happened.

When requesting a feature, please include:
- A description of what you want to accomplish.
- The extent to which the current system lets you achieve your goal. In other words, what is missing?

After being discussed, issues will be moved or linked to parallel issues in the repositories where the bug fix or feature request will be implemented.

## Contributing
Contributions to Autograder.io are always welcome! Autograder.io's source code is divided across a handful of repositories, including the database and API backend, the website frontend, and several supporting libraries.

Contributions to the UI documentation can be made through pull requests to this repository. The source code for the UI documentation can be found in the [docs folder](./docs) of this repository.

For more information on how to contribute, please read our [contributing guide](./CONTRIBUTING.md).

## Running Autograder.io on Your Own Servers
We recommend having at least 2 server machines to run Autograder.io effectively. If that is the case, please read our [swarm deployment guide](https://github.com/eecs-autograder/autograder-full-stack/blob/master/docs/swarm_deployment.md) for instructions.

If you have a small number of users, it may be feasible to deploy Autograder.io on one robust server. In this case, please read our [single-server deployment guide](https://github.com/eecs-autograder/autograder-full-stack/blob/master/docs/production_non_swarm_setup.md) for instructions.
