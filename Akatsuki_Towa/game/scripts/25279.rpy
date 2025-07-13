label avg25279:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
play sfxvoice "bcv_oc001_arts_02.ogg"
c13 '[textdict[1211060]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1211061]]'
return