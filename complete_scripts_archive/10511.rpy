label avg10511:

play music "ED6300.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
$ update_narrator('c43')
window show
with fade_in
c43 '[convertstrid(1150491)]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1150492)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1150493)]'
return