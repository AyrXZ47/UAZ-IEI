library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_rom_mensajes is
end tb_rom_mensajes;

architecture t of tb_rom_mensajes is

  signal sel : STD_LOGIC := '0';
  signal dir : STD_LOGIC_VECTOR(2 downto 0) := "000";
  signal seg : STD_LOGIC_VECTOR(7 downto 0);

  constant MSG0 : string(1 to 8) := "HOLAIEIS";
  constant MSG1 : string(1 to 8) := "35167151";

  -- Patrones activo bajo {a,b,c,d,e,f,g,dp}
  function patron(c : character) return STD_LOGIC_VECTOR is
  begin
    case c is
      when 'H'    => return "10001100";
      when 'O'    => return "00000011";
      when 'L'    => return "11100011";
      when 'A'    => return "00010001";
      when ' '    => return "11111111";
      when 'E'    => return "01100001";
      when 'I'    => return "10011111";
      when 'S'    => return "01001001";
      when '0'    => return "00000011";
      when '1'    => return "10011111";
      when '2'    => return "00100101";
      when '3'    => return "00001101";
      when '5'    => return "01001001";
      when '6'    => return "01000001";
      when '7'    => return "00011111";
      when '8'    => return "00000001";
      when others => return "11111111";
    end case;
  end function;

begin

  uut : entity work.rom_mensajes
        port map (sel => sel, dir => dir, seg => seg);

  stim : process
    variable msg : string(1 to 8);
    variable d : integer;
  begin
    for m in 0 to 1 loop
      if m = 0 then
        sel <= '0'; msg := MSG0;
      else
        sel <= '1'; msg := MSG1;
      end if;

      for i in 1 to 8 loop
        d := 8 - i;                     -- i=1 (izquierda) -> dir=7
        dir <= std_logic_vector(to_unsigned(d, 3));
        wait for 10 ns;
        assert seg = patron(msg(i))
          report "Falla sel=" & integer'image(m) &
                 " dir=" & integer'image(d) &
                 " caracter='" & msg(i) & "'"
          severity failure;
      end loop;
    end loop;

    report "OK: 'HOLAIEIS' y '35167151' verificados en los 8 displays.";
    wait;
  end process;

end t;
