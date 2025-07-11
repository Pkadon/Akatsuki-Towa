label avg25240:

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7023.ogg"
c20143 '[textdict[1210861]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210862]]'
hide p1
play sfx2 "other_7022.ogg"
c20143 '[textdict[1210863]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210864]]'
hide p2
c20143 '[textdict[1210865]]'
play sfx2 "other_7080.ogg"
c20163 '[textdict[1210866]]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210867]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210868]]'
return