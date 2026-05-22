label avg1038:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
$ update_narrator('c581')
window show
with fade_in
c581 '[convertstrid(2100613)]'
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100614)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100615)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[convertstrid(2100616)]'
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[convertstrid(2100617)]'
hide p1
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100618)]'
return