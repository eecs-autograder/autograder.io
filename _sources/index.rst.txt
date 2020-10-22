Autograder.io
=============

Autograder.io is an open-source automated grading system that lets programming
instructors focus on writing high-quality test cases without worrying about
the details of how to run them. Autograder.io is primarily developed and
maintained at the Computer Science department of the University of Michigan,
where it supports 4600 students per semester spread across a dozen courses.

This documentation is intended for instructors. If you are a student,
please contact your instructor for assistance.

.. rubric:: Autograder.io offers:

* State-of-the-art security using Docker containers as a foundation.
* Insulating sensitive instructor files from student code and preventing information leakage.
* A sophisticated, highly customizable feedback system.
* Students can work and submit in groups.
* Elegant displaying of test results, including output diffs.
* Flexible grading policy and deadline options.

This documentation is a work in progress. Contributions are welcome through
pull requests to our
`GitHub repository <https://github.com/eecs-autograder/autograder.io/tree/master/docs>`_.

.. toctree::
    :caption: Getting Started

    getting_started/set_up_course
    getting_started/create_first_project
    getting_started/adding_test_cases
    getting_started/final_steps

.. toctree::
    :caption: Topics

    how_tos
    topics/hard_and_soft_deadlines
    topics/custom_sandbox_images
    topics/bonus_submissions_and_late_days
    topics/handgrading
    topics/verifying_email_receipts
..    topics/mutation_testing
..    topics/advanced_test_case_settings
