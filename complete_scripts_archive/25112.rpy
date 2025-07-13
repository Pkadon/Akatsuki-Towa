label avg25112:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7092.ogg"
c13 '[textdict[1210332]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210333]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210334]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210335]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
c13 '[textdict[1210336]]'
return