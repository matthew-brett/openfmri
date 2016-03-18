#######################
The openfmri data model
#######################

********
Overview
********

A *dataset* contains *subjects*.  Each subject has had functional images
collected while they are performing one or more *tasks*.  They may have had
one or more functional *runs* (see :ref:`runs`) while performing each task.
For each subject there is one or more *model* of the way that the tasks have
influenced the neural activity of the subject.

*******
Objects
*******

* Dataset;
* Subject;
* Model;
* Run;
* Task;

*********
Numbering
*********

In what follows, a number written as ``XXX`` is an integer written as a string
with 3 digits and left zero padding, e.g. ``003, 052, 105``.  The integers
identify element in a sequence, such as a sequence of datasets or subjects or
scans.  The first element in the sequence is always 1.  We will call these
*ZPINTs*.

************
Image format
************

All anatomical and functional scans are in compressed single file NIfTI_ image
format.  They therefore all have file extensions ``.nii.gz``.  You can read
these using the nibabel_ Python package.  If you need the uncompressed image
for any reason, the usual ``gunzip`` Unix command line utility will give you a
valid ``.nii`` file from the ``.nii.gz`` file.

.. _runs:

****************
A functional run
****************

A run is a continuous sequence of functional brain volumes.  The scan begins
acquiring data at the beginning of a functional run, and stops at the end.
In the OpenFMRI directories, runs are always stored as four dimensional NIfTI
images, where the first three dimensions of the image are spatial (e.g. left
to right, anterior to posterior, inferior to superior), and the last dimension
is time.  For example, here we load an OpenFMRI image containing a single run::

    >>> import nibabel as nib
    >>> img = nib.load('ds114/sub005/BOLD/task001_run001/bold.nii.gz')
    >>> img.shape
    (64, 64, 30, 76)

This is sequence of 76 brain volumes, each of shape (64, 64, 30).  Slicing
over the last axis gives the brain volume corresponding to a particular time::

    >>> vol0 = img.get_data()[:, :, :, 0]

******
A task
******

A *task* in OpenFMRI is an identifier for a set of stimuli shown to the
subject or responses made by the subject, or combinations of stimulus and
response, that the experimenter believed would change the functional brain
activity.

A task may be modeled in different ways and therefore with different *models*.

When OpenFMRI defines a model for a task, it categorizes the stimuli and
responses for a task into *conditions*.

Thus, a model is comprised of a set of conditions for each task.

This might be clearer later on in the section :ref:`models`.

*******
Dataset
*******

A Dataset has a corresponding dataset directory.

A dataset directory has directory name ``dsXXX`` (where ``XXX`` is a ZPINT),
e.g. ``ds003`` for dataset number 3.

A Dataset may contain

* subject directories (see :ref:`subject`);
* ``scan_key.txt``: information about the scans in the dataset, such as the TR;
* ``study_key.txt``: information about the experimental protocol, such as the
  experiment name;
* ``task_key.txt``: file associating task numbers (see below) with task names.
* ``model_key.txt``: file associating model numbers (see below) with model
  names.

.. _subject:

*******
Subject
*******

The subject directory contains all information for one subject.

The subject directory has name of form ``subXXX`` where ``XXX`` is a ZPINT
|--| e.g. ``sub001`` for the first subject.

A subject directory may contain:

* an ``anatomy`` directory, containing anatomical images;
* a ``BOLD`` directory containing a directory tree of functional images;
* a ``model`` directory containing a directory tree of model definitions.

*****************
Anatomy directory
*****************

The anatomy directory contains images corresponding to one or more anatomical
scans for the containing subject.  The scans have names ``highresXXX`` where
``XXX`` is a ZPINT.

The original scan in NIfTI format has filename ``highresXXX.nii.gz``, e.g.
``highres001.nii.gz``.

For each original scan, there may be:

* ``highresXXX_brain_mask.nii.gz``: an image with the same dimensions as
  ``highresXXX.nii.gz`` but containing values between 0 and 1 expressing
  whether the corresponding location is inside (1) or outside (0) the brain;
* ``highresXXX_brain.nii.gz``: a copy of ``highresXXX.nii.gz`` where values
  outside the brain (mask values of 0) have been set to 0.

For example, here is the list of files in ``ds114/sub002/anatomy``::

    highres001.nii.gz
    highres001_brain.nii.gz
    highres001_brain_mask.nii.gz
    highres002.nii.gz

**************
BOLD directory
**************

The ``BOLD`` directory contains one subdirectory per functional run.

The subdirectories are named after the *tasks* for this experiment.  There may
be more than one run for which the subject performs the task.  For example,
here is a directory listing for ``ds114/sub002/BOLD``::

    task001_run001/
    task001_run002/
    task002_run001/
    task002_run002/
    task003_run001/
    task003_run002/
    task004_run001/
    task004_run002/
    task005_run001/
    task005_run002/

So ``task003_run002`` contains the second functional scan during which the
subject performed task 3.

Within each of these directories named for the (task number, repeat number),
there is a NIfTI image with the functional data, called ``bold.nii.gz``.

There may also be a subdirectory called ``QA`` containing various metrics from
processing the ``bold.nii.gz``.

.. _models:

****************
Models directory
****************

The models directory of a subject contains one subdirectory per model.

Each model is a different way of defining how the task performed by the
subject can by broken up into *conditions*.

There may be one or more model per subject.

For example, the directory ``ds114/sub002/models`` contains the following
subdirectories::

    model001/
    model002/

The subdirectory for each model contains a further subdirectory called
``onsets``.  This subdirectory in turn contains one subdirectory per (task
number, repeat number) pair.  Here is the listing of
``ds114/sub002/model/model002/onsets``::

    task001_run001/
    task001_run002/
    task002_run001/
    task002_run002/
    task003_run001/
    task003_run002/
    task004_run001/
    task004_run002/
    task005_run001/
    task005_run002/

Within each of these (task number, repeat number) directories, there is one
file per *condition*.  Here is the contents of
``ds114/sub002/model/model002/onsets/task003_run001``::

    cond001.txt
    cond002.txt
    cond003.txt

The condition files are text files with one row per *event*.  An event is an
individual stimulus or response.  For each event, the condition file gives the
onset time of the event, in seconds from time the scanner began collecting
data for the first volume in the functional run. The file also gives the
duration of the event, in seconds, and the amplitude of the event.  For
example, here is the contents of
``ds114/sub002/model/model002/onsets/task003_run001/cond001.txt``::

    10      15.000000       1
    100     15.000000       1
    190     15.000000       1
    280     15.000000       1
    370     15.000000       1

This condition file says that there were five events, starting at 10, 100,
190, 280 and 370 seconds after the start of scanning.  Each of these events
lasted 15 seconds.  They were all of equal amplitude (here, 1 in arbitrary
units).

Events can also differ in amplitude.  For example, imagine the event was a
flash of light.  There might be flashes with low intensity, flashes of medium
intensity and flashes of high intensity.  In that case the condition file
might have amplitude values of 1 for the low-intensity flashes, 2 for the
medium intensity flashes, and 3 for high-intensity flashes.

.. include:: links_names.inc
