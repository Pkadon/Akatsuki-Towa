label avg12003:

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
c561 '[convertstrid(1007080)]'
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007081)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1007082)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1007083)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1007084)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1007085)]'
return