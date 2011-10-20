#!/usr/bin/env sh
nosetests -w tests $1 --cover-package=brukva --nologcapture --nocapture -v

