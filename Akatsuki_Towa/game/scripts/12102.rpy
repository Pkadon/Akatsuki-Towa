label avg12102:

stop music
scene avg_bg_012
$ update_portrait('st051_01 6', 'p709', [r(-9), light], 6)
$ update_narrator('c7093')
window show
with fade_in
play sfx2 "other_7042.ogg"
c7093 '[convertstrid(1128007)]'
$ update_portrait('st051_01 6', 'p709', [r(-9), dark], 5)
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128008)]'
$ update_portrait('oc001_01 6', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st051_01 2', 'p709', [r(-9), light], 6)
c7093 '[convertstrid(1128009)]'
$ play_music("ed7111.ogg")
scene avg_bg_047
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
with fade
play sfxvoice "avg_vocal_ji07.ogg"
c53 '[convertstrid(1128010)]'
$ update_portrait('oc005_01 1', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128011)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 5', 'p5', [r(-6), light], 6)
play sfxvoice "avg_vocal_ji06.ogg"
c53 '[convertstrid(1128012)]'
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1128013)]'
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1128014)]'
$ update_portrait('oc005_01 9', 'p5', [r(-6), light], 6)
play sfxvoice "avg_vocal_ji16.ogg"
c53 '[convertstrid(1128015)]'
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfxvoice "avg_vocal_ji05.ogg"
c53 '[convertstrid(1128016)]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12104
    "[textdict[1100002]]":
        call avg12103
return