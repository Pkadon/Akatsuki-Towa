label avg20133:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1006670)]'
$ update_portrait('sc051_01 4', 'p58', [r_entrance(-32), light], 6)
play sfx2 "other_7049.ogg"
c583 '[convertstrid(1006671)]'
$ update_portrait('sc051_01 4', 'p58', [r(-32), dark], 5)
$ update_portrait('sc050_01 4', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(1006672)]'
$ update_portrait('sc050_01 4', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 4', 'p58', [r(-32), light], 6)
c583 '[convertstrid(1006673)]'
hide p58
play sfx2 "elc_5005.ogg"
c6653 '[convertstrid(1004289)]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(1006675)]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 2', 'p58', [r(-32), light], 6)
play sfx2 "fight_6003.ogg"
c583 '[convertstrid(1006676)]'
$ update_portrait('sc051_01 2', 'p58', [r(-32), dark], 5)
$ update_portrait('sc050_01 2', 'p57', [l(-19), light, flip], 6)
play sfx2 "fight_6024.ogg"
c571 '[convertstrid(1006677)]'
return