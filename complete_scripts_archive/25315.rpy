label avg25315:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1211210]]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na16.ogg"
c13 '[textdict[1211211]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
c23 '[textdict[1211212]]'
hide p2
play sfx2 "other_7093.ogg"
c20153 '[textdict[1211213]]'
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na18.ogg"
c13 '[textdict[1211214]]'
hide p1
c20153 '[textdict[1211215]]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1211216]]'
hide p2
c20153 '[textdict[1211217]]'
play sfx2 "other_7086.ogg"
c0 '[textdict[1211218]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1211219]]'
return