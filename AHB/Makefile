# Makefile

# defaults
SIM ?= questa
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/ahb_master.v \
					$(PWD)/ahb_slave.v \
					$(PWD)/ahb_top.v \
					$(PWD)/decoder.v \
					$(PWD)/multiplexor.v \
					$(PWD)/one_master_slave.v
										
	
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = ahb_top

# MODULE is the basename of the Python test file
MODULE = test_AHB
SIM_ARGS +=  -coverage 
#WAVEFORM = 1
# SIM_ARGS += -voptargs="+acc -designfile design.bin" -coverage -qwavedb=+signal+msg+report -L axcelerator -t 1ps -suppress 3009 -onfinish exit
#SIM_ARGS += -voptargs="+acc -designfile design.bin" -coverage -qwavedb=+signal+msg+report -L axcelerator -t 1ps -suppress 3009 
#SIM_ARGS = vis -designfile design.bin -wavefile qwave.db
#vopt +cover=bcesxf test_sm -o test_sm_opt

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim