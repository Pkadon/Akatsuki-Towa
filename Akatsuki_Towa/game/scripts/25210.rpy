label avg25210:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch30.ogg"
c23 '[textdict[1210726]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfx2 "other_7088.ogg"
c13 '[textdict[1210727]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210728]]'
hide p2
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "common_sephi2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210729]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210730]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch29.ogg"
c23 '[textdict[1210731]]'
return