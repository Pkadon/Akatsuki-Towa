label avg10509:

play music "ED6300.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with fade_in
c43 '[convertstrid(1150483)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1150484)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1150485)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c12031 '[convertstrid(1150486)]'
return