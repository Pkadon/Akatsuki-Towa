label avg12383:

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('st040_01 5', 'p1043', [l(-19), light, flip], 6)
$ update_narrator('c10431')
window show
with fade_in
c10431 '[convertstrid(1133897)]'
$ update_portrait('st040_01 5', 'p1043', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133898)]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 2', 'p1043', [l(-19), light, flip], 6)
c10431 '[convertstrid(1133899)]'
hide p1043
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[convertstrid(1133900)]'
hide p2
$ update_portrait('st040_01 6', 'p1043', [l(-19), light, flip], 6)
play sfx2 "common_quest.ogg"
c10431 '[convertstrid(1133901)]'
return