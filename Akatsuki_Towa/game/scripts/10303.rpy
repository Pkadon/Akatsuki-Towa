label avg10303:

play music "ed7116.ogg"
scene avg_bg_020
$ update_narrator('c5381')
window show
with fade_in
play sfx2 "other_7020.ogg"
c5381 '[convertstrid(1130125)]'
$ update_portrait('st033_01 2', 'p232', [r_entrance(-7), light], 6)
c2323 '[convertstrid(1130126)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130127)]'
c5381 '[convertstrid(1130128)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1130129)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130130)]'
c5381 '[convertstrid(1130131)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1130132)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130133)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1130134)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130135)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1130136)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130137)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1130138)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1130139)]'
c5381 '[convertstrid(1130140)]'
$ update_portrait('st033_01 6', 'p232', [r_exit(-7), light], 6)
play sfx2 "other_7020.ogg"
c2323 '[convertstrid(1130141)]'
hide p232
play music "ed7101.ogg"
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
c31 '[convertstrid(1130142)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1130143)]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1130144)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1130145)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1130146)]'
return