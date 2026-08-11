label avg10011(trans=fade_in):

$ play_music("ED6516.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1001074)]' (**arg(1, 1001074))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1001075)]' (**arg(2, 1001075))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001076)]' (**arg(3, 1001076))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001077)]' (**arg(4, 1001077))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001078)]' (**arg(5, 1001078))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1001079)]' (**arg(6, 1001079))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001080)]' (**arg(7, 1001080))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1001081)]' (**arg(8, 1001081))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1001082)]' (**arg(9, 1001082))
$ update_portrait('oc002_01 19', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6020.ogg"
get_char('c21') '[convertstrid(1001083)]' (**arg(10, 1001083))
hide p2
$ update_portrait('oc003_01 12', 'p719', [l(-6), l_shake, light, flip], 6)
get_char('c7191') '[convertstrid(1001084)]' (**arg(11, 1001084))
$ update_portrait('oc003_01 12', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001085)]' (**arg(12, 1001085))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001086)]' (**arg(13, 1001086))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p719', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c7191') '[convertstrid(1001087)]' (**arg(14, 1001087))
$ update_portrait('oc003_01 5', 'p719', [l(-6), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c7191') '[convertstrid(1001088)]' (**arg(15, 1001088))
return "avg10011"