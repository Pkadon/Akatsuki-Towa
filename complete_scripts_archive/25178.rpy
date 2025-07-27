label avg25178:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7067.ogg"
c13 '[convertstrid(1210571)]'
hide p1
c20133 '[convertstrid(1210572)]'
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1210573)]'
hide p1
play sfx2 "other_7039.ogg"
c20133 '[convertstrid(1210574)]'
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[convertstrid(1210575)]'
return