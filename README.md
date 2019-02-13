# CROWDPINION 

(http://crowdpinionscreenshoturl)](http://crowdpinionproductionurl)


A django app for questionnaire. 

View a running instance at [http://crowdpinionproductionurl](http://crowdpinionproductionurl)


Note that whilst usable, CrowdPinion is under continual development and not
yet feature complete.

The latest source code is available at 
[https://github.com/kartoza/crowdpinion](https://github.com/kartoza/crowdpinion).

* **Developers:** See our [developer guide](README-dev.md)
* **For production:** See our [deployment guide](README-docker.md)


## Key features

* An clean, easy to use app to ask questions and get immediate answer from participants

## Project activity

Story queue on Waffle:

* [![Stories in Ready](https://badge.waffle.io/kartoza/crowdpinion.svg?label=ready&title=Ready)](http://waffle.io/kartoza/crowdpinion) 
* [![Stories in In Progress](https://badge.waffle.io/kartoza/crowdpinion.svg?label=in%20progress&title=In%20Progress)](http://waffle.io/kartoza/crowdpinion)

[![Throughput Graph](https://graphs.waffle.io/kartoza/crowdpinion/throughput.svg)](https://waffle.io/kartoza/crowdpinion/metrics)

* Current test status master: [![Build Status](https://travis-ci.org/inasafe/inasafe.svg?branch=master)](https://travis-ci.org/inasafe/inasafe) and
[![Code Health](https://landscape.io/github/kartoza/crowdpinion/master/landscape.svg?style=flat)](https://landscape.io/github/kartoza/crowdpinion/master)

* Current test status develop: [![Build Status](https://travis-ci.org/inasafe/inasafe.svg?branch=develop)](https://travis-ci.org/inasafe/inasafe) and
[![Code Health](https://landscape.io/github/kartoza/crowdpinion/develop/landscape.svg?style=flat)](https://landscape.io/github/kartoza/crowdpinion/develop)

* Test coverage [![codecov](https://codecov.io/gh/kartoza/crowdpinion/branch/develop/graph/badge.svg)](https://codecov.io/gh/kartoza/crowdpinion)



## Quick Installation Guide

For deployment we use [docker](http://docker.com) so you need to have docker 
running on the host. CrowdPinion is a django app so it will help if you have
some knowledge of running a django site.

```
git clone git://github.com/kartoza/crowdpinion.git
cd crowdpinion/deployment
cp btsync-db.env.EXAMPLE btsync-db.env
cp btsync-media.env.EXAMPLE btsync-media.env
make build
make permissions
make web
# Wait a few seconds for the DB to start before to do the next command
make migrate
make collectstatic
```

If you need backups, put btsync keys in these files. If you don't need backups, 
you can let the default content.

So as to create your admin account:
```
make superuser
```

**google authentication**

In social auth to use the google authentication you need to go to:

https://console.developers.google.com/apis/credentials

Create and oath2 credential with these options:

Authorized redirect URIs

http://<your domain>/en/complete/google-oauth2/

Use the crowdpinion admin panel to set up the google account with your id and
secret


**Backups**

If you wish to sync backups, you need to establish a read / write btsync 
key on your production server and run one or more btsync clients 
with a read only key.

```
cd deployment
cp btsync-media.env.EXAMPLE btsync-media.env
cp btsync-db.env.EXAMPLE btsync-db.env
```

Now edit the ``btsync-media.env`` and ``btsync-db.env`` files, including 
relevant SECRET and DEVICE settings.

## Participation


We work under the philosophy that stakeholders should have access to the
development and source code, and be able to participate in every level of the 
project - we invite comments, suggestions and contributions.  See
[our milestones list](https://github.com/kartoza/crowdpinion/milestones) and
[our open issues list](https://github.com/kartoza/crowdpinion/issues?page=1&state=open)
for known bugs and outstanding tasks. You can also chat live with our developers
and community members using the link below.


## Credits

Crowdpinion was developed by [Kartoza.com](http://kartoza.com) and 
individual contributors.

## License

Crowdpinion is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License version 3 (GPLv3) as
published by the Free Software Foundation.

The full GNU General Public License is available in LICENSE.txt or
http://www.gnu.org/licenses/gpl.html


## Disclaimer of Warranty (GPLv3)

There is no warranty for the program, to the extent permitted by
applicable law. Except when otherwise stated in writing the copyright
holders and/or other parties provide the program "as is" without warranty
of any kind, either expressed or implied, including, but not limited to,
the implied warranties of merchantability and fitness for a particular
purpose. The entire risk as to the quality and performance of the program
is with you. Should the program prove defective, you assume the cost of
all necessary servicing, repair or correction.

## Thank you

Thank you to the individual contributors who have helped to build crowdpinion:

* Tim Sutton (Lead developer): tim@kartoza.com
* Anita Hapsari : anita@kartoza.com

