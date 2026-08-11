label avg12158(trans=fade_in):

$ play_music("ED6107.ogg")
scene avg_bg_057
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1128408)]' (**arg(1, 1128408))
hide p1
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1128409)]' (**arg(2, 1128409))
$ update_portrait('sc017_01 2', 'p963', [l_entrance(-7), light, flip], 6)
get_char('c9631') '[convertstrid(1128410)]' (**arg(3, 1128410))
$ update_portrait('sc017_01 2', 'p963', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1128411)]' (**arg(4, 1128411))
hide p963
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc017_01 5', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1128412)]' (**arg(5, 1128412))
hide p4
$ update_portrait('sc017_01 5', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128413)]' (**arg(6, 1128413))
hide p571
hide p1
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1128414)]' (**arg(7, 1128414))
$ update_portrait('sc017_01 5', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128415)]' (**arg(8, 1128415))
$ update_portrait('sc017_01 5', 'p25', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1128416)]' (**arg(9, 1128416))
hide p25
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc017_01 2', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1128417)]' (**arg(10, 1128417))
$ update_portrait('sc017_01 2', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1128418)]' (**arg(11, 1128418))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('sc017_01 5', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1128419)]' (**arg(12, 1128419))
hide p2
$ update_portrait('sc017_01 5', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128420)]' (**arg(13, 1128420))
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1128421)]' (**arg(14, 1128421))
scene avg_bg_057
$ update_portrait('sc017_01 1', 'p25', [l(-7), light, flip], 6)
$ update_narrator('c251')
with fade
get_char('c251') '[convertstrid(1128422)]' (**arg(15, 1128422))
$ update_portrait('sc017_01 6', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128423)]' (**arg(16, 1128423))
$ update_portrait('sc017_01 1', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128424)]' (**arg(17, 1128424))
$ update_portrait('sc017_01 4', 'p25', [l(-7), light, flip], 6)
play sfx2 "other_7059.ogg"
get_char('c251') '[convertstrid(1128425)]' (**arg(18, 1128425))
$ update_portrait('sc017_01 1', 'p25', [l(-7), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c251') '[convertstrid(1128426)]' (**arg(19, 1128426))
$ update_portrait('sc017_01 3', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128427)]' (**arg(20, 1128427))
$ update_portrait('sc017_01 1', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128428)]' (**arg(21, 1128428))
$ update_portrait('sc017_01 4', 'p25', [l(-7), light, flip], 6)
get_char('c251') '[convertstrid(1128429)]' (**arg(22, 1128429))
return "avg12158"