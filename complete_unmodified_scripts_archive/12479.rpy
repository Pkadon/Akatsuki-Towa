label avg12479:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1144108)]'
c0 '[convertstrid(1144109)]'
c0 '[convertstrid(1144110)]'
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144111)]'
stop music
$ update_portrait('oc006_01 4', 'p6', [l(-5), dark, flip], 5)
play sfx2 "other_7080.ogg"
c10543 '[convertstrid(1144112)]'
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
c61 '[convertstrid(1144113)]'
$ play_music("ed7511.ogg")
hide p6
c0 '[convertstrid(1144114)]'
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144115)]'
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144116)]'
$ update_portrait('oc006_01 4', 'p6', [l(-5), l_shake, light, flip], 6)
c61 '[convertstrid(1144117)]'
return