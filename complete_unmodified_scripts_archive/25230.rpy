label avg25230:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7059.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210818)]' (**arg(1, 1210818))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c13') '[convertstrid(1210819)]' (**arg(2, 1210819))
return