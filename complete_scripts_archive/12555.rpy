label avg12555:

play music "ED6523.ogg"
scene avg_bg_081
window show
with fade_in
c12411 '[textdict[1153059]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1153060]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153061]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1153062]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1153063]]'
hide p4
c12411 '[textdict[1153064]]'
$ update_portrait('sc025_01 1', 'p622', [l_entrance(-1), light, flip], 6)
c6221 '[textdict[1153065]]'
hide p2
$ update_portrait('sc025_01 1', 'p622', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1153066]]'
hide p622
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1153067]]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153068]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
c43 '[textdict[1153069]]'
hide p3
hide p4
with fade
c12413 '[textdict[1153070]]'
$ update_portrait('sc025_01 1', 'p622', [l(-1), light, flip], 6)
c6221 '[textdict[1153071]]'
$ update_portrait('sc025_01 1', 'p622', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1153072]]'
hide p622
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153073]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1153074]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1153075]]'
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1153076]]'
hide p4
hide p1
with fade
c12413 '[textdict[1153077]]'
$ update_portrait('sc025_01 1', 'p622', [l(-1), light, flip], 6)
c6221 '[textdict[1153078]]'
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
c6221 '[textdict[1153079]]'
hide p622
c12411 '[textdict[1153080]]'
return