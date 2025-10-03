label avg20028:

$ play_music("ed7150.ogg")
scene avg_bg_006
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1001691)]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
c2081 '[convertstrid(1001692)]'
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
c2081 '[convertstrid(1001693)]'
$ update_portrait('st008_01 1', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1001694)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1001695)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
c2081 '[convertstrid(1001696)]'
$ update_portrait('st008_01 5', 'p208', [l(-19), light, flip], 6)
c2081 '[convertstrid(1001697)]'
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
c2081 '[convertstrid(1001698)]'
hide p1
$ update_portrait('st008_01 1', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1001699)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1001700)]'
hide p208
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st007_01 1', 'p207', [l(-6), light, flip], 6)
c2071 '[convertstrid(1001701)]'
hide p207
$ update_portrait('st003_01 1', 'p203', [l(-7), light, flip], 6)
c2031 '[convertstrid(1001702)]'
$ update_portrait('st003_01 1', 'p203', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001703)]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1001704)]'
return