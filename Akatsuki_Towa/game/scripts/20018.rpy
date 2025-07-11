label avg20018:

play music "ed7561.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7088.ogg"
c13 '[textdict[1001032]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1001033]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1001034]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "other_7020.ogg"
c13 '[textdict[1001035]]'
return