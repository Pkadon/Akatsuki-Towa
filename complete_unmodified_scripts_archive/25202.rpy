label avg25202:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[convertstrid(1210689)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "other_7037.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1210690)]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5002.ogg"
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[convertstrid(1210691)]'
return