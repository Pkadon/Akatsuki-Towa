label avg25160:

scene placeholderbackground
window show
with fade_in
play sfx2 "fight_6022.ogg"
c20153 '[textdict[1210517]]'
play sfx2 "other_7080.ogg"
c20163 '[textdict[1210518]]'
c20153 '[textdict[1210519]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1210520]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[textdict[1210521]]'
return