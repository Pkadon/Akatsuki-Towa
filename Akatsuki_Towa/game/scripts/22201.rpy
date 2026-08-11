label avg22201(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128572)]' (**arg(1, 1128572))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1128573)]' (**arg(2, 1128573))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c5631') '[convertstrid(1128574)]' (**arg(3, 1128574))
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128575)]' (**arg(4, 1128575))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128576)]' (**arg(5, 1128576))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c5621') '[convertstrid(1128577)]' (**arg(6, 1128577))
get_char('c5621') '[convertstrid(1128580)]' (**arg(7, 1128580))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128581)]' (**arg(8, 1128581))
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128582)]' (**arg(9, 1128582))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
get_char('c5631') '[convertstrid(1128583)]' (**arg(10, 1128583))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li12.ogg"
get_char('c43') '[convertstrid(1128584)]' (**arg(11, 1128584))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1128585)]' (**arg(12, 1128585))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128586)]' (**arg(13, 1128586))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
get_char('c5623') '[convertstrid(1128587)]' (**arg(14, 1128587))
get_char('c5623') '[convertstrid(1128588)]' (**arg(15, 1128588))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128589)]' (**arg(16, 1128589))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch03_b.ogg"
get_char('c23') '[convertstrid(1128590)]' (**arg(17, 1128590))
return "avg22201"