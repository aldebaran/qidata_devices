Description
===========

This very simple package provides a list of devices for QiData context message,
defined as an entry point. It is the default list, the base one, that can be
extended by creating a new package aside of this one.

This package does not depend on qidata, but qidata depends on it.

Installation
============

For now, you can only install this package from sources.

First, you need to install xmp (which can also only be installed from sources)::

	git clone https://github.com/aldebaran/qidata_devices.git
	cd qidata_devices
	python setup.py bdist_wheel
	pip install dist/*
