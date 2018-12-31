##### Tue Dec 18 2018 Sundeep Anand <suanand@redhat.com> - release_0.1.6
* Implement Spec's file %prep section in Jobs, improve tarball selection
* Auth and OpenShift deployment config changes

##### Sat Nov 10 2018 Sundeep Anand <suanand@redhat.com> - release_0.1.6-rc.2
* PostgreSQL database 9.2 back port and bug fixes
* Package exist API and Job commands ACL, better docs
* Add translation platform auth in jobs, bug fixes
* String change job implementation and diff UI
* Provision to pass kwargs for tasks in YML jobs

##### Tue Jul 03 2018 Sundeep Anand <suanand@redhat.com> - release_0.1.6-rc.1
* Language shortcuts in release summary page
* YML Job trigger through API. API Authentication
* Job Templates, Log Unique URL, Job details page

##### Fri Jun 22 2018 Sundeep Anand <suanand@redhat.com> - release_0.1.5
* Add files for OpenShift deployment ([bhavin192](https://github.com/bhavin192))
* Optimise code and a few bug fixes in graphs, diff ui
* Fix branch mapping for GNOME Packages (as per buildsys)
* Improve docs, Add Jobs section to `docs.transtats.org`
* Migrate from Travis CI to Circle CI, fix Docker files
* Update packages summary with out of sync packages
* Extend downstream sync to brew and fix branch mapping
* Add koji build system tags in package branch mapping
* Add Koji API Resources and YAML based TS Jobs
* Add Sync Build Tags Job to facilitate YAML based Jobs

##### Wed Jan 24 2018 Sundeep Anand <suanand@redhat.com> - release_0.1.5-rc.1
* Add docker-compose setup for easy deployment ([bhavin192](https://github.com/bhavin192))
* Making ready for openshift deployment, fix static files

##### Wed Nov 15 2017 Sundeep Anand <suanand@redhat.com> - release_0.1.4
* Modify APIs - `status` is `package` and `workload` is `release` now
* Add `releases` and `packages` reports to landing page
* Improve UI, Jobs tab, package config with stats, better navigation
* Improved transtats docs ([bhavin192](https://github.com/bhavin192))
* Enable FAS authentication and adjust user roles
* Add packages export to CSV option
* Add service layer between API responses and logic

##### Fri Aug 25 2017 Sundeep Anand <suanand@redhat.com> - release_0.1.3
* DamnedLies APIs initial integration: translation status
* REST API development: status, coverage, workload
* Update Dockerfile and add Vagrant + Ansible playbook

##### Fri Jun 30 2017 Sundeep Anand <suanand@redhat.com> - release_0.1.2
* translation platforms auth settings for API
* package upstream sync for translation stats
* add unit tests & configure travis and logging
* add docker file, based on `fedora:latest`

##### Wed Apr 26 2017 Sundeep Anand <suanand@redhat.com> - release_0.1.1
* add combined lang view to translation workload
* add detailed stats view to workload estimation
* translation workload estimation per release branch
* add tabular view to translation status
* split package-refresh into sync and map branches
* add language-wise status graph for a package

##### Fri Mar 17 2017 Sundeep Anand <suanand@redhat.com> - release_0.1.0
* enable branch mapping for translation coverage
* provision section for package configurations
* implement language set and branch mapping features
* add django rest framework to ping server
* enable django admin to manage inventory and jobs

##### Mon Dec 05 2016 Sundeep Anand <suanand@redhat.com> - Concept
* enable ical sync for RHEL and Fedora - syncCalendar Jobs
* add and list graph rules, display graphs based on rules
* add release_stream_branches model, view, html, form
* settings summary and add stats templates dir
* package-names mapping provision
* move to Django ORM - migrations

##### Thu Sept 15 2016 Sundeep Anand <suanand@redhat.com> - Prototype
* add Transifex support - transplatform API configs
* enable displaying some charts based on sync'd data
* add logs settings page, add package transplatform validation
* enable transplatform projects and stats sync (zanata)
* add django-crispy-forms and enable add packages
* moved to Apache Licence Version 2.0
* add languages, transplatform, relstreams settings pages
* rename project to transtats, fix ui and migrate to PostgreSQL
* add features page, zanata api, view, manager and model
* initial structure with django: settings, requires, docs
