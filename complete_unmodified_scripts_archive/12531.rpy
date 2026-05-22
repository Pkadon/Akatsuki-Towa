label avg12531:

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('sc028_01 4', 'p36', [l(-7), light, flip], 6)
$ update_narrator('c361')
window show
with fade_in
c361 '[convertstrid(1151658)]'
$ update_portrait('sc028_01 4', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1151659)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1151660)]'
hide p36
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151661)]'
hide p3
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('sc007_01 5', 'p15', [r(-17), light], 6)
c153 '[convertstrid(1151662)]'
hide p13
$ update_portrait('sc007_01 5', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1151663)]'
return