label avg25256:

stop music
scene placeholderbackground
window show
with fade_in
c20093 '[textdict[1210949]]'
play sfx2 "other_7077.ogg"
c20163 '[textdict[1210950]]'
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na23.ogg"
c13 '[textdict[1210951]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_com_01.ogg"
c23 '[textdict[1210952]]'
return