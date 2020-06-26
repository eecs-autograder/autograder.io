Building Custom Sandbox Images with Docker
==========================================
Autograder.io uses Docker images as its foundation for sandbox environments
used to run test cases. For information on building Docker images,
see the `Docker documentation <https://docs.docker.com/get-started/>`_ and
`Dockerfile reference <https://docs.docker.com/engine/reference/builder/>`_.

Custom Docker images must meet the following requirements to work properly
on Autograder.io:

* The image must extend one of the base images defined in the
  `base-docker-images repo <https://github.com/eecs-autograder/base-docker-images>`_
  or otherwise meet the requirements listed in that repo's README.
* The image must NOT use the `CMD` or `ENTRYPOINT` directives. Allowing these
  directives makes it harder for us to guarantee that containers created from
  the image won't exit prematurely.

For the purpose of this guide, we will use the following minimal Dockerfile:

.. code-block:: none
    :caption: Dockerfile

    FROM eecsautograder/ubuntu18:latest


Once you've successfully built your image on your local computer, go to the
admin page for your course and click on the "Sandbox Images" tab.

.. image:: /pics/topics/custom_sandbox_images/sandbox_images_tab.png

Add your Dockerfile and any other necessary files to the drop area and click
the "Build" button. When your image finishes building, it will have a generic
name of the form "New Image ..." Click on the image in the sidebar and give it
a new name.

.. image:: /pics/topics/custom_sandbox_images/rename_image.gif

To rebuild an image, click on the image name in the sidebar and scroll down to
the "Rebuild ..." section. Upload your files and click "Rebuild."

To use the new image in a test suite, navigate to the admin page for your
project. Under the "Test Cases" tab, select the test suite you want to use the
image with and select the image in the "Sandbox environment" dropdown.

.. image:: /pics/topics/custom_sandbox_images/use_custom_image.gif
