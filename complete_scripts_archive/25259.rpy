label avg25259:

stop music
scene placeholderbackground
window show
with fade_in
play sfx2 "other_7043.ogg"
c20183 '[textdict[1210966]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210967]]'
hide p2
play sfx2 "other_7091.ogg"
c20183 '[textdict[1210968]]'
play sfx2 "other_7086.ogg"
c0 '[textdict[1210969]]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6026.ogg"
play sfxvoice "avg_vocal_ch13.ogg"
c23 '[textdict[1210970]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1210971]]'
return