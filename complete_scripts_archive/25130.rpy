label avg25130:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1210389]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210390]]'
return