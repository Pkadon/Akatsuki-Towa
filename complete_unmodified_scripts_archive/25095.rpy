label avg25095:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210267)]' (**arg(1, 1210267))
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210268)]' (**arg(2, 1210268))
return