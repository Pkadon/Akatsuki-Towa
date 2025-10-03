label avg12477:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1144081)]'
c0 '[convertstrid(1144082)]'
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144083)]'
$ update_portrait('oc006_01 3', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144084)]'
scene avg_bg_070
show memoryoverlay zorder 2
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
c43 '[convertstrid(1144085)]'
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1144086)]'
scene placeholderbackground
$ update_narrator('c61')
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
with fade
$ update_portrait('oc006_01 4', 'p6', [l(-5), l_shake, light, flip], 6)
c61 '[convertstrid(1144087)]'
hide p6
c0 '[convertstrid(1144088)]'
c0 '[convertstrid(1144089)]'
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
c61 '[convertstrid(1144090)]'
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
c61 '[convertstrid(1144091)]'
hide p6
c0 '[convertstrid(1144092)]'
return