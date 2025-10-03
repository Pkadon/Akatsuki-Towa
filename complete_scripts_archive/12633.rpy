label avg12633:

$ play_music("ed7126.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1162690)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1162691)]'
hide p1
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1162692)]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1162693)]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1162694)]'
hide p3
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st062_01 4', 'p1308', [r(-16), light], 6)
c13083 '[convertstrid(1162695)]'
hide p4
$ update_portrait('st062_01 4', 'p1308', [r(-16), dark], 5)
$ update_portrait('sc010_01 5', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1162696)]'
hide p1308
$ update_portrait('sc010_01 5', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1162697)]'
hide p18
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1162698)]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1162699)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1162700)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1162701)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 5', 'p18', [l(-10), l_shake, light, flip], 6)
c181 '[convertstrid(1162702)]'
hide p1
$ update_portrait('sc010_01 5', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1162703)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1162704)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1162705)]' with shake
return