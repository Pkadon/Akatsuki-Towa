label avg10435:
stop music

play music "ed7526.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1141515]]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1141516]]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141517]]'
hide p1
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1141518]]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141519]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1141520]]'
hide p3
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141521]]'
play music "ed7516.ogg"
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1141522]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141523]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1141524]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1141525]]'
hide p2
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1141526]]'
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1141527]]'
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141528]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1141529]]'
menu:
    extend ""
    "[textdict[1141530]]":
        call avg10436
    "[textdict[1141531]]":
        call avg10437
    "[textdict[1141532]]":
        call avg10438
return