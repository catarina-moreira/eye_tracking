#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from mimic.Xray import Xray
from RadiologistAdapter import RadiologistAdapter
from typing import List

class Radiologist(object):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self.is_analysed_by : Xray = None
		"""# @AssociationMultiplicity 1"""
		self.implements : RadiologistAdapter = None

