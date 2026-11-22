-- demux 1x4: 1 entrada de datos (A), 4 salidas (SAL), y SEL elige A cual va.
-- Es un "desviador de vias de tren": A es el tren, SEL es el desviador.
--
--   SEL=00 -> SAL=0001  (A cae en SAL(0))
--   SEL=01 -> SAL=0010  (A cae en SAL(1))
--   SEL=10 -> SAL=0100  (A cae en SAL(2))
--   SEL=11 -> SAL=1000  (A cae en SAL(3))
--
-- (los 4 bits se leen de izquierda a derecha: SAL(3) SAL(2) SAL(1) SAL(0))
--
-- OJO con lo que dijo el profe en clase: A puede valer CUALQUIER cosa menos 0.
-- Por que? Porque si A=0, TODAS las salidas valen 0 sin importar SEL y no
-- puedes ver A donde aterrizo. Con A=1 el '1' "se mueve" por SAL siguiendo a
-- SEL, y ahi se ve el demux funcionando.
--
-- El nombre feo "demux1x4_when_27803872" que genera Active-HDL es solo
-- entity + timestamp; aqui se escribe a mano en 15 lineas y es el mismo VHDL.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity demux1x4 is
  port (
    A   : in  STD_LOGIC;                    -- el dato (1 bit)
    SEL : in  STD_LOGIC_VECTOR(1 downto 0); -- el desviador: 00,01,10,11
    SAL : out STD_LOGIC_VECTOR(3 downto 0)  -- las 4 vias
  );
end demux1x4;

-- ESTILO 1 (el "segundo camino" del profe): UNA sola asignacion condicional.
-- WHEN/ELSE se lee: "si SEL vale esto, SAL toma la expresion de la izquierda".
-- & CONCATENA: pega pedazos de bits uno tras otro, de MSB a LSB.
--   "00" & '1' & '0'  =  0 0 1 0  = "0010"
architecture when_else of demux1x4 is
begin
  SAL <= "000" & A    WHEN SEL = "00" ELSE  -- A en el bit 0: 000[1]
         "00"  & A & '0' WHEN SEL = "01" ELSE  -- A en el bit 1: 00[1]0
         '0'   & A & "00" WHEN SEL = "10" ELSE  -- A en el bit 2: 0[1]00
         A     & "000";                         -- A en el bit 3: [1]000
end when_else;

-- ESTILO 2 (el "primer camino" del profe): una asignacion POR BIT.
-- Mismo circuito, mas verboso (y hay que acordarse de poner el ELSE '0',
-- si no, el bit no elegido quedaria sin asignar = 'U' en simulacion).
--
-- SAL(0) <= A WHEN SEL = "00" ELSE '0';
-- SAL(1) <= A WHEN SEL = "01" ELSE '0';
-- SAL(2) <= A WHEN SEL = "10" ELSE '0';
-- SAL(3) <= A WHEN SEL = "11" ELSE '0';
--
-- ESTILO 3 (el que usaran con SELECT): mismo resultado con una tabla.
--
-- WITH SEL SELECT
--   SAL <= "000" & A   WHEN "00",
--          "00"  & A & '0' WHEN "01",
--          '0'   & A & "00" WHEN "10",
--          A     & "000" WHEN OTHERS;
