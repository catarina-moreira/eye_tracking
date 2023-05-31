#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

class Transfer(object):
	def getID(self) -> str:
		return self.__iD

	def setEvent_type(self, event_type : str):
		self.__event_type = event_type

	def getEvent_type(self) -> str:
		return self.__event_type

	def setCare_unit(self, care_unit : str):
		self.__care_unit = care_unit

	def getCare_unit(self) -> str:
		return self.__care_unit

	def setIntime(self, intime : str):
		self.__intime = intime

	def getIntime(self) -> str:
		return self.__intime

	def setOuttime(self, outtime : str):
		self.__outtime = outtime

	def getOuttime(self) -> str:
		return self.__outtime

	def __init__(self):
		self.__iD : str = None
		self.__event_type : str = None
		self.__care_unit : str = None
		self.__intime : str = None
		self.__outtime : str = None


