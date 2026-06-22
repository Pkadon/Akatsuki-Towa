label avg12181:

$ play_music("ED6104.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1007707)]' (**arg(1, 1007707))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120600)]' (**arg(2, 1120600))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120601)]' (**arg(3, 1120601))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1120602)]' (**arg(4, 1120602))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120603)]' (**arg(5, 1120603))
hide p2
hide p1
$ update_portrait('sc022_01 2', 'p500', [l(-9), light, flip], 6)
$ update_narrator('c5001')
with fade
get_char('c5001') '[convertstrid(1120604)]' (**arg(6, 1120604))
$ update_portrait('sc022_01 2', 'p500', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1120605)]' (**arg(7, 1120605))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120606)]' (**arg(8, 1120606))
hide p500
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), l_shake, light, flip], 6)
get_char('c301') '[convertstrid(1120607)]' (**arg(9, 1120607))
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120608)]' (**arg(10, 1120608))
hide p30
hide p2
get_char('c0') '[convertstrid(1120609)]' (**arg(11, 1120609))
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
get_char('c301') '[convertstrid(1120610)]' (**arg(12, 1120610))
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1120611)]' (**arg(13, 1120611))
hide p1
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
get_char('c301') '[convertstrid(1120612)]' (**arg(14, 1120612))
hide p30
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1120613)]' (**arg(15, 1120613))
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
get_char('c301') '[convertstrid(1120614)]' (**arg(16, 1120614))
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
get_char('c301') '[convertstrid(1120615)]' (**arg(17, 1120615))
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
get_char('c301') '[convertstrid(1120616)]' (**arg(18, 1120616))
return