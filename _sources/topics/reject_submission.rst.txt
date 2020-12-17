Rejecting Submissions that Fail Required Checks
===============================================
In some situations, instructors may want to reject a submission that fails
to meet certain criteria. A rejected submission will NOT count towards the
student's daily limit, nor will it use a student's bonus submission tokens.

This feature can be enabled with the following steps:

1. Add a test suite and move it so that it is the **FIRST** test suite for your
   project.
2. Set the setup command for that suite so that it performs your desired checks.
3. Check the "Reject submission if setup fails" box just below the setup command.

.. image:: /pics/topics/reject_submission/reject_submission_config.png

If a student submission is rejected, the student will see something akin to
this on the submission page:

.. image:: /pics/topics/reject_submission/rejected_submission.png

We recommend setting the feedback settings for this setup command to "Public"
so that students can see why their submission was rejected.

Caveat: Late Day Tokens
-----------------------
If a student uses a late day token and that submission is rejected, the late
day token will NOT be refunded. However, the student will still be able to
continue submitting for the duration allowed by using that token.
