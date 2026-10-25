# Definitional proc to organize widgets for parameters.
proc init_gui { IPINST } {
  ipgui::add_param $IPINST -name "Component_Name"
  #Adding Page
  set Page_0 [ipgui::add_page $IPINST -name "Page 0"]
  ipgui::add_param $IPINST -name "frec_in" -parent ${Page_0}
  ipgui::add_param $IPINST -name "frec_out" -parent ${Page_0}
  ipgui::add_param $IPINST -name "num_display" -parent ${Page_0}


}

proc update_PARAM_VALUE.frec_in { PARAM_VALUE.frec_in } {
	# Procedure called to update frec_in when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.frec_in { PARAM_VALUE.frec_in } {
	# Procedure called to validate frec_in
	return true
}

proc update_PARAM_VALUE.frec_out { PARAM_VALUE.frec_out } {
	# Procedure called to update frec_out when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.frec_out { PARAM_VALUE.frec_out } {
	# Procedure called to validate frec_out
	return true
}

proc update_PARAM_VALUE.num_display { PARAM_VALUE.num_display } {
	# Procedure called to update num_display when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.num_display { PARAM_VALUE.num_display } {
	# Procedure called to validate num_display
	return true
}


proc update_MODELPARAM_VALUE.frec_in { MODELPARAM_VALUE.frec_in PARAM_VALUE.frec_in } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.frec_in}] ${MODELPARAM_VALUE.frec_in}
}

proc update_MODELPARAM_VALUE.frec_out { MODELPARAM_VALUE.frec_out PARAM_VALUE.frec_out } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.frec_out}] ${MODELPARAM_VALUE.frec_out}
}

proc update_MODELPARAM_VALUE.num_display { MODELPARAM_VALUE.num_display PARAM_VALUE.num_display } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.num_display}] ${MODELPARAM_VALUE.num_display}
}

