label avg25136:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210417]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210418]]'
hide p2
play sfx2 "other_7004.ogg"
c0 '[textdict[1210419]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210420]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1210421]]'
return