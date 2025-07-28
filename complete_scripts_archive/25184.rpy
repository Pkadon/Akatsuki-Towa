label avg25184:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1210602)]'
hide p1
c6123 '[convertstrid(1210603)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210604)]'
hide p2
c20213 '[convertstrid(1210605)]'
c20213 '[convertstrid(1210606)]'
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[convertstrid(1210607)]'
hide p1
c20213 '[convertstrid(1210608)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1210609)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c13 '[convertstrid(1210610)]'
return