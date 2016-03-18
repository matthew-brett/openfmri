#######################
The openfmri data model
#######################

*******
Objects
*******

* Dataset;
* Subject;
* Model;
* Run;
* Task;

*******
Details
*******

A Dataset has a corresponding dataset directory.

A dataset directory has a name ``dsXXX`` where ``XXX`` is an integer with left
zero padding, e.g. ``ds003`` for dataset number 3.

A Dataset may contain

* subject directories;
* ``scan_key.txt``: information about the scans in the dataset, such as the TR;
* ``study_key.txt``: information about the experimental protocol, such as the
  experiment name;
* ``task_key.txt``: file associating task numbers (see below) with task names.
* ``model_key.txt``: file associating model mumbers (see below) with model
  names.

The subject directory contains all information for one subject.

The subject directory has name of form ``subXXX`` where ``XXX`` is an integer
with left zero padding, e.g ``sub001`` for subject number 1.  Indices start at
1 so `sub001` is the first subject in the dataset.

A subject directory may contain:

* an ``anatomy`` directory.
    

