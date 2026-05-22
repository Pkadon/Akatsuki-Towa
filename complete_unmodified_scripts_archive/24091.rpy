label avg24091:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1200329)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st026_01 1', 'p225', [l(-14), light, flip], 6)
c2251 '[convertstrid(1200330)]'
$ update_portrait('st026_01 1', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1200331)]'
return