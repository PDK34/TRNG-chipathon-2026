(* blackbox *)
module ring_oscillator_final (
 `ifdef USE_POWER_PINS
    inout wire VDD,
    inout wire GND,
`endif

//    inout wire VDD,
  //  inout wire GND,
    input wire VinVCO,
    output wire VO
);
//dummy module for the analog macro
endmodule