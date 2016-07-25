#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ask Keyer
# Generated: Mon Jul 25 23:25:31 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx


class ask_keyer(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Ask Keyer")

        ##################################################
        # Variables
        ##################################################
        self.tx_freq = tx_freq = 433.9e6
        self.symbol_length = symbol_length = 750e-6
        self.samp_rate = samp_rate = 2e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(tx_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(20, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_vector_source_x_0 = blocks.vector_source_f([0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0], True, 1, [])
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, int(symbol_length*samp_rate))
        self.blocks_patterned_interleaver_0_0 = blocks.patterned_interleaver(gr.sizeof_float*1, ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        self.blocks_patterned_interleaver_0 = blocks.patterned_interleaver(gr.sizeof_float*1, ([2,0,1]))
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, tx_freq, 1, 0)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_patterned_interleaver_0, 2))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_patterned_interleaver_0_0, 1))    
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_patterned_interleaver_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_patterned_interleaver_0, 0), (self.blocks_patterned_interleaver_0_0, 0))    
        self.connect((self.blocks_patterned_interleaver_0_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_patterned_interleaver_0, 0))    

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.osmosdr_sink_0.set_center_freq(self.tx_freq, 0)
        self.analog_sig_source_x_0.set_frequency(self.tx_freq)

    def get_symbol_length(self):
        return self.symbol_length

    def set_symbol_length(self, symbol_length):
        self.symbol_length = symbol_length
        self.blocks_repeat_0.set_interpolation(int(self.symbol_length*self.samp_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_repeat_0.set_interpolation(int(self.symbol_length*self.samp_rate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=ask_keyer, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
