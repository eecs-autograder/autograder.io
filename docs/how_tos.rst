How-tos and FAQ (WIP)
=====================
This page is a work in progress. Contributions are welcome through
pull requests to our
`GitHub repository <https://github.com/eecs-autograder/autograder.io/tree/master/docs>`_.

Clone a Course or Project for a New Term
------------------------------------------
To clone a project, see :ref:`copy-course`.

To clone a project, navigate to the course admin page and click on the
"Projects" tab. Click the "copy" icon for the project you want to clone.

.. image:: /pics/how_tos/copy_project.png

Choose a new name for the project if you want the new project to be created
in the current course. Alternatively, you can choose to have the new project
be created under another course that you are an administrator for.

.. image:: /pics/how_tos/copy_project_other_course.png

Let students submit even if they're not in the roster
-----------------------------------------------------
By default, students must be explicitly listed in the student roster in order
to submit and form groups. There are two quick steps to changing this behavior:

1. Restrict guests to your email domain (Optional, once per course)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Guests are users who are allowed to submit an assignment but are not in the
roster for the course. If your institution has a specific email domain
(e.g. `@umich.edu`) we recommend setting the "Guest usernames must end with"
field to that email domain.

First, navigate to the admin page for your course.

.. image:: /pics/set_up_course/landing_page_gear.png

Then set the "Guest usernames must end with" field to your institution's email
domain.

.. image:: /pics/how_tos/allowed_guest_domain.png

2. Enable the "Anyone with the link can submit" project option
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Navigate to the admin page for your project by clicking the gear icon next to
the project name.

.. image:: /pics/how_tos/course_admin_projects_gear.png

Then, select the "Anyone with the link can submit" option.

.. image:: /pics/how_tos/anyone_with_link_can_submit.png

.. Grant an extension
.. ------------------

.. Edit group members or merge two groups
.. --------------------------------------

.. Rerun a test case or submission
.. --------------------------------

.. Why do I get "permission denied" when I run my script with ``./my_script.sh``?
.. ------------------------------------------------------------------------------

.. Can I use MATLAB?
.. -----------------
