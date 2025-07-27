label avg25195:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210655)]'
hide p1
play sfx2 "other_7039.ogg"
c20133 '[convertstrid(1210656)]'
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210657)]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1210658)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210659)]'
hide p1
c20133 '[convertstrid(1210660)]'
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na16.ogg"
c13 '[convertstrid(1210661)]'
return