label avg10428:
stop music

play music "ed7526.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1141284]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1141285]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1141286]]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1141287]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1141288]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141289]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1141290]]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
c31 '[textdict[1141291]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1141292]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141293]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1141294]]'
hide p4
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141295]]'
hide p4
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141296]]'
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141297]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1141298]]'
menu:
    extend ""
    "[textdict[1141299]]":
        call avg10431
    "[textdict[1141300]]":
        call avg10429
    "[textdict[1141301]]":
        call avg10430
return