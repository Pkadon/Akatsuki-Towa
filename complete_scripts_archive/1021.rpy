label avg1021:

play music "ed7150.ogg"
scene avg_bg_014
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(2100402)]'
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(2100403)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[convertstrid(2100404)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(2100405)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100406)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(2100407)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100408)]'
hide p2
$ update_portrait('oc004_01 7', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[convertstrid(2100409)]'
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100410)]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l_entrance(9), light, flip], 6)
c231 '[convertstrid(2100411)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100412)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(2100413)]'
$ update_portrait('oc004_01 1', 'p4', [r_exit(-5), light], 6)
c43 '[convertstrid(2100414)]'
hide p4
hide p23
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100415)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(2100416)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100417)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100418)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100419)]'
hide p1
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100420)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100421)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100422)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(2100423)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100424)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(2100425)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100426)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100427)]'
hide p1
$ update_portrait('oc002_01 16', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(2100428)]'
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100429)]'
$ update_portrait('sc015_01 2', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100430)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[convertstrid(2100431)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100432)]'
return