label avg25145(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "fight_6017.ogg"
get_char('c0') '[convertstrid(1210459)]' (**arg(1, 1210459))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1210460)]' (**arg(2, 1210460))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210461)]' (**arg(3, 1210461))
return "avg25145"