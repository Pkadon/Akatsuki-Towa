label avg12101:

play music "ed7111.ogg"
scene avg_bg_047
$ update_portrait('oc005_01 2', 'p5', [r(-6), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ji04.ogg"
c53 '[textdict[1128006]]'
$ update_portrait('oc005_01 2', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128011]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 5', 'p5', [r(-6), light], 5)
play sfxvoice "avg_vocal_ji06.ogg"
c53 '[textdict[1128012]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 5)
c53 '[textdict[1128013]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 5)
c53 '[textdict[1128014]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 9', 'p5', [r(-6), light], 5)
play sfxvoice "avg_vocal_ji16.ogg"
c53 '[textdict[1128015]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 5)
play sfxvoice "avg_vocal_ji05.ogg"
c53 '[textdict[1128016]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12104
    "[textdict[1100002]]":
        call avg12103
return