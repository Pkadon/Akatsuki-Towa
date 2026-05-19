label avg24008:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1200025)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
c7431 '[convertstrid(1200026)]'
c7431 '[convertstrid(1200027)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1200028)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1200029)]'
return