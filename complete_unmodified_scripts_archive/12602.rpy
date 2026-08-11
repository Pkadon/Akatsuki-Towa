label avg12602(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_080
$ update_narrator('c21')
window show
with trans
$ update_portrait('oc002_01 17', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c21') '[convertstrid(1161132)]' (**arg(1, 1161132))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1161133)]' (**arg(2, 1161133))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161134)]' (**arg(3, 1161134))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161135)]' (**arg(4, 1161135))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161136)]' (**arg(5, 1161136))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
get_char('c31') '[convertstrid(1161137)]' (**arg(6, 1161137))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161138)]' (**arg(7, 1161138))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161139)]' (**arg(8, 1161139))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1161140)]' (**arg(9, 1161140))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1161141)]' (**arg(10, 1161141))
return "avg12602"