label avg24006:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200019)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c7431 '[convertstrid(1200020)]'
c7431 '[convertstrid(1200021)]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1200022)]'
return