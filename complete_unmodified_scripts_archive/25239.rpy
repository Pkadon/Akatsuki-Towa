label avg25239(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210852)]' (**arg(1, 1210852))
hide p1
get_char('c20133') '[convertstrid(1210853)]' (**arg(2, 1210853))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210854)]' (**arg(3, 1210854))
hide p2
play sfx2 "other_7040.ogg"
get_char('c20133') '[convertstrid(1210855)]' (**arg(4, 1210855))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210856)]' (**arg(5, 1210856))
hide p2
play sfx2 "other_7057.ogg"
get_char('c20213') '[convertstrid(1210857)]' (**arg(6, 1210857))
get_char('c20133') '[convertstrid(1210858)]' (**arg(7, 1210858))
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210859)]' (**arg(8, 1210859))
return "avg25239"