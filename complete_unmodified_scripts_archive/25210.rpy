label avg25210(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch30.ogg"
get_char('c23') '[convertstrid(1210726)]' (**arg(1, 1210726))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1210727)]' (**arg(2, 1210727))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210728)]' (**arg(3, 1210728))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "common_sephi2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210729)]' (**arg(4, 1210729))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210730)]' (**arg(5, 1210730))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c23') '[convertstrid(1210731)]' (**arg(6, 1210731))
return "avg25210"