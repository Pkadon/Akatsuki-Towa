label avg10410:

play music "ed7151.ogg"
scene avg_bg_003
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
$ update_narrator('c33')
window show
with fade_in
play sfx2 "other_7046.ogg"
c33 '[convertstrid(1140624)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
c51 '[convertstrid(1140625)]'
$ update_portrait('oc005_01 8', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140626)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140627)]'
hide p3
$ update_portrait('oc005_01 2', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1140628)]'
hide p5
hide p2
c0 '[convertstrid(1140629)]'
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji20.ogg"
c51 '[convertstrid(1140630)]'
$ update_portrait('oc005_01 7', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140631)]' with shake
$ update_portrait('oc005_01 7', 'p5', [l(-6), l_shake, light, flip], 6)
c51 '[convertstrid(1140632)]'
$ update_portrait('oc005_01 7', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1140633)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1140634)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140635)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140636)]'
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140637)]'
$ update_portrait('oc005_01 12', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140638)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140639)]'
hide p3
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1140640)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140641)]'
hide p2
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140642)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140643)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1140644)]'
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1140645)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1140646)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 10', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji11.ogg"
c51 '[convertstrid(1140647)]'
return