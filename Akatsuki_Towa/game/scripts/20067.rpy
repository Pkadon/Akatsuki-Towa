label avg20067:

$ play_music("ed7150.ogg")
scene avg_bg_018
$ update_narrator('c6441')
window show
with fade_in
$ update_portrait('sc044_01 4', 'p644', [l_entrance(-7), light, flip], 6)
c6441 '[convertstrid(1003764)]'
$ update_portrait('sc044_01 4', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003765)]'
$ update_portrait('sc044_01 4', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003766)]'
$ update_portrait('sc044_01 3', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003767)]'
$ update_portrait('sc044_01 3', 'p644', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1003768)]'
hide p644
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1003769)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1003770)]'
hide p1
$ update_portrait('sc044_01 2', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003771)]'
hide p2
$ update_portrait('sc044_01 2', 'p644', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1003772)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc044_01 4', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003773)]'
hide p1
$ update_portrait('sc044_01 4', 'p644', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1003774)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc044_01 1', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003775)]'
$ update_portrait('sc044_01 1', 'p644', [l(-7), light, flip], 6)
c6441 '[convertstrid(1003776)]'
$ update_portrait('sc044_01 4', 'p644', [l_exit(-7), light, flip], 6)
c6441 '[convertstrid(1003777)]'
hide p644
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[convertstrid(1003778)]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[convertstrid(1003779)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1003780)]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[convertstrid(1003781)]'
return