label avg20073:

play music "ed7117.ogg"
scene avg_bg_021
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1003930)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1003931)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1003932)]'
hide p1
hide p3
c0 '[convertstrid(1003933)]'
play sfx2 "other_7004.ogg"
c6541 '[convertstrid(1003934)]'
c6553 '[convertstrid(1003935)]'
c6541 '[convertstrid(1003936)]'
c6541 '[convertstrid(1003937)]'
c6541 '[convertstrid(1003938)]'
c6553 '[convertstrid(1003939)]'
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfx2 "other_7047.ogg"
c31 '[convertstrid(1003940)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1123026)]'
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1003941)]'
hide p4
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1003942)]'
return