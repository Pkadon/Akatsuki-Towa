label avg10544:

$ play_music("ed7151.ogg")
scene avg_bg_078
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1152741)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152742)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
play sfx2 "other_7047.ogg"
c43 '[convertstrid(1152743)]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12351 '[convertstrid(1152744)]'
return