label avg25108:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210316]]'
hide p1
c6123 '[textdict[1210317]]'
play sfx2 "other_7092.ogg"
c0 '[textdict[1210318]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210319]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
c13 '[textdict[1210320]]'
return