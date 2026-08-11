label avg25318(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1211229)]' (**arg(1, 1211229))
play sfx2 "common_35rewardholy.ogg"
get_char('c0') '[convertstrid(1211230)]' (**arg(2, 1211230))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211231)]' (**arg(3, 1211231))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1211232)]' (**arg(4, 1211232))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211233)]' (**arg(5, 1211233))
return "avg25318"