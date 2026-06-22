label avg12194:

$ play_music("ED6200.ogg")
scene avg_bg_023
$ update_portrait('st018_01 3', 'p217', [r(-16), light], 6)
$ update_narrator('c2173')
window show
with fade_in
get_char('c2173') '[convertstrid(1120770)]' (**arg(1, 1120770))
hide p217
get_char('c0') '[convertstrid(1120771)]' (**arg(2, 1120771))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1120772)]' (**arg(3, 1120772))
hide p2
$ update_portrait('st017_01 2', 'p216', [r(-18), light], 6)
get_char('c2163') '[convertstrid(1120773)]' (**arg(4, 1120773))
hide p216
$ update_portrait('st019_01 5', 'p218', [r(-17), light], 6)
get_char('c2183') '[convertstrid(1120774)]' (**arg(5, 1120774))
hide p218
$ update_portrait('oc002_01 19', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120775)]' (**arg(6, 1120775))
$ update_portrait('oc002_01 19', 'p2', [r(-3), dark], 5)
$ update_portrait('st009_01 2', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120776)]' (**arg(7, 1120776))
$ update_portrait('st009_01 2', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120777)]' (**arg(8, 1120777))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st009_01 4', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120778)]' (**arg(9, 1120778))
hide p2
$ update_portrait('st009_01 4', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1120779)]' (**arg(10, 1120779))
hide p209
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120780)]' (**arg(11, 1120780))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1120781)]' (**arg(12, 1120781))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120782)]' (**arg(13, 1120782))
hide p1
$ update_portrait('st009_01 1', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1120783)]' (**arg(14, 1120783))
return