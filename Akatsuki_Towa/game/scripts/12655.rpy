label avg12655:

play music "ED6300.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1166365)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166366)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfx2 "other_7043.ogg"
c13 '[convertstrid(1166367)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166368)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166369)]'
hide p3
hide p1
play sfx2 "other_7045.ogg"
c0 '[convertstrid(1166370)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166371)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1166372)]'
return