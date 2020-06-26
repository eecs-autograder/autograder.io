# Contributing to Autograder.io

Contributions to Autograder.io are always welcome! Autograder.io's source code is divided across a handful of repositories, including the database and API backend, the website frontend, and several supporting libraries:
- [autograder-server](../autograder-server): The database and API backend, written with Python + Django.
- [autograder-sandbox](../autograder-sandbox): A Python library used for running untrusted code in a Docker container.
- [ag-website-vue](../ag-website-vue): The website frontend, written in Typescript + Vue.
- [ag-client-typescript](../ag-client-typescript): A client library for communicating with the API, written in Typescript.
- [autograder-contrib](../autograder-contrib): Utilities for writing command-line applications that use the Autograder.io API.

## How do I report a bug or request a new feature?
In general, bug and feature requests should be made by emailing help@autograder.io or by using our [central issue tracker](https://github.com/eecs-autograder/autograder.io/issues). If a lead developer suggests that you create your issue in the issue tracker of a specific repo, then you may do so.

After being discussed, issues in the central tracker will be moved or linked to parallel issues in the repositories where the bug fix or feature request will be implemented.

### Website
Before reporting a bug or requesting a new feature, please search our [central issue tracker](https://github.com/eecs-autograder/autograder.io/issues) to see if a matching issue already exists. If not, you can either contact us at help@autograder.io or create a new issue. When using the issue tracker, please __DO NOT DISCLOSE PRIVATE STUDENT DATA__. Similarly, if you find a security issue, contact us directly rather than posting in the issue tracker.

In your issue description, please include:
- The output from your browser's JavaScript console (see https://webmasters.stackexchange.com/questions/8525/how-do-i-open-the-javascript-console-in-different-browsers).
- A list steps you took to arrive at the problem.
- A brief description of what you expected to happen.
- A screenshot and brief description showing what actually happened.

### API Backend
If you are writing an external tool that uses the Autograder.io API and encounter a bug, please search our [central issue tracker](https://github.com/eecs-autograder/autograder.io/issues) to see if a matching issue already exists.

In your issue description, please include:
- A minimal source code snippet that can be used to reproduce the issue.
- The stack trace and HTTP response body that your program produces.

## What issues can I help with?
In general, any open issue is fair game. Issues labelled "size-small" or "good first issue" are likely a good starting point for new developers. Once you've found an issue you'd like to work on, please comment on the issue stating your desire to do so.

### I'm looking for something more challenging. Any suggestions?
Yes! Here are a few more involved issues that we'd graciously accept help with:
- (This list will be updated periodically)

## Can I help write documentation?
Yes! Currently, our biggest documentation priority is filling in the gaps in our [UI documentation](https://eecs-autograder.github.io/autograder.io/). The markdown source code for the site can be found in the [docs folder](./docs) of this repo. Simply fork this repo, make your desired changes, and then make a pull request for your changes to be merged.

## How do I set up my development environment?
For backend development, see the [README](https://github.com/eecs-autograder/autograder-server#server-dev-setup) in the [autograder-server repo](https://github.com/eecs-autograder/autograder-server).

For frontend development, see the [README](https://github.com/eecs-autograder/ag-website-vue#setup) in the [ag-website-vue repo](https://github.com/eecs-autograder/ag-website-vue).

## Coding Standards
When contributing to the `autograder-server` or `autograder-sandbox` repositories, please read our [Python coding standards](./coding_standards_python.md).

When contributing to the `ag-website-vue` or `ag-client-typescript` repositories, please read our [Typescript/Vue coding standards](./coding_standards_typescript_vue.md).

Some repositories have additional coding standards documents beyond the language standards mentioned above:
- [autograder-server](https://github.com/eecs-autograder/autograder-server#coding-standards)
- [ag-website-vue](https://github.com/eecs-autograder/ag-website-vue#coding-standards)
