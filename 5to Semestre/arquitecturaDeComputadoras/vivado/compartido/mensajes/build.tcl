# build.tcl - genera el block design y el bitstream del proyecto "mensajes".
# Uso: vivado -mode batch -source build.tcl
#
# El proyecto reutiliza pres_500hz, contador y dec_an de bcd_diferentes y
# cambia la fuente de datos (mux_datos + Dec_bcd_seg) por una ROM de patrones.

set root [file normalize [file dirname [info script]]]
cd $root

if {[file exists mensajes.xpr]} {
    open_project mensajes.xpr
} else {
    create_project mensajes . -part xc7a100tcsg324-1
    set_property target_language VHDL [current_project]
}

# --- fuentes y restricciones -------------------------------------------------
set srcs [glob -nocomplain mensajes.srcs/sources_1/new/*.vhd]
if {[llength $srcs]} {
    add_files -norecurse $srcs
}

if {[llength [get_files -quiet *Nexys4-DDR-Master.xdc]] == 0} {
    add_files -fileset constrs_1 -norecurse \
        [glob mensajes.srcs/constrs_1/imports/Downloads/*.xdc]
}

update_compile_order -fileset sources_1

# --- block design ------------------------------------------------------------
if {[llength [get_files -quiet design_1.bd]] == 0} {
    create_bd_design design_1

    # Puertos externos (los mismos nombres que usa el XDC de la Nexys)
    create_bd_port -dir I -type clk -freq_hz 100000000 CLK100MHZ
    create_bd_port -dir I rst
    create_bd_port -dir I -from 0 -to 0 SW
    create_bd_port -dir O -from 7 -to 0 seg
    create_bd_port -dir O -from 7 -to 0 AN

    # Modulos
    create_bd_cell -type module -reference pres_500hz   pres_500hz_0
    create_bd_cell -type module -reference contador     contador_0
    create_bd_cell -type module -reference dec_an       dec_an_0
    create_bd_cell -type module -reference rom_mensajes rom_mensajes_0

    # Conexiones
    connect_bd_net [get_bd_ports CLK100MHZ] \
        [get_bd_pins pres_500hz_0/clk]
    connect_bd_net [get_bd_ports rst] \
        [get_bd_pins pres_500hz_0/rst] \
        [get_bd_pins contador_0/rst]
    connect_bd_net [get_bd_pins pres_500hz_0/clk_pres] \
        [get_bd_pins contador_0/clk]
    connect_bd_net [get_bd_pins contador_0/display] \
        [get_bd_pins dec_an_0/ent] \
        [get_bd_pins rom_mensajes_0/dir]
    connect_bd_net [get_bd_ports SW] \
        [get_bd_pins rom_mensajes_0/sel]
    connect_bd_net [get_bd_pins dec_an_0/sal] \
        [get_bd_ports AN]
    connect_bd_net [get_bd_pins rom_mensajes_0/seg] \
        [get_bd_ports seg]

    save_bd_design
    validate_bd_design
} else {
    open_bd_design [get_files design_1.bd]
}

# --- wrapper y top -----------------------------------------------------------
if {[llength [get_files -quiet *design_1_wrapper.vhd]] == 0} {
    set wrapper mensajes.gen/sources_1/bd/design_1/hdl/design_1_wrapper.vhd
    if {![file exists $wrapper]} {
        make_wrapper -files [get_files design_1.bd] -top
    }
    add_files -norecurse $wrapper
}
set_property top design_1_wrapper [current_fileset]
update_compile_order -fileset sources_1

# --- sintesis e implementacion ----------------------------------------------
launch_runs synth_1 -jobs 8
wait_on_run synth_1
if {[get_property PROGRESS [get_runs synth_1]] != "100%"} {
    error "Fallo la sintesis"
}

launch_runs impl_1 -to_step write_bitstream -jobs 8
wait_on_run impl_1
if {[get_property PROGRESS [get_runs impl_1]] != "100%"} {
    error "Fallo la implementacion"
}

puts "Bitstream: [get_property DIRECTORY [get_runs impl_1]]/design_1_wrapper.bit"
