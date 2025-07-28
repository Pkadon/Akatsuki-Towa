label avg10339:

play music "ed7105.ogg"
scene avg_bg_003
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1131035)]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131036)]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1131037)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1131038)]'
hide p3
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131039)]'
return