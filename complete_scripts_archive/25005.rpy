label avg25005:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7079.ogg"
c23 '[textdict[1210007]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_sc01_01.ogg"
c13 '[textdict[1210008]]'
return