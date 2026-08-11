label avg25234(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1210832)]' (**arg(1, 1210832))
play sfx2 "common_36rewardsp.ogg"
get_char('c0') '[convertstrid(1210833)]' (**arg(2, 1210833))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210834)]' (**arg(3, 1210834))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210835)]' (**arg(4, 1210835))
return "avg25234"