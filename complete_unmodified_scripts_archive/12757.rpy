label avg12757:

$ play_music("ed7511.ogg")
scene avg_bg_010
$ update_narrator('c14401')
window show
with fade_in
play sfx2 "fight_6002.ogg"
c14401 '[convertstrid(1174437)]'
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1174438)]'
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
c14521 '[convertstrid(1174439)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174440)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c14521 '[convertstrid(1174441)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1174442)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c14521 '[convertstrid(1174443)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174444)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st057_01 4', 'p1453', [l(-16), light, flip], 6)
c14531 '[convertstrid(1174445)]'
$ update_portrait('st057_01 4', 'p1453', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174446)]'
hide p1453
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1174447)]'
hide p3
c14401 '[convertstrid(1174448)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174449)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1174450)]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174451)]'
hide p1304
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c14401 '[convertstrid(1174452)]'
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1174453)]'
return