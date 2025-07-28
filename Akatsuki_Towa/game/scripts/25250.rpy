label avg25250:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210913)]'
hide p2
c20153 '[convertstrid(1210914)]'
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1210915)]'
hide p1
c20153 '[convertstrid(1210916)]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1210917)]'
hide p2
play sfx2 "other_7007.ogg"
c20153 '[convertstrid(1210918)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210919)]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210920)]'
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1210921)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c13 '[convertstrid(1210922)]'
return