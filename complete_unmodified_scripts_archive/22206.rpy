label avg22206(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c21')
window show
with trans
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch15.ogg"
get_char('c21') '[convertstrid(1128608)]' (**arg(1, 1128608))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128609)]' (**arg(2, 1128609))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c5631') '[convertstrid(1128610)]' (**arg(3, 1128610))
get_char('c5621') '[convertstrid(1128611)]' (**arg(4, 1128611))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128612)]' (**arg(5, 1128612))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c5631') '[convertstrid(1128613)]' (**arg(6, 1128613))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1128614)]' (**arg(7, 1128614))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c5621') '[convertstrid(1128615)]' (**arg(8, 1128615))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1128616)]' (**arg(9, 1128616))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c5631') '[convertstrid(1128617)]' (**arg(10, 1128617))
hide p2
get_char('c5623') '[convertstrid(1128618)]' (**arg(11, 1128618))
get_char('c5623') '[convertstrid(1128619)]' (**arg(12, 1128619))
get_char('c5631') '[convertstrid(1128620)]' (**arg(13, 1128620))
get_char('c5631') '[convertstrid(1128621)]' (**arg(14, 1128621))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1128622)]' (**arg(15, 1128622))
return "avg22206"