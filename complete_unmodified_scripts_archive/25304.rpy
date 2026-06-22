label avg25304:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1211170)]' (**arg(1, 1211170))
hide p2
get_char('c20253') '[convertstrid(1211171)]' (**arg(2, 1211171))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1211172)]' (**arg(3, 1211172))
hide p1
play sfx2 "common_36rewardsp.ogg"
get_char('c20253') '[convertstrid(1211173)]' (**arg(4, 1211173))
return