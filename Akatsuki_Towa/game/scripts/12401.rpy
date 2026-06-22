label avg12401:

$ play_music("ed7100.ogg")
scene avg_bg_023
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1140226)]' (**arg(1, 1140226))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1140227)]' (**arg(2, 1140227))
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140228)]' (**arg(3, 1140228))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140229)]' (**arg(4, 1140229))
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1140230)]' (**arg(5, 1140230))
hide p4
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140231)]' (**arg(6, 1140231))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1140232)]' (**arg(7, 1140232))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140233)]' (**arg(8, 1140233))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch02.ogg"
get_char('c23') '[convertstrid(1140234)]' (**arg(9, 1140234))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140235)]' (**arg(10, 1140235))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140236)]' (**arg(11, 1140236))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140237)]' (**arg(12, 1140237))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140238)]' (**arg(13, 1140238))
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140239)]' (**arg(14, 1140239))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1140240)]' (**arg(15, 1140240))
return