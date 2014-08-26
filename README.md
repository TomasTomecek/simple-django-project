simple-django-project
=====================

This is an example [django](http://djangoproject.com/) 1.7 project deployed with [Red Hat Software Collections](https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/). The project was started for this blog post at [Red Hat's Developer Blog](https://developerblog.redhat.com).

*Read the blog post before trying anything. It covers server setup.*

Architecture
------------

Project has several components:

* app itself
* [software collection](https://www.softwarecollections.org/) [metapackage](http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/sect-Creating_a_Meta_Package.html)
* configuration packaged separately (in `conf/<env>/`)

Each component contains

* makefile
* specfile

and whole app has ansible playbook for deployment.

It's configured to use these technologies:

* [Red Hat Software Collections](https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/)
 * python33
 * nginx14
 * postgresql92
* [django](http://djangoproject.com/) 1.7
* [uWSGI](https://uwsgi-docs.readthedocs.org/en/latest/)
* [Red Hat Enterprise Linux 7](http://www.redhat.com/en/resources/rhel-7-whats-new)
* [virtualenv](http://virtualenv.readthedocs.org/)
* [ansible](http://www.ansible.com/)

Build Process
============

RPMs are built using [mock](http://fedoraproject.org/wiki/Projects/Mock). Configuration files are provided, you just have to update URLs and place them to `/etc/mock/` so mock can find them:

_rhscl-python3.cfg_

mock profile for building SCL metapackage.

```
[rhscl]
name=rhscl
baseurl=http://path/to/your/rhscl/repo  # <-- update me!
enabled=1

[rhel7]
name=rhel7
enabled=1
baseurl=http://path/to/your/rhel7/repo  # <-- update me!

# required by scl-utils-build
[rhel-optional]
name=rhel-optional
enabled=1
baseurl=http://path/to/your/rhel7-optional/repo  # <-- update me!
```

```
$ cp -av rhscl-python3.cfg /etc/mock/
```


_rhscl-python3-sdp.cfg_

mock profile for building app and configuration

```
[rhscl]
name=rhscl
baseurl=http://path/to/your/rhscl/repo  # <-- update me!
enabled=1

[rhel7]
name=rhel7
enabled=1
baseurl=http://path/to/your/rhel7/repo  # <-- update me!

# required by scl-utils-build
[rhel-optional]
name=rhel-optional
enabled=1
baseurl=http://path/to/your/rhel7-optional/repo  # <-- update me!

# repo containing our metapackage
[scl-meta]
name=scl-meta
enabled=1
baseurl=file:////var/tmp/yumrepos/sdp/
```

```
$ cp -av rhscl-python3-sdp.cfg /etc/mock/
```

Prepare RPMs:

```
make
```

Installation
============

```
make deploy
```

or equivalently:

```
ansible-playbook ansible.yml
```

Structure
=========

* `conf` — configuration of application
  * `prod`
  * `stage`
  * `devel`
    * sample development configuration; `prod` and `stage` are empty
* `rpms` — store of rpms built by `make`
* `simple` — django app itself
* `scl` —  metapackage for software collections

For more information, check `Makefile`s, `setup.py` or `specfile`s.

Disclaimer
==========

This is not enterprise ready solution. It's mostly a proof of concept recipe how you could manage your deployments with Red Hat Software Collections. Feedback and ideas for improvement are very welcome.

