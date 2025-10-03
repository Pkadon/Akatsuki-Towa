label avg10336:

$ play_music("ed7105.ogg")
scene avg_bg_003
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[convertstrid(1130999)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131024)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131025)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131026)]'
hide p2
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131027)]'
hide p4
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1131028)]'
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131029)]'
menu:
    extend ""
    "[textdict[1131030]]":
        call avg10338
    "[textdict[1131031]]":
        call avg10339
return