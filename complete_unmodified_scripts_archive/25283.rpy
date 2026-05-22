label avg25283:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1211077)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1211078)]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[convertstrid(1211079)]'
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1211080)]'
hide p2
play sfx2 "other_7077.ogg"
c0 '[convertstrid(1211081)]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1211082)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1211083)]'
return