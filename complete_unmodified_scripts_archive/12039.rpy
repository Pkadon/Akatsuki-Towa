label avg12039:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
get_char('c21') '[convertstrid(1120274)]' (**arg(1, 1120274))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120275)]' (**arg(2, 1120275))
hide p2
hide p1
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
$ update_narrator('c2323')
with fade
get_char('c2323') '[convertstrid(1120276)]' (**arg(3, 1120276))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1120277)]' (**arg(4, 1120277))
get_char('c5381') '[convertstrid(1120278)]' (**arg(5, 1120278))
$ update_portrait('st033_01 1', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120279)]' (**arg(6, 1120279))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120280)]' (**arg(7, 1120280))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1120281)]' (**arg(8, 1120281))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120282)]' (**arg(9, 1120282))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120283)]' (**arg(10, 1120283))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120284)]' (**arg(11, 1120284))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1120285)]' (**arg(12, 1120285))
hide p232
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1120286)]' (**arg(13, 1120286))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120287)]' (**arg(14, 1120287))
return