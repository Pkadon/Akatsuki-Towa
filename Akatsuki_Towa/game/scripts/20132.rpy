label avg20132:

scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "other_7049.ogg"
c11 '[textdict[1006660]]'
$ update_portrait('oc001_01 3', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[textdict[1006661]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1006662]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[textdict[1006663]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc044_01 2', 'p51', [l(-7), light, flip], 6)
c511 '[textdict[1006664]]'
$ update_portrait('sc044_01 2', 'p51', [l(-7), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1006665]]'
hide p3
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji03.ogg"
c7013 '[textdict[1006666]]'
hide p51
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1006667]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1006668]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc044_01 3', 'p51', [l(-7), light, flip], 6)
c511 '[textdict[1006669]]'
return