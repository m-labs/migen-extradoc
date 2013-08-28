from migen.fhdl.std import *
from migen.fhdl import verilog
from migen.genlib.misc import optree
from migen.fhdl import namer

namer._debug = True

class Foo:
	def __init__(self):
		self.la = [Signal() for x in range(2)]
		self.lb = [Signal() for x in range(3)]

class Example(Module):
	def __init__(self):
		a = [Foo() for x in range(3)]
		
		output = Signal()
		allsigs = []
		for obj in a:
			allsigs.extend(obj.la)
			allsigs.extend(obj.lb)
		self.comb += output.eq(optree("|", allsigs))

print(verilog.convert(Example()))
