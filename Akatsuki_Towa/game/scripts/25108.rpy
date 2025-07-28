label avg25108:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210316)]'
hide p1
c6123 '[convertstrid(1210317)]'
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210318)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210319)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c13 '[convertstrid(1210320)]'
return