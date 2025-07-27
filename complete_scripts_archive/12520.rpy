label avg12520:

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with fade_in
c131 '[convertstrid(1151252)]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1151253)]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1151254)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1151255)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151256)]'
return