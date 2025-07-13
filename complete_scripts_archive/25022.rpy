label avg25022:

stop music
scene placeholderbackground
$ update_narrator('c20103')
window show
with fade_in
play sfx2 "other_7079.ogg"
c20103 '[textdict[1210051]]'
c20103 '[textdict[1210052]]'
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_sc01_01.ogg"
c13 '[textdict[1210053]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210054]]'
return