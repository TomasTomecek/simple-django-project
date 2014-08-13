simple-django-project
=====================

This is an example django 1.7 project for blog post at https://developerblog.redhat.com

It contains

* app itself
* spec file
* makefile (so you can easily build it)
* configuration packaged separately

It's configured to use this technology:

* Red Hat Software Collections
 * python33
 * nginx14
 * postgresql92
* django 1.7
* uWSGI
* Red Hat Enterprise Linux 7
* virtualenv

Installation
============

```
make scl-rpm
```

and then install rpms from `./rpms/`:

```
yum install ./rpms/*
```

Structure
=========

* `conf` -- configuration of application
 * `prod`
 * `stage`
 * `devel`
  * sample development configuration; `prod` and `stage` are empty
* `rpms` -- store of rpms built by `make scl-rpm`
* `simple` -- django app itself

Disclaimer
==========

This is not fully enterprise ready solution. It's mostly a proof of concept recipe how you could manage your deployments with Red Hat Software Collections. Feedback and ideas for improvement are very welcome.
