label avg25134:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na18.ogg"
c13 '[textdict[1210405]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210406]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfx2 "other_7088.ogg"
c13 '[textdict[1210407]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210408]]'
return