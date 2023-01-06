#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Radiologist
from typing import List

class RadiologistAdapter(object):
	def __init__(self):
		self.implements : Radiologist = None

	class REFLACX(RadiologistAdapter):
		pass

	class EyeGaze(RadiologistAdapter):
		pass

