import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def ahb_top_tb(dut):
    clock = Clock(dut.hclk, 2, units='ns')
    cocotb.start_soon(clock.start())
    # Initialize inputs
    dut.hclk.value = 0
    dut.hresetn.value = 1
    dut.enable.value = 0
    dut.dina.value = 0
    dut.dinb.value = 0
    dut.addr.value = 0
    dut.wr.value = 0
    dut.slave_sel.value = 0

    # Apply reset
    await Timer(10, units='ns')
    dut.hresetn.value = 0
    await Timer(10, units='ns')
    dut.hresetn.value = 1

    # slave 1
    await write(dut, 0b00, 1, 1, 2)
    await read(dut, 0b00, 1)

    # slave 2
    await write(dut, 0b01, 2, 3, 4)
    await read(dut, 0b01, 2)

    # slave 3
    await write(dut, 0b10, 3, 5, 6)
    await read(dut, 0b10, 3)

    # slave 4
    await write(dut, 0b11, 4, 7, 8)
    await read(dut, 0b11, 4)
    await write(dut, 0b11, 5, 9, 10)
    await read(dut, 0b11, 5)

async def write(dut, sel, address, a, b):
    await RisingEdge(dut.hclk)
    dut.slave_sel.value = sel
    dut.enable.value = 1
    dut.addr.value = address
    await RisingEdge(dut.hclk)
    dut.dina.value = a
    dut.dinb.value = b
    dut.wr.value = 1
    await RisingEdge(dut.hclk)
    dut.enable.value = 0

async def read(dut, sel, address):
    await RisingEdge(dut.hclk)
    dut.enable.value = 1
    dut.slave_sel.value = sel
    dut.addr.value = address
    await RisingEdge(dut.hclk)
    dut.wr.value = 0
    await RisingEdge(dut.hclk)
    await RisingEdge(dut.hclk)
    await RisingEdge(dut.hclk)
    await RisingEdge(dut.hclk)
    dut.enable.value = 0

