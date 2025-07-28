label avg25304:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1211170)]'
hide p2
c20253 '[convertstrid(1211171)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1211172)]'
hide p1
play sfx2 "common_36rewardsp.ogg"
c20253 '[convertstrid(1211173)]'
return