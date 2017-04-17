#!/usr/bin/env python
def par(inicio,fin):
	for i in range(inicio,fin):
		if i % 2==0:
			yield i