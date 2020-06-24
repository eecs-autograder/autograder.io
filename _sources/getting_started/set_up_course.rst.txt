Setting Up Your Course
======================

First-time course creation
--------------------------
If you are creating a course for the first time, contact `help@autograder.io`
(or your system administrator if running on your institution's servers)
for assistance.

Copying a Course from a Previous Term
-------------------------------------
To copy a course from a previous term, click the "copy" icon for the course you want to clone.

.. image:: /pics/set_up_course/landing_page_copy.png

Add Admin, Staff, and Student Users
-----------------------------------
Click the gear icon for your new course to enter the course admin page.

.. image:: /pics/set_up_course/landing_page_gear.png

Next, hover over the "Roster" tab and click on one of the roles listed in the
dropdown menu. The roles are as follows:

* **Admin**: Admins have full edit permissions for the course.
  That includes changing user permissions, editing projects and test cases, etc.
  Admins can also look up students' submissions with any feedback level.
  Admins also have the same privileges as staff users.
* **Staff**: Staff can submit their own code unlimited times with maximum feedback.
  Staff can look up students' submissions, but with restricted feedback as configured by admins.
* **Student**: Students can view and submit to all published projects in the course.
  The can also form groups with other students (where allowed by the project settings).
* **Handgrader**: Handgraders can access the handgrading interface for projects
  in the course and therefore grade students' submissions according to a rubric
  configured by admins.

Any user with none of the roles listed above is considered a guest.
Guests can only access projects that are configured to allow guests,
and can only form groups with other guests.

To add users to the roster you selected, paste a newline-separated list of
**email addresses** into the text box and click "Add to Roster".

.. image:: /pics/set_up_course/roster.gif
