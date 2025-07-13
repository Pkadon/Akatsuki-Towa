label avg12180:

play music "ed7110.ogg"
scene avg_bg_003
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
$ update_narrator('c51')
window show
with fade_in
c51 '[textdict[1120580]]'
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji09.ogg"
c51 '[textdict[1120581]]'
$ update_portrait('oc005_01 16', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji07.ogg"
c51 '[textdict[1120582]]'
$ update_portrait('oc005_01 16', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1120583]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 9', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1120584]]'
hide p2
$ update_portrait('oc005_01 9', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1120585]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1120586]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 11', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji05.ogg"
c51 '[textdict[1120587]]'
hide p2
$ update_portrait('oc005_01 11', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1120588]]'
return