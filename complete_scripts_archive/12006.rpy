label avg12006:

play music "ed7150.ogg"
scene avg_bg_012
$ update_portrait('st024_01 2', 'p223', [l(-16), light, flip], 6)
$ update_narrator('c2231')
window show
with fade_in
c2231 '[convertstrid(1007127)]'
$ update_portrait('st024_01 5', 'p223', [l(-16), light, flip], 6)
c2231 '[convertstrid(1007128)]'
$ update_portrait('st024_01 1', 'p223', [l(-16), light, flip], 6)
c2231 '[convertstrid(1007129)]'
hide p223
play sfx2 "other_7002.ogg"
c0 '[convertstrid(1007249)]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007130)]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('st024_01 2', 'p223', [l(-16), light, flip], 6)
c2231 '[convertstrid(1007131)]'
$ update_portrait('st024_01 2', 'p223', [l(-16), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007132)]'
scene avg_bg_018
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 5', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1007133)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1007134)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 5', 'p72', [l(-17), light, flip], 6)
c721 '[convertstrid(1007135)]'
hide p1
$ update_portrait('sc068_01 5', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007136)]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
c721 '[convertstrid(1007137)]'
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007138)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007139)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1007140)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1007141)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 5', 'p72', [l(-17), light, flip], 6)
c721 '[convertstrid(1007142)]'
return