#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BiTime

urls = [
	(r"/", BiTime.IndexHandler),
	(r"/ferryBus", BiTime.FerryBusHandler),
]