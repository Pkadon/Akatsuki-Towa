label avg25175(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210561)]' (**arg(1, 1210561))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210562)]' (**arg(2, 1210562))
hide p2
play sfx2 "elc_5002.ogg"
get_char('c0') '[convertstrid(1210563)]' (**arg(3, 1210563))
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
get_char('c13') '[convertstrid(1210564)]' (**arg(4, 1210564))
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1210565)]' (**arg(5, 1210565))
hide p2
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210566)]' (**arg(6, 1210566))
return "avg25175"