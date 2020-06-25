Adding Test Cases to Your Project
=================================
For example purposes, we'll be using files with names and contents as
listed below. Please create copies of these files on your local machine as
you follow this guide. The files can also be found
`on GitHub <https://github.com/eecs-autograder/autograder.io/tree/master/docs/getting_started/code_files>`_.

**IMPORTANT**: The ``.correct`` files below should end with a blank line.

.. literalinclude:: ./code_files/test_math_funcs.py
    :caption: test_math_funcs.py

.. literalinclude:: ./code_files/math_funcs.py
    :caption: math_funcs.py

.. literalinclude:: ./code_files/print_words_test_1.in
    :caption: print_words_test_1.in

.. literalinclude:: ./code_files/print_words_test_1.correct
    :caption: print_words_test_1.correct

.. literalinclude:: ./code_files/print_words_test_2.in
    :caption: print_words_test_2.in

.. literalinclude:: ./code_files/print_words_test_2.correct
    :caption: print_words_test_2.correct

.. literalinclude:: ./code_files/student_solution.cpp
    :caption: student_solution.cpp

Upload Instructor Test Case Files
---------------------------------
In the project admin page, click on the "Instructor Files Tab" and then upload
the files **test_math_funcs.py**, **print_words_test_1.in**,
**print_words_test_1.correct**, **print_words_test_2.in**,
**print_words_test_2.correct** from the previous section.

.. image:: /pics/adding_test_cases/instructor_files.gif


Configure Files Students Should Submit
--------------------------------------
Click on the "Student Files" tab and add **math_funcs.py** and
**student_solution.cpp** as expected student files.

.. image:: /pics/adding_test_cases/expected_student_files.gif

Add Test Cases
--------------
Test cases on Autograder.io are organized into *suites*. When a student submits
their code, each suite is run in an isolated environment. Suites also provide
a *setup* step where work required by all the tests in a suite (e.g. compiling
source code) can be done just once.

Create a Test Suite with Python Unit Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Click on the "Test Cases" tab and then click the "Add Suite" button. In the
dialogue that appears, name the suite "Python Tests".

.. image:: /pics/adding_test_cases/new_test_suite.png

Scroll down to the section labelled "Instructor Files" and select
**test_math_funcs.py** from the dropdown. Similarly, select **math_funcs.py**
in the "Student Files" section.

.. image:: /pics/adding_test_cases/python_suite_instr_files.gif

Scroll to the bottom of the page and click the "Save" button.
Since we're using Python, we don't need to use the "setup" option.

Create the First Test
"""""""""""""""""""""
Next, click the "plus" sign next to the suite name in the sidebar. In the
dialogue that appears, name the test "Test Add" and set its command to
``python3 test_math_funcs.py MathFuncTestCase.test_add``.

.. image:: /pics/adding_test_cases/python_first_test.gif

Then, set the following options and click the "save" icon or the "Save" button
at the bottom of the page.

* **Expected Return Code: Zero**
  This tells us that the test is "correct" if the exit status of the program is
  zero.
* **Correct return code: 2 points**
  This tells us that the student's submission will be awarded 2 points for
  exiting with the correct status (zero in this case).
* **Feedback -> Normal -> Preset: Pass/Fail**
  This specifies that students will only see whether their code passed this
  test. Output is hidden in order to prevent our test cases from being leaked.

.. image:: /pics/adding_test_cases/python_first_test_settings.gif

"Test" the Test Case Settings
"""""""""""""""""""""""""""""
Before we make any more tests, we should make sure our first one is set up
correctly. Click on the project name at the top of the page to navigate to the
submission page. Drag ``math_funcs.py`` into the drop area and click the
"Submit" button. You will see a warning that you didn't submit all the
expected files, but that's ok. Click "Submit Anyway".

.. image:: /pics/adding_test_cases/python_first_test_submission.gif

The submission results widget reloads periodically. Since we only have one
test, we can use our browser's refresh button to see the results sooner.

Once the submission is finished grading, we'll want to
**see the same feedback students will**. Select **"Normal"** from the
"Adjust Feedback" dropdown menu to do so.

.. image:: /pics/adding_test_cases/python_first_test_results.gif

Click on the panel for "Test Add", and you'll see that under "Normal" feedback
we don't see any output from the test case. Our first test is good to go!

Clone the Test Case to Complete the Suite
"""""""""""""""""""""""""""""""""""""""""

Create a Test Suite with C++ Output Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Publish the Project
-------------------

Downloading Grades and Submitted Files
--------------------------------------
