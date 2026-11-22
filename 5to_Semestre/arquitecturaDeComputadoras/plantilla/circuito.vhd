-- PLANTILLA de circuito. Lo unico que cambias practica a practica:
--   1. el nombre de la entity (aqui "circuito"),
--   2. las entradas/salidas del port,
--   3. las lineas de logica entre begin y end.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity circuito is
  port (
    A, B, C : in  STD_LOGIC;   -- entradas: agrega o quita segun tu practica
    F       : out STD_LOGIC    -- salidas
  );
end circuito;

architecture logica of circuito is
begin
  -- TU LOGICA AQUI. Cada linea es una compuerta o una expresion:
  --   F <= A and B;                  -- AND
  --   F <= A or B;                   -- OR
  --   F <= not A;                    -- inversor
  --   F <= A nand B;                 -- NAND
  --   F <= (not A and not B) or C;   -- combinacion
  F <= (not A and not B) or C;  -- REEMPLAZA por la de tu practica
end logica;
