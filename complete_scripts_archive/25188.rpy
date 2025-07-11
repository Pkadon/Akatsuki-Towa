label avg25188:

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210626]]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[1210627]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1210628]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210629]]'
return