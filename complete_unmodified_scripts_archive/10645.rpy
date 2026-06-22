label avg10645:

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1164593)]' (**arg(1, 1164593))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1164594)]' (**arg(2, 1164594))
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1164595)]' (**arg(3, 1164595))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l_exit(-6), light, flip], 6)
get_char('c51') '[convertstrid(1164596)]' (**arg(4, 1164596))
hide p5
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1164597)]' (**arg(5, 1164597))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164598)]' (**arg(6, 1164598))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1164599)]' (**arg(7, 1164599))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164600)]' (**arg(8, 1164600))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1164601)]' (**arg(9, 1164601))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164602)]' (**arg(10, 1164602))
return