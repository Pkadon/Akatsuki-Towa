label avg25204(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1210695)]' (**arg(1, 1210695))
hide p2
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210696)]' (**arg(2, 1210696))
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1210697)]' (**arg(3, 1210697))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_sephi2.ogg"
get_char('c13') '[convertstrid(1210698)]' (**arg(4, 1210698))
return "avg25204"