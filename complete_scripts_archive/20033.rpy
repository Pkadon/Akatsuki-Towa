label avg20033:

$ play_music("ed7104.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1002223)]'
c0 '[convertstrid(1002224)]'
c0 '[convertstrid(1002225)]'
c0 '[convertstrid(1002226)]'
c0 '[convertstrid(1002227)]'
c0 '[convertstrid(1002228)]'
c0 '[convertstrid(1002229)]'
c0 '[convertstrid(1002230)]'
c0 '[convertstrid(1002231)]'
c0 '[convertstrid(1002232)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1002233)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
c31 '[convertstrid(1002234)]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002235)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002236)]'
hide p2
hide p1
c0 '[convertstrid(1002237)]'
c0 '[convertstrid(1002238)]'
c0 '[convertstrid(1002239)]'
c0 '[convertstrid(1002240)]'
c0 '[convertstrid(1002241)]'
c0 '[convertstrid(1002242)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1002243)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002244)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1002245)]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002246)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
c5613 '[convertstrid(1002247)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
c11 '[convertstrid(1002248)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1002249)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1002250)]'
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1002251)]'
hide p3
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
c5613 '[convertstrid(1002252)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
c11 '[convertstrid(1002253)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
c5613 '[convertstrid(1002254)]'
return